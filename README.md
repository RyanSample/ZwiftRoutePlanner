# Zwift Route Planner

A web application built to allow a user to keep track of what routes they have completed without needing to launch zwift.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See Installation for information on installing the program.

### Prerequisites
Please see [requirements.txt](requirements.txt) for a full listing of the packages required to run this application

To install the dependencies required to run this program, navigate to the project's root directory and simply type:

```
pip install -r requirements.txt 
```

This will install `pygame==1.9.6` and its dependencies.

### Installation

*TBD*

## Running the program

To run the program type 
```
py manage.py runserver
```

This will start the server and you will be able to test out the application.

## Running the tests

Run tests by navigating to their directory and running the following command:

```
py -m unittest
```

## Loading and Unloading the database

To dump the route and world data run the following command

```
py manage.py dumpdata routeplanner.World routeplanner.Route > data.json
```

This will write all of the data in the route and world models into the data.json file.

Conversely we can load data by typing
```
py manage.py loaddata data.json
```

This will open the file and load the fixtures into the database.

**WARNING** if you are running into unicode issues similar to the following
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```
Then you will need to open the .JSON file in a text editor and resave it with UTF-8 encoding. 

## Built With

* [Django](https://www.djangoproject.com/) 

## Authors

* **Ryan Sample** - [RyanSample](https://github.com/RyanSample)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments