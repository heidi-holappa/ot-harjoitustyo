from tkinter import ttk, constants, StringVar, IntVar, Frame
from entities.user import User
from services.user_management import UserManagement

class CreateAccountView:
    def __init__(self, root, main_view):
        self._root = root
        self._main_view = main_view
        self._frame = None

        self._entry_username_var = None
        self._entry_password_var = None
        self._entry_password_2_var = None
        self._entry_role_var = None
        
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

        
        self._frame = Frame(master=self._root, padx=50, pady=50)
       
        
        label_title = ttk.Label(master=self._frame, text="Create an account")        
        label_title.grid(row=0, column=0, columnspan=4)
        
        label_username = ttk.Label(master=self._frame, text="select username")
        label_password = ttk.Label(master=self._frame, text="enter password")
        label_password_2 = ttk.Label(master=self._frame, text="re-enter password")
        entry_username = ttk.Entry(master=self._frame, textvariable=self._entry_username_var)
        entry_password = ttk.Entry(master=self._frame, show="*", textvariable=self._entry_password_var)
        entry_password_2 = ttk.Entry(master=self._frame, show="*", textvariable=self._entry_password_2_var)
        checkbox = ttk.Checkbutton(master=self._frame, text='Admin',variable=self._entry_role_var, onvalue=1, offvalue=0)
        
        label_username.grid(row=1, column=1)
        entry_username.grid(row=1, column=2, columnspan=3, sticky=constants.EW)
        label_password.grid(row=3, column=1)
        entry_password.grid(row=3, column=2, columnspan=3, sticky=constants.EW)
        label_password_2.grid(row=4, column=1)
        entry_password_2.grid(row=4, column=2, columnspan=3, sticky=constants.EW)
        checkbox.grid(row=5, column=2, columnspan=3)
    
        button_login = ttk.Button(
            master=self._frame,
            text="Submit",
            command=self._try_create
        )
        button_cancel = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._main_view
        )
        
        button_login.grid(row=6, column=3)
        button_cancel.grid(row=6, column=4)
    
    def _try_create(self):
        try:
            if self._entry_password_var and self._entry_username_var and self._entry_role_var and self._entry_password_2_var:
                username_given = self._entry_username_var.get()
                password_given = self._entry_password_var.get()
                password_2_given = self._entry_password_2_var.get()
                is_admin = self._entry_role_var.get()
                print(username_given, password_given, password_2_given, is_admin)
                user_manager = UserManagement()
                is_valid = user_manager.password_is_valid(password_given, password_2_given)
                if is_valid:
                    user = User(username_given, password_given)
                    if is_admin:
                        user.set_admin()
                    if user.create_user():
                        self._main_view()
                    else:
                        label_login_error = ttk.Label(master=self._frame, text="Account creation failed. Username most likely already in use.", foreground="red")        
                        label_login_error.grid(row=1, column=0, columnspan=4)
                else:
                    label_creation_error = ttk.Label(master=self._frame, text="Error: passwords do not match. Try again.", foreground="red")        
                    label_creation_error.grid(row=1, column=0, columnspan=4)
        except:
            print("Error, tried login with nonetype")