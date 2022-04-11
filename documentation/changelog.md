# Changelog

## Week 3
* An initial version of following features created:
  - user can create an account with role counselor
  - account creation has validation (passwords match, username not already taken)
  - account information is stored (unsecurely) in a csv-file
  - user can login with created account
  - user can submit contact data
  - contact data is stored into a csv-file
* Created first tests:
  - method CounselorSubmit().clear_data() resets dictionary storing contact data
  - login is successful with a test user account
* Create following Invoke-tasks
  - start: runs the application
  - test: runs tests with pytest
  - coverage-report: creates an html-version of tests with coverage

## Week 4
* An initial version of GUI has been added. GUI now includes
  - main view
  - login view
  - account creation view
  - user role 'counselor' view for data submission
* User can move between GUI views and can logout
* Data is now stored in SQLite-database
  - database has two tables: users, contacts
  - user- and contactdata can be stored into the database
* Application re-structured. The structure now includes
  - Entities: user and contact objects
  - Service classes for user and contact management
  - repository classes for database queries
  - gui-classes to create different GUI-views

