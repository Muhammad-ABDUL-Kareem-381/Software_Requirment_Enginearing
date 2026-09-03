import pandas as pd
import json

# Step 1: Load the JSON file
json_file_path = 'Ghost2.json'  # Replace with your actual file path
csv_file_path = 'Ghost5.csv'

# Step 2: Open and load the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Step 3: Convert JSON data into a list of dictionaries
# Ensure the data is iterable
issues_list = []

for issue in json_data:
    issues_list.append({
        'ID': issue.get('id'),
        'Title': issue.get('title'),
        'State': issue.get('state'),
        'Number': issue.get('number'),
        'Created At': issue.get('createdAt'),
        'Updated At': issue.get('updatedAt'),
        'Closed At': issue.get('closedAt'),
        'URL': issue.get('url'),
        'Author': issue.get('author', {}).get('login'),
        'Labels': ", ".join([label.get('name') for label in issue.get('labels', [])]),
        'Assignees': ", ".join([assignee.get('login') for assignee in issue.get('assignees', [])])
    })

# Step 4: Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(issues_list)

# Step 5: Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False, encoding='utf-8')

print(f"CSV file successfully created at: {csv_file_path}")
