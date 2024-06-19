# AdvizorPro_Person README

## Project Overview

This project aims to build a system that analyzes data using Retrieval-Augmented Generation (RAG) based Large Language Models (LLMs). The data is initially provided in a CSV file named `AdvizorPro_Person_04.24.2024-1.csv`. The system will integrate and merge data from various sources, store it in a database, and create a chatbot capable of answering queries based on this data.

## Folder Structure

|-- README.md
|-- app.py
|-- core
|   |-- core
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- asgi.py
|   |   |-- management
|   |   |   `-- commands
|   |   |       |-- AdvizorPro_Person_04.24.2024-1.xlsx
|   |   |       |-- data_dump_to_json.py
|   |   |       |-- load_brokers_from_file.py
|   |   |       |`-- load_brokers_linkedin_data.py
|   |   |-- migrations
|   |   |   |-- 0001_initial.py
|   |   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   `-- wsgi.py
|   |-- data_1.json
|   |-- data_2.json
|   |-- data_3.json
|   |-- data_4.json
|   |-- db.sqlite3
|   |`-- manage.py
|-- create_assistant.py
`-- requirements.txt

## Setup and Installation

1. __Clone the Repository__

    ```bash
    git clone https://github.com/HarshShahCitrusbug/AdvizorPro_Person.git
    cd AdvizorPro_Person
    ```

2. __Set Up Virtual Environment__

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. __Install Dependencies__

    ```bash
    pip install -r requirements.txt
    ```

4. __Set Up Database__
    - Configure your database settings in `settings.py`
    - Apply migrations:

      ```bash
      python manage.py migrate
      ```

## Data Ingestion and Processing

1. __Load Broker Data from CSV__

    ```bash
    python manage.py load_brokers_from_file
    ```

    This command reads the `AdvizorPro_Person_04.24.2024-1.csv` file and loads the broker data into the database.

2. __Load LinkedIn Data__

    ```bash
    python manage.py load_brokers_linkedin_data
    ```

    This command fetches LinkedIn data using the LinkedIn column from the CSV file and merges it with the existing broker data.

3. __Dump Data to JSON__

    ```bash
    python manage.py data_dump_to_json
    ```

    This command creates four different JSON files, each containing unique data.

## Assistant Creation

1. __Create Assistant__

    ```bash
    python create_assistant.py
    ```

    This script reads the JSON files and uses an LLM to create an assistant capable of answering questions about the data.

## Running the Streamlit App

1. __Start Streamlit App__

    ```bash
    streamlit run app.py
    ```

    This command starts the Streamlit app, providing a user-friendly interface for interacting with the assistant and receiving streaming responses.

## Features

- __Data Integration__: Merges data from `AdvizorPro_Person_04.24.2024-1.csv`, BrokerCheck (<https://brokercheck.finra.org/>), and LinkedIn (<https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api>).
- __Database Storage__: Supports various data infrastructures like PostgreSQL, BigQuery, etc.
- __ETL Process__: Uses SQL and custom ETL processes for data transformation and loading.
- __Chatbot Assistant__: Utilizes RAG-based LLMs (ChatGPT) to answer user queries based on the integrated data.
- __Streamlit Interface__: Provides a streaming response for a better user experience.

## Query Examples

- "What information do you have on John Doe?"
- "Show me the details for CRD number 123456."
- "What is the LinkedIn profile for Jane Smith?"

## Conclusion

This project provides a comprehensive solution for analyzing and interacting with integrated data using advanced AI technologies. Follow the setup instructions to get started and leverage the powerful features offered by the system.
