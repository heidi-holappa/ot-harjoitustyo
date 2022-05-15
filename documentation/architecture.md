# Architecture

## Structure
The structure of the application follows the layered architecture framework.  

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
    Repositories --> Entities
```
* The package UI includes the classes used to create objects that construct the graphical user interface views and it's interactive functionalities. 
* The package Service works as a hub controlling the logic of the application. 
* Package Entities contains the objects that contain the different data structures used by the application. 
* The package Repositories handles the database queries (retrieving and storing data).

## Class diagram

Below is a visualization of the class diagram and dependencies. The application uses default object instances of service and repository classes. UI-classes 'remember' the instances of service classes they use and the service classes 'remember' the instances of repository class objects used. None of the GUI, service or repository classes 'remember' instances from the entities classes, even if many of them use them temporarily. Exception being the active user that is referenced in the service class UserManagement. 


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
UI ->> UI: main view is destroyed and login view constructed
user ->> UI: inputs credentials, presses submit
UI ->> UserManagement: login("heidi", "password123")
activate UserManagement
UserManagement ->> User: user = User("heidi", "password123")
UserManagement ->> UserManagement: self._set_active_user(user)
UserManagement ->> UserRepository: get_user("heidi")
UserRepository -->> UserManagement: user_found
UserManagement ->> User: password_hash_valid(hashed_password)
activate User
User -->> UserManagement: boolean
deactivate User
UserManagement ->> UserManagement: self._set_active_user(user_found)
UserManagement ->> UI: return (True, empty string)
deactivate UserManagement
UI ->> UI: show appropriate view or notify of validation error
```

### Submit contact data
When user fills the data submission form and submits new data, the following chain of actions is carried out in the case of valid submission:

```mermaid
sequenceDiagram
actor user
participant UI
participant ContactRepository
participant Contact
participant ContactManagement
participant UserManagement
user ->> UI: fills form, clicks submit
UI ->> ContactManagement: manage_new_contact_submission(channel, type, gender, age, content)
activate ContactManagement
ContactManagement ->> Contact: contact(args)
activate Contact
Contact -->> ContactManagement: contact
deactivate Contact
ContactManagement ->> Contact: contact.is_valid()
activate Contact
Contact -->> ContactManagement: True
deactivate Contact
ContactManagement ->> ContactManagement: submit_contact(contact)
ContactManagement ->> UserManagement: get_active_user()
UserManagement -->> ContactManagement: User object
ContactManagement ->> ContactRepository: add_contact(user.username, contact)
activate ContactRepository
ContactRepository -->> ContactManagement: (True, "")
deactivate ContactRepository
ContactManagement -->> UI: (True, "")
deactivate ContactManagement
UI ->> UI: Construct a messagebox notifying of success. 
```

Incase the validation fails (for instance a counseling contact is missing required data) the following sequence takes place:

```mermaid
sequenceDiagram
actor user
participant UI
participant ContactRepository
participant Contact
participant ContactManagement
participant UserManagement
user ->> UI: fills form, clicks submit
UI ->> ContactManagement: manage_new_contact_submission(channel, type, gender, age, content)
activate ContactManagement
ContactManagement ->> Contact: contact(args)
activate Contact
Contact -->> ContactManagement: contact
deactivate Contact
ContactManagement ->> Contact: contact.is_valid()
activate Contact
Contact -->> ContactManagement: False
deactivate Contact
ContactManagement -->> UI: (False, "Error message indicating what is wrong")
deactivate ContactManagement
UI ->> UI: Construct a messagebox with a error-message.
```

### Mark contact data for deletion
Users with role admin can preview data submission, mark them for deletion and delete marked submission. The next sequence diagram showcases the chain of events that is carried out when a user first marks an item for deletion and then deletes marked items. This sequence diagram has more internal logic of GUI object instance described to give an understanding on the logic GUI classes have been constructed with. 

```mermaid
sequenceDiagram
actor user
participant UI
participant ContactManagement
participant ContactRepository
user ->> UI: activates and object in treeview
user ->> UI: clicks button "mark for deletion"
UI ->> UI: event activates method _mark_contact_for_deletion(contact_id)
UI ->> ContactManagement: mark_contact_for_deletion(contact_id, "TRUE")
ContactManagement ->> ContactRepository: mark_contact_for_deletion(contact_id, "TRUE")
UI -->> user: UI is refreshed
user ->> UI: clicks 'delete marked' -button
UI ->> UI: event activates method _delete_marked_contacts()
UI ->> UI: constructs a messagebox for confirmation
user ->> UI: user presses "Confirm"
UI ->> UI: destroys widgets from frames treeview and text_view
UI ->> ContactManagement: delete_marked_contacts()
ContactManagement ->> ContactRepository: delete_marked_contacts()
UI ->> UI: constructs widgets to populate frames treeview and text_view
UI ->> UI: populates treeview with items
UI ->> UI: destroys widgets from contact_magement_frame
UI ->> UI: populates contact_magement_frame with widgets
UI -->> user: UI is refreshed
```
