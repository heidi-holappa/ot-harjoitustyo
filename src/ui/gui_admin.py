from tkinter import ttk, constants, Frame, StringVar, IntVar, Radiobutton, Text
from services.contact_management import ContactManagement
from services.user_management import default_user_management


class AdminView:
    def __init__(self, 
                root, 
                main_view, 
                counselor_view, 
                user_management=default_user_management):
        
        self._root = root
        self._main_view = main_view
        self._counselor_view = counselor_view
                
        self._frame = None


        self._initialize()
        self._contact_management = ContactManagement()
        self._user_management = user_management

    def pack(self):
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root, padx=50, pady=50)
        label = ttk.Label(
            master=self._frame, text="You are now in the Admin View")

        button_logout = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._main_view
        )

        label.grid(row=0, column=0, pady=5, sticky=constants.W)
        button_logout.grid(row=0, column=1, padx=10,
                           pady=5, sticky=constants.E)

        button_logout = ttk.Button(
            master=self._frame,
            text="Counselor view",
            command=self._counselor_view
        )

        label.grid(row=0, column=1, pady=5, sticky=constants.W)
        button_logout.grid(row=1, column=1, padx=10,
                           pady=5, sticky=constants.E)



        button_submit = ttk.Button(
            master=self._frame,
            text="Do admin stuff",
            command=self._do_admin_stuff
        )
        button_submit.grid(row=17, column=1, sticky=constants.E, padx=20)

    def _do_admin_stuff(self):
        print("Hello admin world!")
