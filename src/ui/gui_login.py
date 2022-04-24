from tkinter import ttk, constants, StringVar, Frame
from services.user_management import default_user_management


class LoginView:
    def __init__(self, root, main_view, counselor_view, admin_view,
                 user_management=default_user_management):
        self._root = root
        self._main_view = main_view
        self._counselor_view = counselor_view
        self._admin_view = admin_view
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

        self._frame = Frame(master=self._root, padx=50, pady=50)

        label_title = ttk.Label(
            master=self._frame, text="Submit username and password to login")
        label_title.grid(row=0, column=0, columnspan=4)

        label_username = ttk.Label(master=self._frame, text="username")
        label_password = ttk.Label(master=self._frame, text="password")
        entry_username = ttk.Entry(
            master=self._frame, textvariable=self._entry_username_var)
        entry_password = ttk.Entry(
            master=self._frame, show="*", textvariable=self._entry_password_var)

        label_username.grid(row=2, column=1)
        entry_username.grid(row=2, column=2, columnspan=3, sticky=constants.EW)
        label_password.grid(row=3, column=1)
        entry_password.grid(row=3, column=2, columnspan=3, sticky=constants.EW)

        button_login = ttk.Button(
            master=self._frame,
            text="Submit",
            command=self._try_login
        )
        button_cancel = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._main_view
        )

        button_login.grid(row=4, column=3)
        button_cancel.grid(row=4, column=4)

    def _try_login(self):

        if self._entry_password_var and self._entry_username_var:
            password_given = self._entry_password_var.get()
            username_given = self._entry_username_var.get()
            self._user_management.create_active_user(
                username_given, password_given)
            login_attempt = self._user_management.login()
            if login_attempt[0]:
                if login_attempt[1] == "counselor":
                    self._counselor_view()
                else:
                    self._admin_view()
            else:
                label_login_error = ttk.Label(
                    master=self._frame, text="Error: username or password incorrect. Try again.", foreground="red")
                label_login_error.grid(row=1, column=0, columnspan=4)
