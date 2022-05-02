from tkinter import ttk, constants, StringVar, Frame, Menu, messagebox
import webbrowser
from services.user_management import default_user_management


class LoginView:
    def __init__(
        self, root,
        main_view,
        counselor_view,
        admin_view,
        dummy_data_view,
        user_management=default_user_management
    ):

        self._root = root
        self._main_view = main_view
        self._counselor_view = counselor_view
        self._admin_view = admin_view
        self._dummy_data_view = dummy_data_view
        self._frame = None

        self._entry_username_var = None
        self._entry_password_var = None

        self._user_management = user_management

        self._initialize()

    def pack(self):
        if self._frame:
            self._frame.pack()

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _initialize(self):
        self._entry_username_var = StringVar()
        self._entry_username_var.set("")
        self._entry_password_var = StringVar()
        self._entry_password_var.set("")

        self._frame = Frame(
            master=self._root,
            padx=50,
            pady=50,
            bg="grey95"
        )

        label_title = ttk.Label(
            master=self._frame,
            text="Submit username and password to login",
            style="Header1.TLabel"
        )

        label_username = ttk.Label(
            master=self._frame,
            text="username",
            style="Custom.TLabel"
        )

        label_password = ttk.Label(
            master=self._frame,
            text="password",
            style="Custom.TLabel"
        )

        entry_username = ttk.Entry(
            master=self._frame,
            textvariable=self._entry_username_var,
            style="Custom.TEntry"
        )

        entry_password = ttk.Entry(
            master=self._frame,
            show="*",
            textvariable=self._entry_password_var,
            style="Custom.TEntry"
        )

        button_login = ttk.Button(
            master=self._frame,
            text="Submit",
            command=self._try_login,
            style="Custom.TButton"
        )
        button_cancel = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._main_view,
            style="Custom.TButton"
        )

        label_title.grid(
            row=0,
            column=0,
            columnspan=4
        )

        label_username.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        entry_username.grid(
            row=2,
            column=2,
            columnspan=3,
            sticky=constants.EW
        )

        label_password.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )
        entry_password.grid(
            row=3,
            column=2,
            columnspan=3,
            sticky=constants.EW
        )

        button_login.grid(
            row=4,
            column=3,
            pady=10
        )

        button_cancel.grid(
            row=4,
            column=4,
            pady=10
        )

    def _try_login(self):

        if self._entry_password_var and self._entry_username_var:
            password_given = self._entry_password_var.get()
            username_given = self._entry_username_var.get()
            login_attempt = self._user_management.login(
                username_given, password_given)
            if login_attempt[0]:
                menubar = Menu(self._root)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Logout", command=self._main_view)
                filemenu.add_separator()
                filemenu.add_command(label="Exit", command=self.exit)
                menubar.add_cascade(label="File", menu=filemenu)

                if self._user_management.get_active_user_role() == "admin":
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
                self._root.config(menu=menubar)

                if login_attempt[1] == "counselor":
                    self._counselor_view()
                else:
                    self._admin_view()
            else:
                label_login_error = ttk.Label(
                    master=self._frame,
                    text="Error: username or password incorrect. Try again.",
                    style="Error.TLabel")
                label_login_error.grid(row=1, column=0, columnspan=4)
                label_login_error.after(
                    3000, lambda: label_login_error.destroy())

    def exit(self):
        self._root.destroy()

    def _open_help(self):
        webbrowser.open_new(
            "https://github.com/heidi-holappa/ot-harjoitustyo/blob/master/documentation/how-to-guide.md")

    def _show_about(self):
        messagebox.showinfo(
            title="About the application",
            message="Version 0.1\n\nCreated as a University project in 2022",
            icon=messagebox.INFO
        )
