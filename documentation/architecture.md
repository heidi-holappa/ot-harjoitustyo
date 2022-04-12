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
The package UI includes the classes responsible for creating the objects that create the graphical user interface and it's functionalities. The package Service works as a hub controlling the logic of the application. 

Package Entities contains the objects that contain the different data structures used by the application. The package Repositories handles the database queries (retrieving and storing data).

## Class diagram

Below is a visualization of the current class diagram and dependencies. The vision is to make refactor the code in week 5 to make the dependencies more structured. Feedback and tips on how to work towards this are very welcome!

```mermaid
    classDiagram
        class User
        class Contact
        class UserManagement
        class ContactManagement
        class ContactDataRepository
        class UserRepository
        class GUI_Login
        class GUI_CreateAccount
        class GUI_Counselor
        
        UserManagement --> User
        ContactManagement --> Contact
        ContactManagement --> User
        ContactManagement --> UserManagement
        ContactManagement --> ContactDataRepository
        UserManagement --> UserRepository
        GUI_Login --> UserManagement
        GUI_CreateAccount --> UserManagement
        GUI_Counselor --> ContactManagement
        GUI_Counselor --> UserManagement
        UserRepository --> User
        ContactRepository --> Contact
        ContactRepository --> User

```