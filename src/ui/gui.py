from tkinter import Tk, ttk
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
        self.style = "default"
        self.app_style = ttk.Style(root)
        self.app_style.theme_use("clam")
        self.init_styles()

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
            self._handle_admin_view,
            self._handle_create_dummy_data_view
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
            self._handle_admin_view,
            self._handle_create_dummy_data_view
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
        print(self._show_admin_view)
        self._show_admin_view()

    def _handle_create_dummy_data_view(self):
        self._show_create_dummy_data_view()

    def init_styles(self):

        self._root.option_add('*Dialog.msg.font', 'Calibri 10')

        self.app_style.configure('Custom.TFrame',
                                 background="grey95",
                                 foreground="black")

        self.app_style.configure('Custom.TLabelframe',
                                 background="grey95",
                                 foreground="black")

        self.app_style.configure('TLabelframe.Label',
                                 background="grey95",
                                 foreground="black")

        self.app_style.configure('Custom.TButton',
                                 background="grey95",
                                 foreground="black",
                                 focuscolor="grey48",
                                 font='Calibri 10 bold')

        self.app_style.map('TButton', background=[("active", "grey78")])

        self.app_style.configure('Custom.TLabel',
                                 background="grey95",
                                 foreground="grey12",
                                 font='Calibri 10 bold',
                                 wraplength=400)

        self.app_style.configure('Centered.TLabel',
                                 background="grey95",
                                 foreground="grey12",
                                 justify="center",
                                 font='Calibri 10 bold',
                                 wraplength=400)

        self.app_style.configure('Success.TLabel',
                                 background="grey95",
                                 foreground="green",
                                 font='Calibri 10 bold',
                                 wraplength=400)

        self.app_style.configure('Error.TLabel',
                                 background="grey95",
                                 foreground="red",
                                 font='Calibri 10 bold',
                                 wraplength=400)

        self.app_style.configure('Header1.TLabel',
                                 background="grey95",
                                 foreground="black",
                                 font='Cambria 14 bold')

        self.app_style.configure('Custom.TEntry',
                                 background="grey95",
                                 foreground="black",
                                 font='Calibri 10')

        self.app_style.configure('Custom.TCheckbutton',
                                 background="grey95",
                                 foreground="black")
        self.app_style.map('TCheckbutton', background=[("disabled", "grey95")])

        self.app_style.configure('Custom.TRadiobutton',
                                 background="grey95",
                                 foreground="black",
                                 font='Calibri 10')

        self.app_style.map('TRadiobutton', background=[("disabled", "grey95")])

        self.app_style.configure('Custom.Treeview',
                                 background="white",
                                 foreground="black",
                                 font='Calibri 10')

        self.app_style.configure('Vertical.TScrollbar',
                                 background="grey95",
                                 foreground="black")

    # TEST BUILDING DARK MODE HERE
    # ADD SELECTION TO LOGIN AS A FIRST STEP
    def set_dark_mode(self):
        self.app_style.configure('Custom.TLabel',
                                 background="grey14",
                                 foreground="grey82",
                                 font='Helvetica 8 bold',
                                 wraplength=400)


# Launch the GUI

def main():
    window = Tk()
    window.title("Backup data submission application")

    ui = UI(window)
    ui.start()

    window.mainloop()
