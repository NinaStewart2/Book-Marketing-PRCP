import os
import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ics import Calendar, Event

class BookMarketingStrategy:
    def __init__(self, book_title, author_name, genre, target_audience, release_date, book_description, author_bio):
        self.book_title = book_title
        self.author_name = author_name
        self.genre = genre
        self.target_audience = target_audience
        self.release_date = release_date
        self.book_description = book_description
        self.author_bio = author_bio
        self.strategy = []

    def create_strategy(self, is_non_fiction=False):
        self.add_overview()
        if is_non_fiction:
            self.add_pre_launch_non_fiction()
            self.add_launch_non_fiction()
            self.add_post_launch_non_fiction()
            self.add_additional_ideas_non_fiction()
        else:
            self.add_pre_launch()
            self.add_launch()
            self.add_post_launch()
            self.add_additional_ideas()

    def add_overview(self):
        overview = {
            "title": "Overview",
            "details": f"Book Title: {self.book_title}\n"
                       f"Author Name: {self.author_name}\n"
                       f"Genre: {self.genre}\n"
                       f"Target Audience: {self.target_audience}\n"
                       f"Release Date: {self.release_date}\n"
                       f"Book Description: {self.book_description}\n"
                       f"Author Bio: {self.author_bio}\n"
        }
        self.strategy.append(overview)

    def add_pre_launch(self):
        pre_launch = {
            "title": "Pre-Launch Strategy",
            "details": [
                "1. Cover Reveal: Share the cover on social media platforms, book blogs, and newsletters.",
                "2. Author Website: Ensure the author’s website is updated with a dedicated page for the new book.",
                "3. Email List Building: Create a sign-up form on the website for updates and exclusive content.",
                "4. Advanced Reader Copies (ARCs): Distribute ARCs to book bloggers, influencers, and reviewers.",
                "5. Social Media Teasers: Post snippets, character introductions, and quotes from the book.",
                "6. Book Trailer: Create and share a book trailer on YouTube and social media platforms.",
                "7. Collaborations: Partner with other authors or influencers for cross-promotions."
            ]
        }
        self.strategy.append(pre_launch)

    def add_pre_launch_non_fiction(self):
        pre_launch = {
            "title": "Pre-Launch Strategy",
            "details": [
                "1. Cover Reveal: Share the cover on social media platforms, book blogs, and newsletters.",
                "2. Author Website: Ensure the author’s website is updated with a dedicated page for the new book.",
                "3. Email List Building: Create a sign-up form on the website for updates and exclusive content.",
                "4. Advanced Reader Copies (ARCs): Distribute ARCs to industry experts, influencers, and reviewers.",
                "5. Social Media Teasers: Post snippets, key takeaways, and infographics from the book.",
                "6. Book Trailer: Create and share a book trailer on YouTube and social media platforms.",
                "7. Guest Blogging: Write guest posts for popular blogs in your book’s niche."
            ]
        }
        self.strategy.append(pre_launch)

    def add_launch(self):
        launch = {
            "title": "Launch Strategy",
            "details": [
                "1. Virtual Launch Party: Host a live event on platforms like Facebook, Instagram, or YouTube.",
                "2. Social Media Blitz: Schedule multiple posts across all social media platforms.",
                "3. Email Campaign: Send a launch announcement to the email list with purchase links.",
                "4. Book Giveaways: Organize giveaways on Goodreads, Instagram, or through the author’s newsletter.",
                "5. Press Release: Distribute a press release to relevant media outlets and book blogs.",
                "6. Paid Advertising: Utilize Facebook Ads, Instagram Ads, and Amazon Ads to reach a wider audience.",
                "7. Influencer Marketing: Collaborate with influencers to promote the book on their channels."
            ]
        }
        self.strategy.append(launch)

    def add_launch_non_fiction(self):
        launch = {
            "title": "Launch Strategy",
            "details": [
                "1. Virtual Launch Party: Host a live event on platforms like Facebook, Instagram, or YouTube.",
                "2. Social Media Blitz: Schedule multiple posts across all social media platforms.",
                "3. Email Campaign: Send a launch announcement to the email list with purchase links.",
                "4. Book Giveaways: Organize giveaways on Goodreads, Instagram, or through the author’s newsletter.",
                "5. Press Release: Distribute a press release to relevant media outlets and industry publications.",
                "6. Paid Advertising: Utilize Facebook Ads, Instagram Ads, LinkedIn Ads, and Google Ads to reach a wider audience.",
                "7. Influencer Marketing: Collaborate with influencers and thought leaders in your niche to promote the book on their channels."
            ]
        }
        self.strategy.append(launch)

    def add_post_launch(self):
        post_launch = {
            "title": "Post-Launch Strategy",
            "details": [
                "1. Book Signings: Arrange book signings at local bookstores, libraries, and literary events.",
                "2. Ongoing Social Media Engagement: Continue engaging with readers through posts, stories, and Q&A sessions.",
                "3. Book Clubs: Encourage book clubs to feature the book and offer to join their discussions.",
                "4. Podcast Interviews: Seek opportunities for the author to be interviewed on podcasts related to the book's genre.",
                "5. Continued Advertising: Maintain a consistent advertising presence on relevant platforms.",
                "6. Book Reviews: Encourage readers to leave reviews on Amazon, Goodreads, and other platforms."
            ]
        }
        self.strategy.append(post_launch)

    def add_post_launch_non_fiction(self):
        post_launch = {
            "title": "Post-Launch Strategy",
            "details": [
                "1. Speaking Engagements: Arrange speaking engagements at industry conferences, webinars, and podcasts.",
                "2. Ongoing Social Media Engagement: Continue engaging with readers through posts, stories, and Q&A sessions.",
                "3. Book Clubs: Encourage book clubs and professional groups to feature the book and offer to join their discussions.",
                "4. Podcast Interviews: Seek opportunities for the author to be interviewed on podcasts related to the book's topic.",
                "5. Continued Advertising: Maintain a consistent advertising presence on relevant platforms.",
                "6. Book Reviews: Encourage readers to leave reviews on Amazon, Goodreads, and other platforms."
            ]
        }
        self.strategy.append(post_launch)

    def add_additional_ideas(self):
        additional_ideas = {
            "title": "Additional Creative Ideas",
            "details": [
                "1. Interactive Website Features: Add interactive elements like quizzes, character profiles, and maps.",
                "2. Merchandise: Create and sell merchandise related to the book (e.g., T-shirts, bookmarks).",
                "3. Book Club Kits: Provide downloadable book club kits with discussion questions and author insights.",
                "4. Author Blog: Start a blog with behind-the-scenes content, writing tips, and personal stories.",
                "5. Themed Events: Host events or contests related to the book's themes or settings.",
                "6. Serialized Content: Share short stories or prequel content on platforms like Wattpad."
            ]
        }
        self.strategy.append(additional_ideas)

    def add_additional_ideas_non_fiction(self):
        additional_ideas = {
            "title": "Additional Creative Ideas",
            "details": [
                "1. Interactive Website Features: Add interactive elements like quizzes, additional resources, and downloadable content.",
                "2. Webinars: Host webinars to discuss the book's content and its applications.",
                "3. Merchandise: Create and sell merchandise related to the book (e.g., T-shirts, bookmarks).",
                "4. Author Blog: Start a blog with behind-the-scenes content, industry insights, and personal stories.",
                "5. Themed Events: Host events or contests related to the book's themes or subject matter.",
                "6. Serialized Content: Share key insights or chapters on platforms like Medium."
            ]
        }
        self.strategy.append(additional_ideas)

    def display_strategy(self):
        strategy_text = ""
        for section in self.strategy:
            strategy_text += f"{section['title']}\n{'-' * len(section['title'])}\n"
            if isinstance(section['details'], list):
                for detail in section['details']:
                    strategy_text += detail + "\n"
            else:
                strategy_text += section['details'] + "\n"
            strategy_text += "\n"
        return strategy_text
