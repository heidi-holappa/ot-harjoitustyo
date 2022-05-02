# How to use the application

This release is meant to provide a proof of concept for an application that can be used to temporarily store data on a local hard drive in case of events in which cloud services are temporarily unavailable. To test the concept you can create accounts in both available roles. The application also includes a view for creating dummy data to make testing the concept easier. 

## Account creation and logginging in

Once you have launched the application, you can either create an account or login with an existing account. Account creation has light validation. Account must have a username and a password. As you create an account, you also select whether it is an admin-account. Accounts with role 'admin' can use all the available functionalities. Accounts with the role 'counselor' can only login, logout and submit contact data. 

## Submitting contact data
**Roles available to:** counselor, admin

All submission must have atleast a channel and a type. If the contact type is a counseling contact, additional information is also required. 

## Managing data submissions
**Roles available to:** admin

As an administrator you can review and manage contact data submissions. By first selecting items from the table, you can then mark them ready for deletion by using the button 'Mark contact for deletion.'  When you are ready to delete processed contacts, you can press the button 'delete selected.'

**Hint:** you can also mark contacts by first left-clicking a table item and then right-clicking the selected item. This makes processing contacts quicker. 

## Creating dummy data

For more easier testing experience functionalities to create dummy data are available. In this view you can either create dummy data or delete all data submissions. Please note that when you delete data, all data is deleted, not just dummy data! 

## Menu
The application has a Menu that makes navigating between views easier. You can also exit the app from the menu, and access this document. 

