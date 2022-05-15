from tkinter import ttk, constants, Frame, messagebox
from services.contact_management import ContactManagement


class CreateDummyData:
    """Creates an object for building a dummy data creation view

    Attributes:

        root: root component for constructing GUI-views
        main_view: a reference to a method that handles showing the main view
        admin_view: a reference to a method that handles showing the admin view
    """

    def __init__(self,
                 root,
                 main_view,
                 admin_view):
        """A constructor for the class

        Args:
            root (Tk): root component for constructing GUI-views
            main_view (reference to a method): a reference to a method 
            that handles showing the main view
            admin_view (reference to a method): a reference to a method 
            that handles showing the admin view
            _frame: a variable for the Frame object
            _contact_management: service class object for contact management

        """

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
        """A method to destroy the Frame-object and all it's children. 
        """
        if self._frame:
            self._frame.destroy()

    def _initialize(self):
        """A method that initializes the default view.
        """
        self._frame = Frame(
            master=self._root,
            padx=50,
            pady=50,
            bg="grey95")
        label = ttk.Label(
            master=self._frame,
            text='''This view is intended for the staging version of this application. User can create between 1 to 100 accounts of dummydata, or delete all contacts for a fresh start. Enter the desired amount of dummy data in the entry field.''',
            style="Custom.TLabel"
        )

        user_entry = ttk.Entry(
            master=self._frame,
            style="Custom.TEntry")
        user_entry.insert(constants.END, "0")

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

        button_logout = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._admin_view,
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

    def _create_dummy_data(self, input):
        """A method that handles creation of contact data.

        Args:
            input (int/str/None): an int value is expected, but as users
            can type in the value, invalid data types are prepared for.
        """
        failed = False
        status = ""
        if not input.isnumeric() or not input.isdigit():
            failed = True
            status = "Value must be a positivive integer between 1 and 100. "
        n_of_contacts = 0
        try:
            n_of_contacts = int(input)
        except (TypeError, ValueError) as e:
            failed = True
            status = "Value must be a positive integer between 1 and 100. "
        if not failed:
            failed = bool(n_of_contacts < 1 or 100 < n_of_contacts)
            if failed:
                status += "Value must be between 1 and 100."
        if failed:
            label_fail = ttk.Label(
                master=self._frame,
                text=status,
                style="Error.TLabel"
            )
            label_fail.grid(row=1, column=0, columnspan=4)
            label_fail.after(3000, lambda: label_fail.destroy())
            return
        result, status_msg = self._contact_management.create_random_contacts(
            n_of_contacts)
        if not result:
            label_fail = ttk.Label(
                master=self._frame,
                text=status_msg,
                style="Error.TLabel"
            )
            label_fail.grid(row=1, column=0, columnspan=4)
            label_fail.after(3000, lambda: label_fail.destroy())
            return
        self._admin_view()

    def _delete_all_data(self):
        """A method that initiates deletion of all contacts from the database.
        """
        check_ok = messagebox.askokcancel(
            title="Confirm deletion",
            message="Are you sure? All contact data will be deleted.",
            icon=messagebox.WARNING)
        if not check_ok:
            return
        self._contact_management.delete_all_contacts()
        self._admin_view()
