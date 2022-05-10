from tkinter import Menu, messagebox
import webbrowser
from entities.user import Role
from services.user_management import default_user_management

class GuiMenu:

    def __init__(self, 
            root,
            main_view,
            counselor_view,
            admin_view,
            dummy_data_view,
            user_management=default_user_management):
        """Constructor for initializing an object of the class.

        Args:
            root (Tk): root component for constructing viewsself._entry_username_var = None
        self._entry_password_var = None

            main_view (MainView): a reference to the methong that calls view MainView
            counselor_view (CounselorView): a reference to the method that calls view CounselorView
            admin_view (AdminView): a reference to the method that calls view AdminView
            dummy_data (CreateDummyData): a reference to the method that calls view CreateDummyData
            _frame: a variable for the object Frame
            _entry_username_var: a variable for the username entry
            _entry_password_var: a variable for the password entry
            user_management (UserManagement, optional): Service class object for user management.
            Defaults to default_user_management.
        """

        self._root = root
        self._main_view = main_view
        self._counselor_view = counselor_view
        self._admin_view = admin_view
        self._dummy_data_view = dummy_data_view
        self._frame = None

        self._user_management = user_management


    def init_menu(self):
        menubar = Menu(self._root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Logout", command=self._main_view)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        if self._user_management.get_active_user_role() == Role.ADMIN:
            adminmenu = Menu(menubar, tearoff=0)
            adminmenu.add_command(
                label="Manage data submissions", command=self._admin_view)
            adminmenu.add_command(
                label="Submit data", command=self._counselor_view)
            adminmenu.add_command(
                label="Create dummy content", command=self._dummy_data_view)
            menubar.add_cascade(label="Admin", menu=adminmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(
            label="Help (opens browser)", command=self._open_help)
        helpmenu.add_command(label="About", command=self._show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        return menubar
        # self._root.config(menu=menubar)

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
