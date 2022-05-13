from tkinter import ttk, constants, Frame, Menu
from ui.gui_menu import GuiMenu


class MainView:
    """Creates the main view of the application.

    Attributes:
        root: root component of the GUI
        login: a reference to a method that handles creating the login view
        create account: a reference to a method that handles the creation of create account view
        frame: a variable for creating the Frame object
    """

    def __init__(self, root, login, create_account):
        self._root = root
        self._login = login
        self._create_account = create_account
        self._frame = None

        self._initialize()

    def pack(self):
        """A method to add the widgets to the GUI and make them visible to the user.
        """
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        """A method to destroy the Frame-object and all it's children. 
        """
        if self._frame:
            self._frame.destroy()

    def _create_menubar(self):
        """A method that calls for the construction of default menu bar.
        """
        create_menu = GuiMenu(self._root)
        menubar = create_menu.init_default_menu(
            self._login,
            self._create_account)
        self._root.config(menu=menubar)

    def _initialize(self):
        """Initializes the widgets in the main view. 
        """

        self._frame = Frame(self._root,
                            padx=50,
                            pady=50,
                            bg="grey95")
        self._create_menubar()
        label = ttk.Label(
            master=self._frame,
            text="Welcome to the backup data submission application!",
            style="Header1.TLabel")

        label_description = ttk.Label(
            master=self._frame,
            text="You can use this app to temporarily store contact information\nin case the main cloud-services are unavailable. \n\nSee 'help' from menu for additional information.",
            style="Centered.TLabel")

        button_login = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login,
            style="Custom.TButton"
        )
        button_create_account = ttk.Button(
            master=self._frame,
            text="Create account",
            command=self._create_account,
            style="Custom.TButton"
        )

        label_login = ttk.Label(
            master=self._frame, text="Already a user? Login here.",
            style="Custom.TLabel"
        )
        label_create_account = ttk.Label(
            master=self._frame, text="New user? Create account here.",
            style="Custom.TLabel"
        )

        label.grid(
            row=0,
            column=0,
            padx=10,
            pady=0
        )

        label_description.grid(
            row=1,
            column=0,
            pady=10
        )

        label_login.grid(
            row=2,
            column=0,
            pady=10
        )
        button_login.grid(
            row=3,
            column=0
        )
        label_create_account.grid(
            row=4,
            column=0,
            pady=10
        )
        button_create_account.grid(
            row=5,
            column=0
        )
