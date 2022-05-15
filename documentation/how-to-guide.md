# How to use the application
Start by downloading the [latest release](https://github.com/heidi-holappa/ot-harjoitustyo/releases/tag/final-release) by choosing 'Source code' from the section Assets. 

## Configuration
You can configure the database filename in file .env. Default filename is database.db. 

## Installation and starting the application

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

## Testing

To run tests use the command
```
poetry run invoke test
```
To create an HTML report of tests branch coverage use the command
```
poetry run invoke coverage-report
```

## Application tutorial

This release is meant to provide a proof of concept for an application that can be used to temporarily store data on a local hard drive in case of events in which cloud services are temporarily unavailable. To test the concept you can create accounts in both available roles. The application also includes a view for creating dummy data to make testing the concept easier. 

### Main view

Once you have launched the application, you will be shown the main view. In here you can either log in or create a new account by either clicking the buttons or by using the File menu to navigate. 

![Main view](/documentation/images/how-to-main-view.png)

### Account creation view

Account creation has light validation. Account must have a username and a password. Password can not be an empty String and a username must have four characters. 

As you create an account, you also select whether it is an admin-account. Accounts with role 'admin' can use all the available functionalities. Accounts with the role 'counselor' can only login, logout and submit contact data. 


![Create account](/documentation/images/how-to-create-account.png)


### Login view

To login enter your chosen username and password. If login fails, you will receive a notification message. 

![Login view](/documentation/images/how-to-login-view.png)

### Submitting contact data
**Roles available to:** counselor, admin

To submit a new contact fill in the fields in the form. All submission must have atleast a channel and a type. If the contact type is other than counseling, form elements 'select gender', 'select age' and 'write summary of contact' will remain disabled as they will not be filled. 

![Contact submission view 1](/documentation/images/how-to-counselor-view.png)

If the contact type is a counseling contact, all available fields are also required to be filled. 

![Counseling contact](/documentation/images/how-to-counseling-contact.png)

A contact is submitted by pressing submit. If data validation fails, user is notified. If data submission succeeds user is also notified. 


### Managing data submissions
**Roles available to:** admin

As an administrator you can review and manage contact data submissions. 

![Manage data submissions](/documentation/images/how-to-admin-view.png)

By first selecting items from the table, you can inspect them in the text widget. You can also mark selected items ready for deletion by using the button 'Mark contact for deletion.'  

![Marked for deletion](/documentation/images/how-to-admin-mark-and-delete.png)

When you are ready to delete processed contacts, you can press the button 'delete selected.' A messagebox prompts to confirm data deletion. Press "Ok" to confirm deletion of selected data. 

![Delete selected](/documentation/images/how-to-admin-confirm-delete.png)

**Hint:** you can also mark contacts by first left-clicking a table item and then right-clicking the selected item. This makes processing contacts quicker. 

### Creating dummy data

For more easier testing experience functionalities to create dummy data are available. In this view you can either create dummy data or delete all data submissions. To create dummy data type in the number of contacts you would like to create. 

![Create dummy data](/documentation/images/how-to-create-dummy-data.png)

**Please note** that when you delete data, all data is deleted, not just dummy data! 

### Menu
The application has a Menu that makes navigating between views easier. You can also exit the app from the menu, and access this documentation from the Help-section. 