class BookLaunchStrategy:
    def __init__(self, book_title, author_name, genre, target_audience, release_date, book_description, author_bio):
        self.book_title = book_title
        self.author_name = author_name
        self.genre = genre
        self.target_audience = target_audience
        self.release_date = release_date
        self.book_description = book_description
        self.author_bio = author_bio
        self.strategy = []

       
class BookLaunchStrategy:
    def __init__(self, book_title, author_name, genre, target_audience, release_date, book_description, author_bio):
        self.book_title = book_title
        self.author_name = author_name
        self.genre = genre
        self.target_audience = target_audience
        self.release_date = release_date
        self.book_description = book_description
        self.author_bio = author_bio
        self.strategy = []


    def create_strategy(self):
        self.add_overview()
        self.add_pre_launch()
        self.add_launch()
        self.add_post_launch()
        self.add_additional_ideas()

    def add_overview(self):
        overview = {
            "title": "Overview",
            "details": f"Book Title: {self.book_title}\n"
                       f"Author Name: {self.author_name}\n"
                       f"Genre: {self.genre}\n"
                       f"Target Audience: {self.target_audience}\n"
                       f"Release Date: {self.release_date}\n"
                       f"Book Description: {self.book_description}\n"
                       f"Author Bio: {self.author_bio}\n"
        }
        self.strategy.append(overview)

    def add_pre_launch(self):
        pre_launch = {
            "title": "Pre-Launch Strategy",
            "details": [
                "1. Cover Reveal: Share the cover on social media platforms, book blogs, and newsletters.",
                "2. Author Website: Ensure the author’s website is updated with a dedicated page for the new book.",
                "3. Email List Building: Create a sign-up form on the website for updates and exclusive content.",
                "4. Advanced Reader Copies (ARCs): Distribute ARCs to book bloggers, influencers, and reviewers.",
                "5. Social Media Teasers: Post snippets, key takeaways, or quotes from the book.",
                "6. Book Trailer: Create and share a book trailer on YouTube and social media platforms.",
                "7. Guest Blogging: Write guest posts for popular blogs in your book’s niche or genre.",
                "8. Collaborations: Partner with other authors or influencers for cross-promotions."
            ]
        }
        self.strategy.append(pre_launch)

    def add_launch(self):
        launch = {
            "title": "Launch Strategy",
            "details": [
                "1. Virtual Launch Party: Host a live event on platforms like Facebook, Instagram, or YouTube.",
                "2. Social Media Blitz: Schedule multiple posts across all social media platforms.",
                "3. Email Campaign: Send a launch announcement to the email list with purchase links.",
                "4. Book Giveaways: Organize giveaways on Goodreads, Instagram, or through the author’s newsletter.",
                "5. Press Release: Distribute a press release to relevant media outlets and book blogs.",
                "6. Paid Advertising: Utilize Facebook Ads, Instagram Ads, LinkedIn Ads, and Google Ads to reach a wider audience.",
                "7. Influencer Marketing: Collaborate with influencers to promote the book on their channels.",
                "8. Podcast Interviews: Seek opportunities for the author to be interviewed on podcasts related to the book's genre or topic."
            ]
        }
        self.strategy.append(launch)

    def add_post_launch(self):
        post_launch = {
            "title": "Post-Launch Strategy",
            "details": [
                "1. Book Signings: Arrange book signings at local bookstores, libraries, and literary events.",
                "2. Ongoing Social Media Engagement: Continue engaging with readers through posts, stories, and Q&A sessions.",
                "3. Book Clubs: Encourage book clubs to feature the book and offer to join their discussions.",
                "4. Speaking Engagements: Arrange speaking engagements at industry conferences, webinars, and community events.",
                "5. Continued Advertising: Maintain a consistent advertising presence on relevant platforms.",
                "6. Book Reviews: Encourage readers to leave reviews on Amazon, Goodreads, and other platforms."
            ]
        }
        self.strategy.append(post_launch)

    def add_additional_ideas(self):
        additional_ideas = {
            "title": "Additional Creative Ideas",
            "details": [
                "1. Interactive Website Features: Add interactive elements like quizzes, additional resources, and downloadable content.",
                "2. Webinars: Host webinars to discuss the book's content and its applications.",
                "3. Merchandise: Create and sell merchandise related to the book (e.g., T-shirts, bookmarks).",
                "4. Author Blog: Start a blog with behind-the-scenes content, industry insights, and personal stories.",
                "5. Themed Events: Host events or contests related to the book's themes or subject matter.",
                "6. Serialized Content: Share key insights or chapters on platforms like Medium or Wattpad."
            ]
        }
        self.strategy.append(additional_ideas)

    def display_strategy(self):
        strategy_text = ""
        for section in self.strategy:
            strategy_text += f"{section['title']}\n{'-' * len(section['title'])}\n"
            if isinstance(section['details'], list):
                for detail in section['details']:
                    strategy_text += detail + "\n"
            else:
                strategy_text += section['details'] + "\n"
            strategy_text += "\n"
        return strategy_text
