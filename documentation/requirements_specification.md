# Requirements specification

## Purpose of the application
This application is meant for storing data from answered helpline contacts. The purpose of this application is to provide a backup-tool for collecting data in events in which the main data collection application is unusable. 

The applications used in the helpline activities are all cloud based. In the event that one or more cloud based services would be unreachable or unsable for some reason, a backup solution for storing contact information is needed. The purpose of this digital application is a to provide a structured offline-tool to make sure that enough information is stored so that the contacts can later be stored in the cloud services manually based on the temporarily stored information. The helpline contacts are answerred in a secured and at all times supervised call center facility. Multiple counsellors can use the same computer in the call center. 

## Application users
The application can be used in two different roles: as a counselor and as a supervisor. Counselors used the application to store helpline contacts in an offline mode and the supervisor uses the application to manage stored submissions.

## User Interface (UI) design
The initial plan is to have for user screens:
- A login screen
- A screen for creating a new counselor account
- A counselor view for submitting data
- A supervisor screen for reviewing and managing submitted data

![login screen](/documentation/images/req-spec-login.png)
![create account screen](/documentation/images/req-spec-create-account.png)
![counselor-submit-data-screen](/documentation/images/req-spec-submit-content.png)
![supervisor-review-and-manage-content-screen](/documentation/images/req-spec-supervisor-browse.png)


## Basic functionalities

**Before logging in**
- User can create an account with the role 'counselor'. 
- Account creation has validation (username must have atleast three characters, passwords have to match, name can not be empty)
- User can login into the system
- If login fails, user is notified

**After logging in (counselor)**
- User with role counselor can submit new data entries
- Form contains validation (some fields are mandatory, depending on the selections made)
- User can logout

**After logging in (supervisor)**
- User with role supervisor can review all data submissions
- User can mark processed submissions as done
- User can permanently delete all submissions marked as done
- User can logout

## Further development
In the future following features could be added:

**Supervisor can manage accounts**
- Supervisor can view all accounts
- Supervisor can delete accounts
- Supervisor can reset user passwords
- Supervisor can create new supervisor accounts

**Supervisor can submit data**
- Supervisor can access the data submission view and submit data

**View account**
- All users can view their account information
- All users can change their password

**Counselors can manage their own data submissions**
The idea is that since service disruptions in cloud based services are often short in duration, it might be beneficial if the counselor could also process submissions they themselves have made during their own shift, when possible. 
- Counselors can view their data submissions
- Counselors can mark data submissions as processed
- Counselors can delete submissions marked as processed
