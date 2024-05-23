import os
import streamlit as st
import pandas as pd
import openai
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ics import Calendar, Event

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize an empty DataFrame to store PR activities
columns = ['Event', 'Date', 'Details']
if 'pr_activities' not in st.session_state:
    st.session_state.pr_activities = pd.DataFrame(columns=columns)

def add_event(event, date, details):
    try:
        new_event = pd.DataFrame([{'Event': event, 'Date': date, 'Details': details}])
        st.session_state.pr_activities = pd.concat([st.session_state.pr_activities, new_event], ignore_index=True)
        st.session_state.pr_activities.to_csv('pr_campaign.csv', index=False)
        st.success(f"Event '{event}' on {date} added successfully!")
    except Exception as e:
        st.error(f"An error occurred while adding the event: {e}")

def view_events():
    try:
        if st.session_state.pr_activities.empty:
            st.warning("No events planned.")
        else:
            st.dataframe(st.session_state.pr_activities)
    except Exception as e:
        st.error(f"An error occurred while viewing the events: {e}")

def edit_event(index, event=None, date=None, details=None):
    try:
        if index in st.session_state.pr_activities.index:
            if event:
                st.session_state.pr_activities.at[index, 'Event'] = event
            if date:
                st.session_state.pr_activities.at[index, 'Date'] = date
            if details:
                st.session_state.pr_activities.at[index, 'Details'] = details
            st.session_state.pr_activities.to_csv('pr_campaign.csv', index=False)
            st.success(f"Event at index {index} updated successfully!")
        else:
            st.error(f"No event found at index {index}.")
    except Exception as e:
        st.error(f"An error occurred while editing the event: {e}")

def delete_event(index):
    try:
        if index in st.session_state.pr_activities.index:
            st.session_state.pr_activities = st.session_state.pr_activities.drop(index)
            st.session_state.pr_activities.to_csv('pr_campaign.csv', index=False)
            st.success(f"Event at index {index} deleted successfully!")
        else:
            st.error(f"No event found at index {index}.")
    except Exception as e:
        st.error(f"An error occurred while deleting the event: {e}")

def collect_author_info():
    try:
        author_name = st.text_input("Enter the author name:")
        author_email = st.text_input("Enter the author email:")
        book_title = st.text_input("Enter the book title:")
        book_genre = st.text_input("Enter the book genre:")
        author_goal = st.text_input("What is your main goal for this book? (e.g., increase sales, build brand, etc.):")
        target_audience = st.text_input("Describe your target audience:")
        book_release_date = st.date_input("Enter the book release date (tentative):")
        return {
            "author_name": author_name,
            "author_email": author_email,
            "title": book_title,
            "genre": book_genre,
            "goal": author_goal,
            "audience": target_audience,
            "release_date": book_release_date
        }
    except Exception as e:
        st.error(f"An error occurred while collecting author information: {e}")
        return None

def generate_marketing_strategy(author_info):
    prompt = f"""
    I am a book marketing expert. Based on the following details about a book and its author, generate a comprehensive book marketing strategy.

    Author Name: {author_info['author_name']}
    Author Email: {author_info['author_email']}
    Book Title: {author_info['title']}
    Genre: {author_info['genre']}
    Target Audience: {author_info['audience']}
    Main Goal: {author_info['goal']}
    Book Release Date: {author_info['release_date']}

    Provide detailed steps and strategies, including matching the author with media, PR agencies, or agents, and generating social media posts, blog posts, press releases, and pitch emails to influencers, media companies, book clubs, local libraries, elementary schools, and colleges. Also, include a book launch strategy with social media marketing, Amazon, and Google ads plan.
    """

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        strategy = response.choices[0].text.strip()
        return strategy
    except openai.error.OpenAIError as e:
        st.error(f"An error occurred while generating the marketing strategy: {e}")
        return None

def generate_pdf_report(author_info, marketing_strategy):
    try:
        pdf_filename = "Book_Marketing_Campaign_Report.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter

        # Title
        c.setFont("Helvetica-Bold", 20)
        c.drawString(30, height - 50, "Book Marketing Campaign Report")

        # Subtitle
        c.setFont("Helvetica", 12)
        c.drawString(30, height - 80, f"Book: {author_info['title']}")

        # Author Information
        c.setFont("Helvetica-Bold", 16)
        c.drawString(30, height - 110, "Author Information")
        y = height - 130
        c.setFont("Helvetica", 12)
        c.drawString(30, y, f"Name: {author_info['author_name']}")
        y -= 20
        c.drawString(30, y, f"Email: {author_info['author_email']}")
        y -= 20
        c.drawString(30, y, f"Book Title: {author_info['title']}")
        y -= 20
        c.drawString(30, y, f"Genre: {author_info['genre']}")
        y -= 20
        c.drawString(30, y, f"Goal: {author_info['goal']}")
        y -= 20
        c.drawString(30, y, f"Target Audience: {author_info['audience']}")
        y -= 20
        c.drawString(30, y, f"Release Date: {author_info['release_date']}")

        # Marketing Strategy
        y -= 40
        c.setFont("Helvetica-Bold", 16)
        c.drawString(30, y, "Marketing Strategy")
        y -= 20
        c.setFont("Helvetica", 12)
        for line in marketing_strategy.split('\n'):
            c.drawString(30, y, line.strip())
            y -= 15
            if y < 100:  # Start a new page if space is running out
                c.showPage()
                y = height - 50

        c.save()
        st.success("PDF report generated successfully!")
        st.download_button(
            label="Download PDF",
            data=open(pdf_filename, "rb").read(),
            file_name=pdf_filename,
            mime="application/pdf",
        )
    except Exception as e:
        st.error(f"An error occurred while generating the PDF report: {e}")

def export_to_ical():
    try:
        c = Calendar()

        for index, row in st.session_state.pr_activities.iterrows():
            e = Event()
            e.name = row['Event']
            e.begin = row['Date']
            e.description = row['Details']
            c.events.add(e)

        with open('pr_campaign.ics', 'w') as my_file:
            my_file.writelines(c)
        st.success("iCal file generated successfully!")
    except Exception as e:
        st.error(f"An error occurred while exporting to iCal: {e}")

def main():
    st.title("Book Marketing Campaign Planner")

    menu = ["Book Marketing Strategy", "Book Launch Strategy", "Promo and Marketing Pitch Email Generator"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Book Marketing Strategy":
        author_info = collect_author_info()
        if author_info and st.button("Generate Marketing Strategy"):
            marketing_strategy = generate_marketing_strategy(author_info)
            if marketing_strategy:
                st.text_area("Generated Marketing Strategy:", marketing_strategy)
                st.session_state.marketing_strategy = marketing_strategy
                st.session_state.author_info = author_info

    elif choice == "Book Launch Strategy":
        if "marketing_strategy" in st.session_state:
            generate_pdf_report(st.session_state.author_info, st.session_state.marketing_strategy)
        else:
            st.warning("Please generate the marketing strategy first.")

    elif choice == "Promo and Marketing Pitch Email Generator":
        st.text("Generate promotional and marketing pitch emails based on the type of recipient.")
        recipient_type = st.selectbox("Select Recipient Type", ["Influencer", "Media Company", "Book Club", "Local Library", "Elementary School", "College"])
        author_info = collect_author_info()
       