class MediaPitchEmail:
    def __init__(self, recipient_name, recipient_email, book_title, author_name, release_date, book_description, unique_angle):
        self.recipient_name = recipient_name
        self.recipient_email = recipient_email
        self.book_title = book_title
        self.author_name = author_name
        self.release_date = release_date
        self.book_description = book_description
        self.unique_angle = unique_angle

    def generate_email(self):
        email = f"""
        Subject: Feature Story Idea: {self.book_title} by {self.author_name}

        Dear {self.recipient_name},

        I hope this email finds you well. My name is {self.author_name}, and I am the author of the upcoming book, "{self.book_title}", which is set to be released on {self.release_date}.

        "{self.book_title}" is a {self.book_description}. What makes this book particularly compelling is {self.unique_angle}. I believe your audience would find this story both engaging and thought-provoking.

        I am reaching out to see if you would be interested in featuring a story about my book. I am available for interviews and would be happy to provide additional information, review copies, or anything else you might need.

        Thank you for considering this opportunity. I look forward to the possibility of working together to bring "{self.book_title}" to your audience.

        Best regards,
        {self.author_name}
        [Author's Contact Information]
        [Author's Website]
        """
        return email
class OrganizationPitchEmail:
    def __init__(self, recipient_name, recipient_email, book_title, author_name, release_date, book_description, event_idea):
        self.recipient_name = recipient_name
        self.recipient_email = recipient_email
        self.book_title = book_title
        self.author_name = author_name
        self.release_date = release_date
        self.book_description = book_description
        self.event_idea = event_idea

    def generate_email(self):
        email = f"""
        Subject: Exciting Author Event Opportunity: {self.book_title} by {self.author_name}

        Dear {self.recipient_name},

        My name is {self.author_name}, and I am the author of the forthcoming book, "{self.book_title}", which is set to be released on {self.release_date}. I am writing to propose an exciting event opportunity for your organization.

        "{self.book_title}" is a {self.book_description}. To celebrate its release, I would love to collaborate with your organization to host an event such as {self.event_idea}. This event could include a book reading, Q&A session, and book signing.

        I believe this event would be a wonderful way to engage your community and promote a love for reading and literature. I am available to discuss this proposal further and coordinate any details necessary to make this event a success.

        Thank you for considering this opportunity. I look forward to the possibility of partnering with you to bring "{self.book_title}" to your community.

        Best regards,
        {self.author_name}
        [Author's Contact Information]
        [Author's Website]
        """
        return email
