from tkinter import ttk, constants, StringVar

from matplotlib.pyplot import text


class LoginView:
    def __init__(self, root, main_view, counselor_view, admin_view):
        self._root = root
        self._main_view = main_view
        self._counselor_view = counselor_view
        self._admin_view = admin_view
        self._frame_top = None
        self._frame_center = None
        self._frame_bottom = None

        self._entry_username_var = None
        self._entry_password_var = None
        
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
        
        self._frame_top = ttk.Frame(master=self._root, width=600, height=50)
        self._frame_center = ttk.Frame(master=self._root, width=600, height=200)
        self._frame_bottom = ttk.Frame(master=self._root, width=600, height=50)
        self._frame_top.grid_propagate(False)
        self._frame_center.grid_propagate(False)
        self._frame_bottom.grid_propagate(False)
        
        label_title = ttk.Label(master=self._frame_center, text="Submit username and password to login")        
        label_title.grid(row=0, column=0, columnspan=4)
        
        label_username = ttk.Label(master=self._frame_center, text="username")
        label_password = ttk.Label(master=self._frame_center, text="password")
        entry_username = ttk.Entry(master=self._frame_center, textvariable=self._entry_username_var)
        entry_password = ttk.Entry(master=self._frame_center, show="*", textvariable=self._entry_password_var)
        
        label_username.grid(row=1, column=1)
        entry_username.grid(row=1, column=2, columnspan=3, sticky=constants.EW)
        label_password.grid(row=2, column=1)
        entry_password.grid(row=2, column=2, columnspan=3, sticky=constants.EW)
    
        button_login = ttk.Button(
            master=self._frame_center,
            text="Submit",
            command=self._try_login
        )
        button_cancel = ttk.Button(
            master=self._frame_center,
            text="Cancel",
            command=self._main_view
        )
        
        button_login.grid(row=3, column=3)
        button_cancel.grid(row=3, column=4)
    
    def _try_login(self):
        try:
            if self._entry_password_var and self._entry_username_var:
                password_given = self._entry_password_var.get()
                username_given = self._entry_username_var.get()
                print(username_given, password_given)
            # Login
            # ... 
            # If success:

        except:
            print("Error, tried login with nonetype")
        
