# Architecture

## Structure
The structure of the application follows the layered architecture framework. At the current initial stage the structure has open issues that will be fixed in the future. For instance in the next phase the goal is to disconnet UI from the Entities-package. 

```mermaid
    stateDiagram
    state Repositories {
        UserRepository
        ContactDataRepository
    }
    state Service {
        UserManagement
        ContactManagement
    }
    state UI {
        GUI_classes
    }
    state Entities {
        User
        Contact
    }

    UI --> Service
    Service --> Repositories
    Service --> Entities
    UI --> Entities: this will be refactored
    Repositories --> Entities
```
The package UI includes the classes responsible for the objects that create the graphical user interface and it's functionalities. The package Service works as a hub controlling the logic of the application. 

Package Entities contains the objects that contain the different data structures used by the application. The package Repositories handles the database queries (retrieving and storing data).

## Class diagram

Below is a visualization of the current class diagram and dependencies. The vision is to make refactor the code in week 5 to make the dependencies more structured. Feedback and tips on how to work towards this are very welcome!

At the time being the application uses one object instance of the classes in UI, service and repository classes. UI-classes 'remember' the service classes they use and the service classes 'remember' the repositories used. None of the GUI, service or repository classes 'remember' objects from the entities classes, even if many of them use them temporarily. 


```mermaid
    classDiagram
        class UI_classes
        class UserManagement
        class ContactManagement
        class User
        class Contact
        class ContactDataRepository
        class UserRepository
        
        
        UI_classes "1" -- "1" ContactManagement
        UI_classes "1" -- "1" UserManagement
        ContactManagement "1" -- "1" ContactDataRepository
        UserManagement "1" -- "1" UserRepository
        ContactManagement "1" .. "*" Contact
        ContactManagement "1" .. "*" User
        ContactManagement "1" -- "1" UserManagement
        UserManagement "1" .. "*" User
        UserRepository "1" .. "*" User
        ContactDataRepository "1" .. "*" Contact
        ContactDataRepository "1" .. "*" User

```

## Main functionalities

We will next showcase the application logic through examples of few main functionalities.

### Login
When user enters the main view and sets to log in, the following chain of events is carried out:

```mermaid
sequenceDiagram
actor user
participant UI
participant UserManagement
participant UserRepository
participant User
user ->> UI: clicks Login-button
UI ->> UI: changes to login view
user ->> UI: inputs credentials, presses submit
UI ->> UserManagement: create_active_user
UserManagement ->> User: User(username, password)
User -->> UserManagement: self._active_user
UI ->> UserManagement: login()
UserManagement ->> UserRepository: get_user_data
UserRepository -->> UserManagement: user_data
UserManagement ->> UserManagement: validate login
UserManagement ->> UI: return boolean + message
UI ->> UI: show appropriate view or fail notification
```

### Submit contact data
When user fills the data submission form and submits new data, the following chain of actions is carried out:

```mermaid
sequenceDiagram
actor user
participant UI
participant ContactManagement
participant UserManagement
participant ContactRepository
participant Contact
user ->> UI: fills form, clicks submit
UI ->> ContactManagement: manage_contact_submission()
ContactManagement ->> Contact: contact(arguments)
Contact -->> ContactManagement: contact
ContactManagement ->> Contact: contact.is_valid()
Contact -->> ContactManagement: boolean
ContactManagement ->> ContactManagement: submit_contact()
ContactManagement ->> UserManagement: get_active_user()
ContactManagement ->> ContactRepository: add_contact(username, contact)
ContactManagement -->> UI: status (boolean) + message
UI ->> UI: Check if success, show appropriate notification
```