from tkinter import Tk
from gui_main_view import MainView
from gui_login import LoginView
from gui_create_account import CreateAccountView

class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_main_view(self):
        self._hide_current_view
        self._current_view = MainView(
            self._root,
            self._show_login_view,
            self._show_create_account_view
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view
        self._current_view = LoginView(
            self._root,
            self.start
        )

        self._current_view.pack()
    
    def _show_create_account_view(self):
        self._hide_current_view
        self._current_view = CreateAccountView(
            self._root,
            self.start
        )

        self._current_view.pack()


# Launch the GUI
window = Tk()
window.title("Backup data submission application")

ui = UI(window)
ui.start()

window.mainloop()