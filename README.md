# Data Docs

Generate a data dictionary for your Excel file.

![AI Agent create data dictionary](img/Ai_Agent_Data_Docs_wide.jpeg)

## Index

1. [Overview](#overview)
2. [Try the Web App](#try-the-web-app)
3. [Features](#features)
4. [Requirements](#requirements)
5. [Code Structure](#code-structure)
6. [Installation](#installation)
7. [Usage](#usage)
8. [License](#license)
9. [Demonstration](#demonstration)
10. [Known Issues](#known-issues)
11. [Acknowledgments](#acknowledgments)
12. [About Me](#about-me)

## Overview

This project uses an AI agent to read an Excel file, determine the data types and descriptions of each column, and generate a data dictionary. The data dictionary is then added as comments to the header of the Excel file.

## Try the Web App

Try the Web Application || [Access Streamlit Here!](https://excel-datadocs.streamlit.app/)

## Features

1. Converts Excel file to CSV
2. Generates data dictionary with column information (data type, description, etc.)
3. Adds data dictionary as comments to Excel file header
4. Saves output file with comments

## Requirements

Python 3.11<br>
Gemini API Key: [Get one here](https://ai.google.dev/gemini-api/docs/api-key)

* `Streamlit`
* `OpenPyXL`
* `Pandas`
* `AGNO`

## Code Structure

### Tools for the AI Agent

* `convert_to_csv`: Converts Excel file to CSV
* `add_comments_to_header`: Adds data dictionary as comments to Excel file header
* `create_agent`: Creates the AI agent with Gemini model
* `main`: Runs the agent and generates data dictionary

## Installation

To run this project, you can use the [Streamlit App](https://excel-datadocs.streamlit.app/) or run it locally in your machine.
To run it in your machine, follow these steps.

### Step 1: Clone the Repository

```bash
git clone https://github.com/gurezende/Data-Dictionary-GenAI.git
```

### Step 2: Navigate to the Project Directory

```bash
cd data-docs
```

### Step 3: Install the Required Libraries

```bash
pip install streamlit openpyxl pandas agno mcp google-genai
```

### Step 4: Run the Application

```bash
streamlit run data_docs.py
```

This will start the Streamlit server, and you can access the application in your web browser at http://localhost:8501.

## Usage

1. Enter your Gemini API key on the sidebar
2. Select the Excel file to be modified on the sidebar.
3. Run the AI agent.
4. The agent will generate a data dictionary and add it as comments to the header of the Excel file.
5. It will save the `output.xlsx` file and display a `Download` button to save the output locally.

## Demonstration

![Demonstration](img/data-docs-agent.gif)

## License

This project is licensed under the MIT License.

## Known Issues

* This Agent is configured to deal with Excel files containing a single Sheet. Files with multiple sheets may experience errors or unexpected behavior.
* LLMs are sometimes unpredictable. Some runs may not produce the expected result of saving the `output.xlsx`. As a possible solution, if you are running the agent in your machine, try stopping the app (`Ctrl+C` on your Terminal) and re-running it, as it may solve the problem. If you are running it online, reset the app and try again.

## Acknowledgments

AGNO library for providing the AI agent functionality.<br>
Streamlit for providing an easy-to-use interface for the project.

## About Me

This project was created by **Gustavo R Santos**.<br>
More about my work in my website: https://gustavorsantos.me