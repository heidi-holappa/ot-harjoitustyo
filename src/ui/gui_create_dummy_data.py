from tkinter import ttk, constants, Frame, StringVar, IntVar, Radiobutton, Text
from services.contact_management import ContactManagement


class CreateDummyData:
    def __init__(self,
                 root,
                 main_view,
                 admin_view):

        self._root = root
        self._main_view = main_view
        self._admin_view = admin_view

        self._frame = None

        self._contact_management = ContactManagement()
        self._initialize()

    def pack(self):
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root, padx=50, pady=50)
        label = ttk.Label(
            master=self._frame,
            text="Select the amount of dummy data to create")

        button_logout = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._main_view
        )

        button_admin_stuff = ttk.Button(
            master=self._frame,
            text="Create data",
            command=self._do_admin_stuff
        )

        label.grid(row=0, column=0, pady=5, sticky=constants.W)

        button_admin_stuff.grid(row=0, column=1,
                                padx=20,
                                sticky=constants.E)
        button_logout.grid(row=0, column=3,
                           padx=10, pady=5,
                           sticky=constants.E)

    def _do_admin_stuff(self):
        print("Hello admin world!")
