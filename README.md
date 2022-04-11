# Back-up data-submission application
University course task - Spring 2022

This application is created for storing data from answered helpline contacts. The purpose of this application is to provide a backup-tool for collecting data in events in which the main data collection application is unusable. 

## Documentation

* [Requirements specification](documentation/requirements_specification.md)
* [Application architecture](documentation/architecture.md)
* [Changelog](documentation/changelog.md)
* [Working hours record](documentation/working-hours-record.md)


## Installation
1. Install dependencies with the command 
```
poetry install
```

2. Run the project with the command
```
poetry run invoke start
```

## Usable command promtp commands
The following commands are usable:
1. Run the application with
```
poetry run invoke start
```
2. Run tests with
```
poetry run invoke test
```
3. Create an HTML report of tests with coverage with
```
poetry run invoke coverage-report
```
You can locate the generated file in the folder htmlcov

4. Run pylint with 
```
poetry run invoke lint
```
5. Run autopep8 with
```
poetry run invoke format
```