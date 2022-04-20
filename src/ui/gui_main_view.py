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
        self._frame = Frame(self._root, padx=50, pady=50)
        self._create_menubar()
        label = ttk.Label(
            master=self._frame, text="Welcome to the backup data submission application!")

        button_login = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login
        )
        button_create_account = ttk.Button(
            master=self._frame,
            text="Create account",
            command=self._create_account
        )

        label.grid(row=0, column=1)
        button_login.grid(row=1, column=1)
        button_create_account.grid(row=2, column=1)
