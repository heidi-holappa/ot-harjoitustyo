from tkinter import Tk
from ui.gui_main_view import MainView
from ui.gui_login import LoginView
from ui.gui_create_account import CreateAccountView
from ui.gui_counselor import CounselorView
from ui.gui_admin import AdminView
from ui.gui_theme import setTheme
from ui.gui_create_dummy_data import CreateDummyData
from services.user_management import default_user_management


class UI:
    """Creates a hub-object to coordinate application logic for other GUI-objects.

    Attributes:
        root: root component of the GUI
        current_view: the current view to be constructed
        user_management: service class for user management
        style: currentl selected graphical style
    """

    def __init__(self, root):
        """Constructor for the class

        Args:
            root (Tk): root component of the GUI
        """
        self._root = root
        self._current_view = None
        self._user_management = default_user_management
        self.style = "default"
        setTheme(self._root)

    def start(self):
        """Calls a method that initiates the building of the main view
        """
        self._show_main_view()

    def _hide_current_view(self):
        """A method that destroys all widgets from the root component. 
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_main_view(self):
        """A method that call to construct the main view.

        If a user is logged in, they are logged out when entering main view.
        """

        self._user_management.logout()
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_login,
            self._handle_create_account
        )

        self._current_view.pack()

    def _show_login_view(self):
        """A method that calls the construction of the login view
        """
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._handle_main_view,
            self._handle_counselor_view,
            self._handle_admin_view,
            self._handle_create_dummy_data_view
        )

        self._current_view.pack()

    def _show_create_account_view(self):
        """A method that calls for the construction of the create account view
        """
        self._hide_current_view()
        self._current_view = CreateAccountView(
            self._root,
            self._handle_main_view
        )

        self._current_view.pack()

    def _show_counselor_view(self):
        """A method that calls to construct the counselor view
        """
        self._hide_current_view()
        self._current_view = CounselorView(
            self._root,
            self._handle_main_view,
            self._handle_admin_view,
            self._handle_create_dummy_data_view
        )

        self._current_view.pack()

    def _show_admin_view(self):
        """A method that calls to construct the admin view
        """
        self._hide_current_view()
        self._current_view = AdminView(
            self._root,
            self._handle_main_view,
            self._handle_counselor_view,
            self._handle_admin_view,
            self._handle_create_dummy_data_view
        )

        self._current_view.pack()

    def _show_create_dummy_data_view(self):
        """A method that calls to construct the dummy data view.
        """
        self._hide_current_view()
        self._current_view = CreateDummyData(
            self._root,
            self._handle_main_view,
            self._handle_admin_view
        )
        self._current_view.pack()

    def _handle_login(self):
        """A method that can be referenced and then handles 
        the method call for building login view"""
        self._show_login_view()

    def _handle_create_account(self):
        """A method that can be referenced and then handles 
        the method call for building create account view"""
        self._show_create_account_view()

    def _handle_main_view(self):
        """A method that can be referenced and then handles 
        the method call for building main view"""
        self._show_main_view()

    def _handle_counselor_view(self):
        """A method that can be referenced and then handles 
        the method call for building counselor view"""
        self._show_counselor_view()

    def _handle_admin_view(self):
        """A method that can be referenced and then handles 
        the method call for building admin view"""
        self._show_admin_view()

    def _handle_create_dummy_data_view(self):
        """A method that can be referenced and then handles 
        the method call for building dummy data view"""
        self._show_create_dummy_data_view()


def main():
    """A method that launches the application.
    """
    window = Tk()
    window.title("Backup data submission application")

    ui = UI(window)
    ui.start()

    window.mainloop()