def collect_author_info():
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

def generate_pdf_report(author_info, marketing_strategy):
 def generate_pdf_report(author_info, marketing_strategy):
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

def export_to_ical():
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
def main():
    st.title("Book Marketing Campaign Planner")

    menu = ["Book Marketing Strategy", "Book Launch Strategy", "Promo and Marketing Pitch Email Generator"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Book Marketing Strategy":
        author_info = collect_author_info()
        book_description = st.text_area("Enter the book description:")
        author_bio = st.text_area("Enter the author bio:")
        is_non_fiction = st.checkbox("Is this a non-fiction book?")
        if st.button("Generate Marketing Strategy"):
            strategy = BookMarketingStrategy(
                book_title=author_info['title'],
                author_name=author_info['author_name'],
                genre=author_info['genre'],
                target_audience=author_info['audience'],
                release_date=author_info['release_date'],
                book_description=book_description,
                author_bio=author_bio
            )
            strategy.create_strategy(is_non_fiction=is_non_fiction)
            marketing_strategy = strategy.display_strategy()
            st.text_area("Generated Marketing Strategy:", marketing_strategy)
            st.session_state.marketing_strategy = marketing_strategy
            st.session_state.author_info = author_info

    elif choice == "Book Launch Strategy":
        author_info = collect_author_info()
        book_description = st.text_area("Enter the book description:")
        author_bio = st.text_area("Enter the author bio:")
        if st.button("Generate Book Launch Strategy"):
            strategy = BookLaunchStrategy(
                book_title=author_info['title'],
                author_name=author_info['author_name'],
                genre=author_info['genre'],
                target_audience=author_info['audience'],
                release_date=author_info['release_date'],
                book_description=book_description,
                author_bio=author_bio
            )
            strategy.create_strategy()
            book_launch_strategy = strategy.display_strategy()
            st.text_area("Generated Book Launch Strategy:", book_launch_strategy)
            st.session_state.book_launch_strategy = book_launch_strategy
            st.session_state.author_info = author_info

    elif choice == "Promo and Marketing Pitch Email Generator":
        st.text("Generate promotional and marketing pitch emails based on the type of recipient.")
        recipient_type = st.selectbox("Select Recipient Type", ["Influencer", "Media Company", "Book Club", "Local Library", "Elementary School", "College", "Organization"])
        author_info = collect_author_info()
        if st.button(f"Generate Pitch Email for {recipient_type}"):
            recipient_name = st.text_input("Enter the recipient name:")
            recipient_email = st.text_input("Enter the recipient email:")
            if recipient_type == "Organization":
                event_idea = st.text_area("Enter the event idea:")
                pitch_email = OrganizationPitchEmail(
                    recipient_name=recipient_name,
                    recipient_email=recipient_email,
                    book_title=author_info['title'],
                    author_name=author_info['author_name'],
                    release_date=author_info['release_date'],
                    book_description=author_info['goal'],
                    event_idea=event_idea
                ).generate_email()
            else:
                unique_angle = st.text_area("Enter the unique angle or hook:")
                pitch_email = MediaPitchEmail(
                    recipient_name=recipient_name,
                    recipient_email=recipient_email,
                    book_title=author_info['title'],
                    author_name=author_info['author_name'],
                    release_date=author_info['release_date'],
                    book_description=author_info['goal'],
                    unique_angle=unique_angle
                ).generate_email()
            
            if pitch_email:
                st.text_area(f"Generated Pitch Email for {recipient_type}:", pitch_email)

if __name__ == "__main__":
    main()
