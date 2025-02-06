# SmartSpark-Final

## Overview

**SmartSpark-Final.py** is a Python script that integrates OpenAI's GPT-3.5 Turbo with Smartsheet to generate and populate a structured task list for a given project type. The script takes user input for the project type and Smartsheet Sheet ID, generates a detailed task breakdown using OpenAI, and then inserts the structured task data into a specified Smartsheet.

## Features

- **Generates project plans**: Uses OpenAI's GPT-3.5 Turbo to create a structured, JSON-formatted task list based on a user-specified project type.
- **Automated Smartsheet Integration**: Fetches a target Smartsheet and populates it with generated tasks and durations.
- **Secure API Key Handling**: Uses environment variables for OpenAI and Smartsheet API keys.
- **Error Handling**: Ensures proper JSON response formatting and prevents invalid data entry.

## Prerequisites

- Python 3.8+
- An OpenAI API Key (`OPENAI_API_KEY` stored in environment variables)
- A Smartsheet API Key (`SMARTSHEET_API_KEY` stored in environment variables)
- Required Python libraries:
  - `openai`
  - `smartsheet-python-sdk`
  - `json`
  - `os`

## Installation

1. **Clone the Repository** (or copy the script):

   ```sh
   git clone <repo-url>
   cd APItesting/2025
   ```

2. **Install Dependencies**:

   ```sh
   pip install openai smartsheet-python-sdk
   ```

3. **Set Environment Variables** (Recommended):

   ```sh
   export OPENAI_API_KEY="your_openai_api_key"
   export SMARTSHEET_API_KEY="your_smartsheet_api_key"
   ```

## Usage

1. **Run the script**:

   ```sh
   python SmartSpark-Final.py
   ```

2. **Provide Input**:
   - Enter the project type when prompted.
   - Enter the Smartsheet Sheet ID where tasks should be added.

3. **Output**:
   - The script will generate a structured task plan in JSON format.
   - It will then add the tasks and their durations to the specified Smartsheet.

## JSON Structure Example

The script generates tasks in the following JSON format:

```json
{
  "tasks": [
    {
      "task": "Define project scope",
      "duration": "5"
    },
    {
      "task": "Develop project plan",
      "duration": "10"
    }
  ]
}
```

## Error Handling

- **Invalid JSON Response**: If OpenAI's response is not in proper JSON format, the script exits with an error message.
- **Missing or Invalid Sheet ID**: Ensures that the Smartsheet API can retrieve the given sheet before attempting updates.
- **Non-Numeric Durations**: Extracts numeric values from OpenAI's duration estimates.

## Future Improvements

- **Enhance task generation prompts**: Refine OpenAI prompt for better accuracy and additional metadata.
- **Flexible Column Mapping**: Allow dynamic column selection for Smartsheet integration.
- **Support for Additional AI Models**: Extend compatibility with other OpenAI models.

## License

MIT License (or specify if different).

## Author

Mike Kozub
