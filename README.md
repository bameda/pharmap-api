# PharMap


## Requirements:

- Python 3.6
- Python VirtualEnv Wrapper
- PostgreSQL 9.6
- PostGIS 2.3 (you neded to create a db template 'template_postgis')


## Setup

1. Create the virtualenv and install the requirements.
    ```
    mkvirtualenv pharmap
    pip install -r requirements-devel.txt
    ```
2. Create the database
    ```
    createdb -T template_postgis pharmap
    apistar create_tables
    ```
3. Run the Api
    ```
    apistar run
    ```

