from tkinter import ttk, constants, StringVar, IntVar, Frame
from services.user_management import default_user_management


class CreateAccountView:
    def __init__(self, root, main_view,
                 user_management=default_user_management):
        self._root = root
        self._main_view = main_view
        self._frame = None

        self._entry_username_var = None
        self._entry_password_var = None
        self._entry_password_2_var = None
        self._entry_role_var = None

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
        self._entry_password_2_var = StringVar()
        self._entry_password_2_var.set("")
        self._entry_role_var = IntVar()
        self._entry_role_var.set(False)

        self._frame = Frame(master=self._root,
                            padx=50,
                            pady=50,
                            bg="grey95")

        label_title = ttk.Label(master=self._frame,
                                text="Create an account",
                                style="Header1.TLabel"
                                )
        label_title.grid(row=0, column=0, columnspan=4)

        label_username = ttk.Label(master=self._frame,
                                   text="select username",
                                   style="Custom.TLabel"
                                   )
        label_password = ttk.Label(master=self._frame,
                                   text="enter password",
                                   style="Custom.TLabel"
                                   )
        label_password_2 = ttk.Label(
            master=self._frame,
            text="re-enter password",
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
        entry_password_2 = ttk.Entry(
            master=self._frame,
            show="*",
            textvariable=self._entry_password_2_var,
            style="Custom.TEntry"
        )
        checkbox = ttk.Checkbutton(
            master=self._frame,
            text='Admin',
            variable=self._entry_role_var,
            onvalue=1,
            offvalue=0,
            style="Custom.TCheckbutton")

        label_username.grid(row=2,
                            column=1,
                            padx=5,
                            pady=5
                            )
        entry_username.grid(row=2,
                            column=2,
                            columnspan=3,
                            sticky=constants.EW
                            )
        label_password.grid(row=4,
                            column=1,
                            padx=5,
                            pady=5
                            )
        entry_password.grid(row=4,
                            column=2,
                            columnspan=3,
                            sticky=constants.EW
                            )
        label_password_2.grid(row=5,
                              column=1,
                              padx=5,
                              pady=5
                              )
        entry_password_2.grid(
            row=5,
            column=2,
            columnspan=3,
            sticky=constants.EW)
        checkbox.grid(row=6,
                      column=2,
                      columnspan=3,
                      padx=5,
                      pady=5)

        button_login = ttk.Button(
            master=self._frame,
            text="Submit",
            command=self._try_create,
            style="Custom.TButton"
        )
        button_cancel = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._main_view,
            style="Custom.TButton"
        )

        button_login.grid(row=7, column=3)
        button_cancel.grid(row=7, column=4)

    def _try_create(self):
        if self._entry_password_var and self._entry_username_var and self._entry_role_var and self._entry_password_2_var:
            username_given = self._entry_username_var.get()
            password_given = self._entry_password_var.get()
            password_2_given = self._entry_password_2_var.get()
            is_admin = self._entry_role_var.get()
            result = self._user_management.handle_user_creation(
                username_given,
                password_given,
                password_2_given,
                is_admin)
            if result[0]:
                self._main_view()
            else:
                label_login_error = ttk.Label(
                    master=self._frame,
                    text=result[1],
                    foreground="red",
                    style="Custom.TLabel")
                label_login_error.grid(row=1, column=0, columnspan=4)
                label_login_error.after(
                    3000, lambda: label_login_error.destroy())
