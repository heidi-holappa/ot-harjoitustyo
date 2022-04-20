from tkinter import Tk
from ui.gui_main_view import MainView
from ui.gui_login import LoginView
from ui.gui_create_account import CreateAccountView
from ui.gui_counselor import CounselorView
from ui.gui_admin import AdminView
from ui.gui_create_dummy_data import CreateDummyData
from services.user_management import default_user_management


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._user_management = default_user_management
        # self._root.geometry("600x300")

    def start(self):
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_main_view(self):
        self._user_management.logout()
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_login,
            self._handle_create_account
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._handle_main_view,
            self._handle_counselor_view,
            self._handle_admin_view
        )

        self._current_view.pack()

    def _show_create_account_view(self):
        self._hide_current_view()
        self._current_view = CreateAccountView(
            self._root,
            self._handle_main_view
        )

        self._current_view.pack()

    def _show_counselor_view(self):
        self._hide_current_view()
        self._current_view = CounselorView(
            self._root,
            self._handle_main_view,
            self._handle_admin_view
        )

        self._current_view.pack()

    def _show_admin_view(self):
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
        self._hide_current_view()
        self._current_view = CreateDummyData(
            self._root,
            self._handle_main_view,
            self._handle_admin_view
        )
        self._current_view.pack()

    def _handle_login(self):
        self._show_login_view()

    def _handle_create_account(self):
        self._show_create_account_view()

    def _handle_main_view(self):
        self._show_main_view()

    def _handle_counselor_view(self):
        self._show_counselor_view()

    def _handle_admin_view(self):
        self._show_admin_view()

    def _handle_create_dummy_data_view(self):
        self._show_create_dummy_data_view()


# Launch the GUI

def main():
    window = Tk()
    window.title("Backup data submission application")

    ui = UI(window)
    ui.start()

    window.mainloop()
