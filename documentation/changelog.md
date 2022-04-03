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

