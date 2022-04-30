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
        self._frame = Frame(
            master=self._root,
            padx=50,
            pady=50,
            bg="white")
        label = ttk.Label(
            master=self._frame,
            text='''This view is intended for the staging version of this application. User can create between 1 to 100 accounts of dummydata, or delete all contacts for a fresh start. Enter the desired amount of dummy data in the entry field.''',
            style="Custom.TLabel"
            )

        # THIS DOES NOT WORK. FIX IT.
        user_entry = ttk.Entry(
            master=self._frame,
            style="Custom.TEntry")
        user_entry.insert(constants.END, "0")

        button_logout = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._admin_view,
            style="Custom.TButton"
        )

        button_create_dummy_data = ttk.Button(
            master=self._frame,
            text="Create data",
            command=lambda: self._create_dummy_data(user_entry.get()),
            style="Custom.TButton"
        )

        button_delete_all_data = ttk.Button(
            master=self._frame,
            text="Delete all contacts",
            command=self._delete_all_data,
            style="Custom.TButton"
        )

        label.grid(
            row=0, 
            column=0,
            columnspan=3,
            pady=5,
            sticky=constants.W
        )
        
        user_entry.grid(
            row=2,
            columnspan=3,
            sticky=constants.NW
        )

        button_create_dummy_data.grid(
            row=3,
            column=0,
            padx=20,
            sticky=constants.E
        )

        button_delete_all_data.grid(
            row=3,
            column=1,
            padx=10,
            pady=5,
            sticky=constants.E
        )

        button_logout.grid(
            row=3,
            column=3,
            padx=10,
            pady=5,
            sticky=constants.E
        )

    # Consider moving data validation to service class
    def _create_dummy_data(self, input):
        failed = False
        if not input.isnumeric() or not input.isdigit():
            failed = True
        n_of_contacts = 0
        try:
            n_of_contacts = int(input)
        except (TypeError, ValueError) as e:
            failed = True
        if failed:
            label_fail = ttk.Label(
                master=self._frame,
                text="Input is not a number, please input an integer value.",
                style="Error.TLabel"
            )
            label_fail.grid(row=1, column=0, columnspan=4)
            label_fail.after(3000, lambda: label_fail.destroy())
            return
        self._contact_management.create_random_contacts(n_of_contacts)
        self._admin_view()

    def _delete_all_data(self):
        self._contact_management.delete_all_contacts()
        self._admin_view()
