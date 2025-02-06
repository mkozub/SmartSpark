
import openai
import os
import smartsheet
import json

# Secure API key handling
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ask the user for the type of project and Sheet ID
use_case = input("Enter the type of project you want to run: ")
sheet_id = input("\nEnter Sheet ID: ")

# OpenAI API call
model_engine = "gpt-3.5-turbo"
prompt = f"Generate a detailed, task-by-task plan to run a {use_case} project. Think hard to ensure the tasks cover all key tasks of a {use_case} project from initiation to completion. Also estimate the duration of each task in days. Just give me the number of days, no need to label the number. Return only the tasks and duration in a strict JSON structured. no other text. Here is the JSON structure you must follow: {{\"tasks\": [{{\"task\": \"Task Name\", \"duration\": \"Duration\"}}]}}"

print("\n\n")
print("Prompt:", prompt)
print("\n\n")

response = client.chat.completions.create(
    model=model_engine,
    messages=[{"role": "user", "content": prompt}],
    max_tokens=500,
    temperature=0.7
)

generated_json = response.choices[0].message.content.strip()
print("Generated JSON:", generated_json)
print("\n\n")

# Load data from generated JSON
try:
    load = json.loads(generated_json)
except json.JSONDecodeError:
    print("Error: Invalid JSON received from OpenAI.")
    exit(1)

smartsheet_api_key = os.getenv("SMARTSHEET_API_KEY")

client = smartsheet.Smartsheet(smartsheet_api_key)

# Get the sheet and column objects
sheet = client.Sheets.get_sheet(sheet_id)
columns = sheet.columns
column_id_task = columns[0].id  # First column for task
column_id_duration = columns[1].id  # Second column for duration

# Add rows based on JSON data
to_add = []
for item in load.get("tasks", []):  # Assuming OpenAI returns a list of tasks
    new_row = smartsheet.models.Row()
    new_row.to_top = True

    # Task cell
    task_cell = smartsheet.models.Cell()
    task_cell.column_id = column_id_task
    task_cell.value = item.get("task")

    # Duration cell (extract number from duration)
    duration_cell = smartsheet.models.Cell()
    duration_cell.column_id = column_id_duration
    duration = item.get("duration", "")
    duration_number = ''.join(filter(str.isdigit, duration))  # Extract numeric part
    duration_cell.value = duration_number if duration_number else duration  # Fallback if no number

    # Add cells to row
    new_row.cells.append(task_cell)
    new_row.cells.append(duration_cell)

    to_add.append(new_row)

if to_add:
    client.Sheets.add_rows(sheet_id, to_add)
    print("Rows added to Smartsheet successfully.")
else:
    print("No valid data to add.")
