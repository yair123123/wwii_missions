# Project Overview

In this project, we take a Big Data table that is denormalized and organize it into normalized tables. The project uses the following technologies:

- **SQLAlchemy**
- **Flask**
- **Toolz**

The project is written in **Python** and **SQL**.

## Requirements

- **PostgreSQL** must be installed.
- A database named `wwii_missions` should be created.

## Installation and Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yair123123/wwii_missions.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure PostgreSQL is running and the database `wwii_missions` is created.

4. Run the project:
    ```bash
    python main.py
    ```

    **Note**: The initial run may take some time, so please be patient.

## Endpoints

- `/Mission`: Retrieves all the missions after normalization.
- `/Mission/id`: Fetches a specific mission based on its `id`.

## Database

This project connects to a PostgreSQL database named `wwii_missions`.
