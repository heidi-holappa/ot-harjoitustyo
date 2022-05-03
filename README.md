# Back-up data-submission application
University course task - Spring 2022

This application is created for storing data from answered helpline contacts. The purpose of this application is to provide a backup-tool for collecting data in events in which the main data collection application is unusable. 

## Latest release

[Latest release: week 6](https://github.com/heidi-holappa/ot-harjoitustyo/releases/tag/viikko6)

## Documentation

* [Requirements specification](documentation/requirements_specification.md)
* [Application architecture](documentation/architecture.md)
* [User manual](documentation/how-to-guide.md)
* [Changelog](documentation/changelog.md)
* [Working hours record](documentation/working-hours-record.md)


## Installation
1. Install dependencies with the command 
```
poetry install
```
2. Initialize the application database with
```
poetry run invoke build
```
3. Run the project with the command
```
poetry run invoke start
```

## Usable command promtp commands
The following commands are usable:
1. Initialize the application with
```
poetry run invoke build
```
2. Run the application with
```
poetry run invoke start
```
3. Run tests with
```
poetry run invoke test
```
4. Create an HTML report of tests with coverage with
```
poetry run invoke coverage-report
```
You can locate the generated file in the folder htmlcov

5. Run pylint with 
```
poetry run invoke lint
```
6. Run autopep8 with
```
poetry run invoke format
```

7. Create dummy data for easier testing
```
poetry run invoke create-dummy-data
```
