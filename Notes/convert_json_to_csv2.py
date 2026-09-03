import pandas as pd
import json

# Step 1: Define file paths
json_file_path = 'NewGhost2.json'  # Replace with your actual JSON file path
csv_file_path = 'NewGhost3.csv'    # Path for the output CSV file

# Step 2: Load the JSON file
# Open and read JSON data into a Python object
with open(json_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Step 3: Parse JSON data into a list of dictionaries
# Extract relevant fields from JSON, including comments
issues_list = []

for issue in json_data:
    # Extract comments if available
    comments = issue.get('comments', [])
    comment_texts = [
        f"{comment.get('author', {}).get('login', 'N/A')} ({comment.get('createdAt', 'N/A')}): {comment.get('body', 'N/A')}"
        for comment in comments
    ]
    combined_comments = " | ".join(comment_texts)  # Combine all comments into a single string

    # Append issue details to the list
    issues_list.append({
        'ID': issue.get('id'),  # Issue ID
        'Title': issue.get('title'),  # Title of the issue
        'State': issue.get('state'),  # Current state (e.g., open/closed)
        'State Reason': issue.get('stateReason', 'N/A'),  # State reason if available
        'Number': issue.get('number'),  # Issue number
        'Created At': issue.get('createdAt'),  # Date and time of creation
        'Updated At': issue.get('updatedAt'),  # Last updated timestamp
        'Closed At': issue.get('closedAt', 'N/A'),  # Closed timestamp (optional)
        'URL': issue.get('url'),  # Issue URL link
        'Author': issue.get('author', {}).get('login', 'N/A'),  # Issue author's login
        'Labels': ", ".join([label.get('name', '') for label in issue.get('labels', [])]),  # Issue labels
        'Assignees': ", ".join([assignee.get('login', '') for assignee in issue.get('assignees', [])]),  # Assignee list
        'Comments': combined_comments  # Extracted comments as a single string
    })

# Step 4: Convert the parsed data into a pandas DataFrame
# DataFrame structure for easy export and manipulation
df = pd.DataFrame(issues_list)

# Step 5: Save the DataFrame as a CSV file
# Export the DataFrame to a CSV file without the index
df.to_csv(csv_file_path, index=False, encoding='utf-8')

# Step 6: Print completion message
print(f"CSV file successfully created at: {csv_file_path}")
