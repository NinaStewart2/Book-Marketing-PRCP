import pandas as pd
from datetime import datetime

# Initialize an empty DataFrame to store PR activities
columns = ['Activity', 'Date', 'Details']
pr_activities = pd.DataFrame(columns=columns)

# Load existing data if available (for demonstration, we're starting fresh)
try:
    pr_activities = pd.read_csv('pr_campaign.csv')
except FileNotFoundError:
    pass

def add_activity(activity, date, details):
    global pr_activities
    new_activity = {'Activity': activity, 'Date': date, 'Details': details}
    pr_activities =pr_activities.append(new_activity, ignore_index=True)
    pr_activities.to_csv('pr_campaign.csv', index=False)
    print(f"Activity '{activity}' on {date} added successfully!")

def view_activities():
    global pr_activities
    if pr_activities.empty:
        print("No activities planned.")
    else:
        print(pr_activities)

def edit_activity(index, activity=None, date=None, details=None):
    global pr_activities
    if index in pr_activities.index:
        if activity:
            pr_activities.at[index, 'Activity'] = activity
        if date:
            pr_activities.at[index, 'Date'] = date
        if details:
            pr_activities.at[index, 'Details'] = details
        pr_activities.to_csv('pr_campaign.csv', index=False)
        print(f"Activity at index {index} updated successfully!")
    else:
        print(f"No activity found at index {index}.")

def delete_activity(index):
    global pr_activities
    if index in pr_activities.index:
        pr_activities = pr_activities.drop(index)
        pr_activities.to_csv('pr_campaign.csv', index=False)
        print(f"Activity at index {index} deleted successfully!")
    else:
        print(f"No activity found at index {index}.")

# Example usage
add_activity('Press Release', '2023-05-20', 'Release to major book blogs')
add_activity('Book Signing', '2023-06-10', 'At local bookstore')
view_activities()
edit_activity(0, date='2023-05-21')
delete_activity(1)
view_activities()
