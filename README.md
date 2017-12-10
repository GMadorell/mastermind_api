

# Mastermind API
This project provides functionality for creating a mastermind game and working with it.


# Setup
## Development environment
- Create the database server: `$ docker docker-compose up -d`
- Setup a virtual environment with the given `dependencies.pip` file.
- Create the database tables located in `./database`.
    - *TODO: create a script that does this automatically.*
- Locate the configuration file using an environment variable
    - `$ export MASTERMIND_CONFIG="path/to/configuration.conf"`
    - There is a sample configuration file for testing in `./configuration/configuration.conf`
- Run tests: `$ nosetests`
