## Environment variables
There are specific files used to provide environment variables to each service in the compose file. These files should be in the root level of the project.

### Database
The `.db.env` file provides the variables below to the database:
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB

### API
The `.dev.env` file provides the variables below to the API:
- POSTGRES_HOST
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
- POSTGRES_PORT

`POSTGRES_HOST` may refer to the hostname property in the service on the compose file.