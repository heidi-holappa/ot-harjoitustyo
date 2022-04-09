from tkinter import ttk, constants, StringVar, IntVar


class CreateAccountView:
    def __init__(self, root, main_view):
        self._root = root
        self._main_view = main_view
        self._frame_top = None
        self._frame_center = None
        self._frame_bottom = None

        self._entry_username_var = None
        self._entry_password_var = None
        self._entry_password_2_var = None
        self._entry_role_var = None
        
        self._initialize()

    def pack(self):
        if self._frame_top and self._frame_center and self._frame_bottom:
            self._frame_top.pack()
            self._frame_center.pack()
            self._frame_bottom.pack()
            

    def destroy(self):
        if self._frame_top and self._frame_center and self._frame_bottom:
            self._frame_top.destroy()
            self._frame_center.destroy()
            self._frame_bottom.destroy()


    def _initialize(self):
        self._entry_username_var = StringVar()
        self._entry_username_var.set("")
        self._entry_password_var = StringVar()
        self._entry_password_var.set("")
        self._entry_password_2_var = StringVar()
        self._entry_password_2_var.set("")
        self._entry_role_var = IntVar()
        self._entry_role_var.set(False)

        
        self._frame_top = ttk.Frame(master=self._root, width=600, height=50)
        self._frame_center = ttk.Frame(master=self._root, width=600, height=200)
        self._frame_bottom = ttk.Frame(master=self._root, width=600, height=50)
        self._frame_top.grid_propagate(False)
        self._frame_center.grid_propagate(False)
        self._frame_bottom.grid_propagate(False)
        
        label_title = ttk.Label(master=self._frame_center, text="Create an account")        
        label_title.grid(row=0, column=0, columnspan=4)
        
        label_username = ttk.Label(master=self._frame_center, text="select username")
        label_password = ttk.Label(master=self._frame_center, text="enter password")
        label_password_2 = ttk.Label(master=self._frame_center, text="re-enter password")
        entry_username = ttk.Entry(master=self._frame_center, textvariable=self._entry_username_var)
        entry_password = ttk.Entry(master=self._frame_center, show="*", textvariable=self._entry_password_var)
        entry_password_2 = ttk.Entry(master=self._frame_center, show="*", textvariable=self._entry_password_2_var)
        checkbox = ttk.Checkbutton(master=self._frame_center, text='Admin',variable=self._entry_role_var, onvalue=1, offvalue=0)
        
        label_username.grid(row=1, column=1)
        entry_username.grid(row=1, column=2, columnspan=3, sticky=constants.EW)
        label_password.grid(row=2, column=1)
        entry_password.grid(row=2, column=2, columnspan=3, sticky=constants.EW)
        label_password_2.grid(row=3, column=1)
        entry_password_2.grid(row=3, column=2, columnspan=3, sticky=constants.EW)
        checkbox.grid(row=4, column=2, columnspan=3)
    
        button_login = ttk.Button(
            master=self._frame_center,
            text="Submit",
            command=self._try_create
        )
        button_cancel = ttk.Button(
            master=self._frame_center,
            text="Cancel",
            command=self._main_view
        )
        
        button_login.grid(row=5, column=3)
        button_cancel.grid(row=5, column=4)
    
    def _try_create(self):
        try:
            if self._entry_password_var and self._entry_username_var and self._entry_role_var and self._entry_password_2_var:
                username_given = self._entry_username_var.get()
                password_given = self._entry_password_var.get()
                password_2_given = self._entry_password_2_var.get()
                is_admin = self._entry_role_var.get()
                print(username_given, password_given, password_2_given, is_admin)
            # Try to create
            # ... 
            # If success:
            # back to main screen
            # If not success
            # Inform of error and try again

        except:
            print("Error, tried login with nonetype")