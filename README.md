# PharMap


## Requirements:

- Python 3.6
- Python VirtualEnv Wrapper
- PostgreSQL 9.6


## Setup

1. Create the virtualenv and install the requirements.
    ```
    mkvirtualenv pharmap
    pip install -r requirements-devel.txt
    ```
2. Create the database
    ```
    createdb pharmap
    apistar create_tables
    apistar sample_data  # Optional: To populate the db with sample data
    ```
3. Run the Api
    ```
    apistar run
    ```

