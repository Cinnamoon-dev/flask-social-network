## Flask API
Using flask to create a minimal application of an API and SQLAlchemy as ORM for a SQLite database. 

### Creating and using the virtual environment
The python dependency management tool used is [poetry](https://python-poetry.org/). If you never used it you might want to enable the virtual environment inside the project folder.
> poetry config virtualenvs.in-project true </br>

</br>

Then you can just install the depedencies and enable the virtual environment.
> poetry install </br>
> poetry shell </br>

### Database Configuration
#### Table Generation
> flask db init</br>
> flask db migrate</br>
> flask db upgrade</br>

### Running the Application
> python3 run.py </br>

### Running the Dockerized Application
You can just skip the steps above and test the application using docker compose.
> docker compose up </br>