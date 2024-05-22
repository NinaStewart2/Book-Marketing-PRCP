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
columns = ['Activity', 'Date', 'Details']
if 'pr_activities' not in st.session_state:
    st.session_state.pr_activities = pd.DataFrame(columns=columns)

def add_activity(activity, date, details):
    new_activity = pd.DataFrame([{'Activity': activity, 'Date': date, 'Details': details}])
    st.session_state.pr_activities = pd.concat([st.session_state.pr_activities, new_activity], ignore_index=True)
    st.session_state.pr_activities.to_csv('pr_campaign.csv', index=False)
    st.success(f"Activity '{activity}' on {date} added successfully!")

def view_activities():
    if st.session_state.pr_activities.empty:
        st.warning("No activities planned.")
    else:
        st.dataframe(st.session_state.pr_activities)

def edit_activity(index, activity=None, date=None, details=None):
    if index in st.session_state.pr_activities.index:
        if activity:
            st.session_state.pr_activities.at[index, 'Activity'] = activity
        if date:
            st.session_state.pr_activities.at[index, 'Date'] = date
        if details:
            st.session_state.pr_activities.at[index, 'Details'] = details
        st.session_state.pr_activities.to_csv('pr_campaign.csv', index=False)
        st.success(f"Activity at index {index} updated successfully!")
    else:
        st.error(f"No activity found at index {index}.")

def delete_activity(index):
    if index in st.session_state.pr_activities.index:
        st.session_state.pr_activities = st.session_state.pr_activities.drop(index)
        st.session_state.pr_activities.to_csv('pr_campaign.csv', index=False)
        st.success(f"Activity at index {index} deleted successfully!")
    else:
        st.error(f"No activity found at index {index}.")

def collect_author_info():
    book_title = st.text_input("Enter the book title:")
    book_genre = st.text_input("Enter the book genre:")
    target_audience = st.text_input("Describe your target audience:")
    author_goal = st.text_input("What is your main goal for this book? (e.g., increase sales, build brand, etc.):")
    return {
        "title": book_title,
        "genre": book_genre,
        "audience": target_audience,
        "goal": author_goal
    }

def generate_marketing_strategy(author_info):
    prompt = f"""
    I am a book marketing expert. Based on the following details about a book and its author, generate a comprehensive book marketing strategy.

    Book Title: {author_info['title']}
    Genre: {author_info['genre']}
    Target Audience: {author_info['audience']}
    Main Goal: {author_info['goal']}

    Provide detailed steps and strategies.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    strategy = response.choices[0].text.strip()
    return strategy

def generate_pdf_report(author_info, marketing_strategy):
    c = canvas.Canvas("PR_Campaign_Report.pdf", pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, height - 50, "PR Campaign Report")

    # Subtitle
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 80, f"Book: {author_info['title']}")

    # Marketing Strategy
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 110, "Marketing Strategy")

    y = height - 140
    for line in marketing_strategy.split('\n'):
        c.setFont("Helvetica", 12)
        c.drawString(30, y, line.strip())
        y -= 15
        if y < 100:  # Start a new page if space is running out
            c.showPage()
            y = height - 50

    # PR Activities
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, y, "PR Activities")
    y -= 20

    # Table headers
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y, "Activity")
    c.drawString(200, y, "Date")
    c.drawString(300, y, "Details")
    y -= 20

    # Table rows
    c.setFont("Helvetica", 12)
    for index, row in st.session_state.pr_activities.iterrows():
        c.drawString(30, y, str(row['Activity']))
        c.drawString(200, y, str(row['Date']))
        c.drawString(300, y, str(row['Details']))
        y -= 20
        if y < 100:  # Start a new page if space is running out
            c.showPage()
            y = height - 50

    c.save()
    st.success("PDF report generated successfully!")

def export_to_ical():
    c = Calendar()

    for index, row in st.session_state.pr_activities.iterrows():
        e = Event()
        e.name = row['Activity']
        e.begin = row['Date']
        e.description = row['Details']
        c.events.add(e)

    with open('pr_campaign.ics', 'w') as my_file:
        my_file.writelines(c)
    st.success("iCal file generated successfully!")

def main():
    st.title("PR Campaign Planner")

    menu = ["Add Activity", "View Activities", "Edit Activity", "Delete Activity",
            "Collect Author Info", "Generate Marketing Strategy", "Generate PDF Report",
            "Export to iCal"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Activity":
        activity = st.text_input("Enter activity name:")
        date = st.text_input("Enter date (YYYY-MM-DD):")
        details = st.text_input("Enter details:")
        if st.button("Add"):
            add_activity(activity, date, details)

    elif choice == "View Activities":
        view_activities()

    elif choice == "Edit Activity":
        index = st.number_input("Enter the index of the activity to edit:", min_value=0)
        activity = st.text_input("Enter new activity name (leave blank to keep unchanged):")
        date = st.text_input("Enter new date (YYYY-MM-DD, leave blank to keep unchanged):")
        details = st.text_input("Enter new details (leave blank to keep unchanged):")
        if st.button("Edit"):
            edit_activity(index, activity if activity else None, date if date else None, details if details else None)

    elif choice == "Delete Activity":
        index = st.number_input("Enter the index of the activity to delete:", min_value=0)
        if st.button("Delete"):
            delete_activity(index)

    elif choice == "Collect Author Info":
        author_info = collect_author_info()
        if st.button("Save Info"):
            st.session_state.author_info = author_info

    elif choice == "Generate Marketing Strategy":
        if "author_info" in st.session_state:
            marketing_strategy = generate_marketing_strategy(st.session_state.author_info)
            st.session_state.marketing_strategy = marketing_strategy
            st.text_area("Generated Marketing Strategy:", marketing_strategy)
        else:
            st.warning("Please collect author info first (Option 5).")

    elif choice == "Generate PDF Report":
        if "author_info" in st.session_state and "marketing_strategy" in st.session_state:
            generate_pdf_report(st.session_state.author_info, st.session_state.marketing_strategy)
        else:
            st.warning("Please collect author info and generate marketing strategy first (Options 5 and 6).")

    elif choice == "Export to iCal":
        export_to_ical()

if __name__ == "__main__":
    main()

