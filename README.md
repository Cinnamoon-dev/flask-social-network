## Flask API
Using flask to create a minimal application of an API and SQLAlchemy as ORM for a SQLite database. 

</br>

### Essential Configuration
#### Database IP Address
To make the communication between the containers (database and API) work you'll have to get local docker ip address.
> sudo ip addr show docker0 </br>

And then put it inside the HOST constant in the config.py file before the build of the container image.
> HOST = "local.docker.ip.address" </br>

After this you can start the containerized application.

</br>

### Database Configuration
#### Table Generation
> flask db init</br>
> flask db migrate</br>
> flask db upgrade</br>

### Running the Application
> python3 run.py </br>

### Creating and using the virtual environment
The python dependency management tool used is [poetry](https://python-poetry.org/). If you never used it you might want to enable the virtual environment inside the project folder.
> poetry config virtualenvs.in-project true </br>

</br>

Then you can just install the depedencies and enable the virtual environment.
> poetry install </br>
> poetry shell </br>

</br>