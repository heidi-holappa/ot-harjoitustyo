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
* Application re-structured. The structure now includes packages
  - Entities: user and contact objects
  - Services: classes for user and contact management
  - Repositories: classes for database queries
  - UI: classes to create different GUI-views
* Application has new tests, testing uses test-database. Tests include:
  - creating objects from package Entities classes User and Contact
  - testing methods from classes in Service package
  - testing method from classes in the Repositories package (through Service package)

## Week 5
* Code refactored. GUI-classes no longer use Entities-classes directly
* Added external library Werkzeug for password hashing. Passwords are now hashed
* Added date and time to contact data submission
* Application now has an admin view
* As a bonus admins can also submit contact data
* Admin view layout restructured and polished
* Contact data can now be browsed
* Contact data can be marked to be deleted
* Contact data can be deleted
* User can create dummy data. Added external library for creating lorem ipsum
* New poetry command for creating dummy data. Dummy data can also be created in GUI in admin-mode

## Week 6
* GUI-classes now take advantage of ttk.style(). GUI has a custom style. 
* Account creation now has validation. 
* A messagebox added to confirm marked data deletion
* Counselor view layout restructured
* Improved counselor view usability. Datafields are enabled only if they are to be filled.
* Application now has a working menu
* Application now has a how-to-guide that can be accessed through the menu in the application. 


## Week 7 - Final week
* Code refactored for easier future maintenance. More detailed docstring added.
* Account creation validation improved.
* Dummy data creation validation improved. Error notifications added. 
* A confirmation messagebox added before deleting all data. 
* Menu refactored into it's own class
* Enums introduced
