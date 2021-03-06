# Requirements specification

## Purpose of the application
This application is meant for storing data from answered helpline contacts. The purpose of this application is to provide a backup-tool for collecting data in events in which the cloud based main data collection application is unusable. 

The applications used in the helpline activities are all cloud based. In the event that one or more cloud based services would be unreachable or unsable for some reason, a backup solution for storing contact information is needed. The purpose of this digital application is a to provide a structured offline-tool to make sure that enough information is stored so that the contacts can later be stored in the cloud services manually based on the temporarily stored information. The helpline contacts are answerred in a secured and at all times supervised call center facility. Multiple counsellors can use the same computer in the call center. 

As this is a proof-of-concept type of execution, the application has some features that an application built for production would not have. 

## Application users
The application can be used in two different roles: as a counselor and as a supervisor. Counselors used the application to store helpline contacts in an offline mode and the supervisor uses the application to manage stored submissions. In this proof-of-concept version users can create user accounts in chosen roles. In production version a different type of account management would be required. 

## User Interface (UI) design
The application has the following views:
- A main view that is shown when user logs in. 
- A login view
- A view for creating a new account
- A counselor view for submitting data
- A supervisor view for reviewing and managing submitted data
- A supervisor view for creating dummy data. 

Each view can be seen in the [how to -guide of the application](how-to-guide.md)

## Basic functionalities

**Main view**
- User can either log in or create a new account
- User can exit the application from menu

**Create account view**
- User can create an account with the role 'counselor' or with the role 'admin'. 
- Account creation has validation. Username must have four charcters. Passwords have to match and have atleast six characters. 

**Login view**
- User can login into the system with a username and a password.
- Login is authenticated. If login fails, user is notified

**After logging in (role counselor)**
- Role counselor can submit new data entries
- Form contains validation (for counseling contacts all fields are mandatory)
- User can logout
- User can view how to - documentation via menu. 
- User can exit the app via menu

**After logging in (role admin)**
- Role admin can access all available views either via navigation buttons or through menu. 
- In all the following views role admin can logout or exit the app via menu.
- In all the following views role admin can view how to - documentation via menu. 

**Contact management view**
- Role admin can review all data submissions.
- User can mark processed submissions as done.
- User can permanently delete all submissions marked as done.

**Contact submission view**
- User with role admin can submit contacts
- The view is the same as the view role counselor uses to submit data. 
- Users with role admin have additional features in data submission view (for navigation)
- User can create dummy data for easier testing of the application

**Dummy data creation view**
- User with role admin can create from 1 to 100 dummy contact to populate the contact management treeview. 
- User with role admin can delete all contacts at once.


**General features**
- The application has a menubar in all views. Menu bar has different options for logged in user. Features depend on user role. 
- The application has a custom style. 

## Further development
In the future following features could be added (preliminary time-estimates included):

**Account management (role admin)**
- Details:
  - Admin can view all accounts
  - Admin can delete accounts
  - Admin can reset user passwords
  - Admin can create new supervisor accounts
- Time-estimate: 1-2 work days (8-16)
- Note: could be done together with the next item (view and edit account details). Same estimate would apply to these both were built at the same time. 

**View and edit account details (all users)**
- Details:
  - All users can view their account information
  - All users can change their password
- Time-estimate: 1-2 work days (8-16 hours)
- Note: could be done together with the previous item (account management). Same estimate would apply if these both were built at the same time. 

**Counselors can manage their own data submissions**
- Details: Since service disruptions in cloud based services are often short in duration, it might be beneficial if the counselor could also process submissions they themselves have made during their own shift, when possible. 
  - Counselors can view their data submissions
  - Counselors can mark data submissions as processed
  - Counselors can delete submissions marked as processed
- Time-estimate: 4-6 hours
- Note: Methods for fetching data submissions from selected user exist in repository and service classes. These were consciously left to save time on further development. 

**Dark mode**
- Details: Creating a custom theme made it possible to offer users alternate themes in the future. With further development new themes could be added. An initial version of dark mode already exists in the guiTheme -class, but the style needs futher work and the code also needs some re-factoring. 
- Time-estimate: 4-6 hours. 
- Note: Initial dark mode theme exists in class SetTheme. It was consciously left to save time on further development.