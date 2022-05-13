from tkinter import Menu, messagebox
import webbrowser
from entities.user import Role
from services.user_management import default_user_management


class GuiMenu:

    def __init__(self,
                 root,
                 user_management=default_user_management):
        """Constructor for initializing an object of the class.

        Args:
            root (Tk): root component for constructing viewsself._entry_username_var = None
        self._entry_password_var = None
            _frame: a variable for the object Frame
            user_management (UserManagement, optional): Service class object for user management.
            Defaults to default_user_management.
        """

        self._root = root
        self._user_management = user_management

    def init_default_menu(self,
                          login,
                          create_account):
        """A method that creates an initial menu bar.

        Args:
            login (method reference): calls for the initialization of login view
            create_account (method reference): calls for the initalization of create account view
        """
        menubar = Menu(self._root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Login", command=login)
        filemenu.add_command(label="Create account",
                             command=create_account)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)
        self._root.config(menu=menubar)

    def init_logged_menu(self,
                         main_view,
                         counselor_view,
                         admin_view,
                         dummy_data_view):
        """A method that constructs a new Menu after user logs in.
        
        Agrs:
            main_view (MainView): a reference to the methong that calls view MainView
            counselor_view (CounselorView): a reference to the method that calls view CounselorView
            admin_view (AdminView): a reference to the method that calls view AdminView
            dummy_data (CreateDummyData): a reference to the method that calls view CreateDummyData
        """
        menubar = Menu(self._root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Logout", command=main_view)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        if self._user_management.get_active_user_role() == Role.ADMIN:
            adminmenu = Menu(menubar, tearoff=0)
            adminmenu.add_command(
                label="Manage data submissions", command=admin_view)
            adminmenu.add_command(
                label="Submit data", command=counselor_view)
            adminmenu.add_command(
                label="Create dummy content", command=dummy_data_view)
            menubar.add_cascade(label="Admin", menu=adminmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(
            label="Help (opens browser)", command=self._open_help)
        helpmenu.add_command(label="About", command=self._show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        return menubar

    def exit(self):
        """Method that destroys the root component and exits the application.
        """
        self._root.destroy()

    def _open_help(self):
        """A method that opens the how-to-guide in the operating system's default browser.
        """
        webbrowser.open_new(
            "https://github.com/heidi-holappa/ot-harjoitustyo/blob/master/documentation/how-to-guide.md")

    def _show_about(self):
        """A method that prompts a messabox with project information.
        """
        messagebox.showinfo(
            title="About the application",
            message="Version 0.1\n\nCreated as a University project in 2022",
            icon=messagebox.INFO
        )
