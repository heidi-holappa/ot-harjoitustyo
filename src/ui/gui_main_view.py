from tkinter import ttk, constants, Frame, Menu


class MainView:
    def __init__(self, root, login, create_account):
        self._root = root
        self._login = login
        self._create_account = create_account
        self._frame = None

        self._initialize()

    def pack(self):
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _create_menubar(self):
        menubar = Menu(self._root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Login", command=self._login)
        filemenu.add_command(label="Create account",
                             command=self._create_account)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)
        self._root.config(menu=menubar)

    def exit(self):
        self._root.destroy()

    def _initialize(self):

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
