from tkinter import ttk, constants, Frame, Text, messagebox
from services.contact_management import ContactManagement
from services.user_management import default_user_management


class AdminView:
    """Creates the main view for users with the role 'admin.

    Attributes:
        root: root component for constructing the view
        main_view: a reference to the method that calls view MainView
        counselor_view: a reference to the method that calls view CounselorView
        admin_view: a reference to the method that calls view AdminView
        dummy_data: a reference to the method that calls view CreateDummyData
        default_user_management: default service class for user management
    """

    def __init__(self,
                 root,
                 main_view,
                 counselor_view,
                 admin_view,
                 dummy_data,
                 user_management=default_user_management):
        """Constructor for initializing an object of the class.

        Args:
            root (Tk): root component for constructing views
            main_view (MainView): a reference to the methong that calls view MainView
            counselor_view (CounselorView): a reference to the method that calls view CounselorView
            admin_view (AdminView): a reference to the method that calls view AdminView
            dummy_data (CreateDummyData): a reference to the method that calls view CreateDummyData
            user_management (UserManagement, optional): Service class object for user management.
            Defaults to default_user_management.
        """

        self._root = root
        self._main_view = main_view
        self._counselor_view = counselor_view
        self._admin_view = admin_view
        self._create_dummy_data = dummy_data

        self._frame = None

        self._contact_management = ContactManagement()
        self._user_management = user_management
        self._initialize()

    def pack(self):
        """A method to add the widgets to the GUI and make them visible to the user.
        """
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        """A method to destroy the Frame-object and all it's children. 
        """
        if self._frame:
            self._frame.destroy()

    def _initialize(self):
        """A method that initializes the default view.

        Please note that the method has multiple method calls. 
        """

        self._frame = Frame(
            master=self._root,
            padx=50,
            pady=50,
            bg="grey95"
        )
        self.nav_buttons_frame = ttk.LabelFrame(
            master=self._frame,
            text="Navigation buttons",
            style="Custom.TLabelframe",
        )
        self.treeview_frame = ttk.LabelFrame(
            master=self._frame,
            text="Submitted contacts",
            style="Custom.TLabelframe"
        )
        self.textview_frame = ttk.LabelFrame(
            master=self._frame,
            text="Preview selected contact",
            style="Custom.TLabelframe"
        )
        self.contact_management_frame = ttk.LabelFrame(
            master=self._frame,
            text="Manage selected contact",
            style="Custom.TLabelframe"
        )

        self.nav_buttons_frame.grid(sticky=constants.EW)
        self.treeview_frame.grid(sticky=constants.EW)
        self.textview_frame.grid(sticky=constants.EW)
        self.contact_management_frame.grid(sticky=constants.EW)

        self._init_buttons(self.nav_buttons_frame)
        self._init_treeview(self.treeview_frame)
        self._init_textfield(self.textview_frame)
        self._populate_treeview(self.treeview)
        self._init_contact_management_buttons(self.contact_management_frame)

        self.treeview.bind('<<TreeviewSelect>>', self.item_selected)

    def _init_buttons(self, selected_frame):
        """Initializes the navigation buttons.

        Args:
            selected_frame (LabelFrame): LabelFrame widget in which the buttons are to be embedded.
        """
        button_logout = ttk.Button(
            master=selected_frame,
            text="Logout",
            command=self._main_view,
            style="Custom.TButton"
        )

        button_counselor = ttk.Button(
            master=selected_frame,
            text="Counselor view",
            command=self._counselor_view,
            style="Custom.TButton"
        )

        button_admin_stuff = ttk.Button(
            master=selected_frame,
            text="Create dummy data",
            command=self._create_dummy_data,
            style="Custom.TButton"
        )

        button_counselor.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky=constants.W
        )
        button_admin_stuff.grid(
            row=0,
            column=1,
            padx=20,
            sticky=constants.W
        )
        button_logout.grid(
            row=0,
            column=2,
            padx=10,
            pady=5,
            sticky=constants.E
        )

    def _init_treeview(self, selected_frame: ttk.Labelframe):
        """Initializes the treeview and scrollbar widgets.

        Treeview creates a table like element for showcasing data. 

        Args:
            selected_frame (LabelFrame): LabelFrame widget in which the buttons are to be embedded.
        """
        columns = ("rowid", "username", "date_and_time",
                   "channel", "type", "delete")
        self.treeview = ttk.Treeview(
            master=selected_frame,
            columns=columns,
            show="headings",
            selectmode="browse",
            style="Custom.Treeview"
        )
        self.treeview.column("rowid", stretch=False, width=40)
        self.treeview.heading("rowid", text="ID")
        self.treeview.column("username", stretch=False, width=150)
        self.treeview.heading("username", text="username")
        self.treeview.column("date_and_time", stretch=False, width=150)
        self.treeview.heading("date_and_time", text="date and time")
        self.treeview.column("channel", stretch=False, width=150)
        self.treeview.heading("channel", text="channel")
        self.treeview.column("type", stretch=False, width=150)
        self.treeview.heading("type", text="type")
        self.treeview.column("delete", stretch=False, width=60)
        self.treeview.heading("delete", text="delete")

        scrollbar = ttk.Scrollbar(
            master=self.treeview_frame,
            orient=constants.VERTICAL,
            command=self.treeview.yview,
            style="Vertical.TScrollbar"
        )

        self.treeview.grid(
            row=0,
            column=0,
            sticky=constants.NSEW
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky=constants.NS
        )

        self.treeview.bind("<Button-3>", self._mark_keybind)

    def _init_textfield(self, selected_frame: ttk.Labelframe):
        """A method for creating the initial Text-widget for showing the selected contacts. 

        Args:
            selected_frame (LabelFrame): LabelFrame widget in which the buttons are to be embedded.
        """
        # String is composed in this way to get the desired formatting in the Text-widget
        default_printout = "Choose contact to view more details and options.\n \n Hint: once you click an item with left click, you can then use right click to mark item for deletion."
        textfield = Text(
            master=selected_frame,
            wrap="word",
            bg="white"
        )
        textfield.grid(
            row=3,
            column=0
        )

        textfield.insert(1.0, default_printout)
        textfield["state"] = "disabled"

    def item_selected(self, event):
        """A method that is called when user selects an item in the treeview widget.

        Method builds a new Text-widget and populates it with the selected contact data.

        Args:
            event (event): LabelFrame widget in which the buttons are to be embedded.
        """

        '''insert selected row into a Text widget'''
        printout = ""
        selected = self.treeview.focus()
        selected_item = self.treeview.item(selected, "values")
        rowid = selected_item[0]
        contact = self._contact_management.fetch_selected_contact(rowid)

        printout = (f"Username: {str(contact[1])}\n")
        printout += "date and time: " + str(contact[2]) + "\n"
        printout += "channel: " + str(contact[3])
        printout += ", type: " + str(contact[4])
        if contact[4] != "None":
            printout += ", gender: " + str(contact[5])
            printout += ", age: " + str(contact[6])
            printout += "\n\n" + "content:\n"
            printout += str(contact[7])

        textfield = Text(
            master=self.textview_frame,
            wrap="word",
            bg="white"
        )

        textfield.grid(
            row=3,
            column=0
        )

        textfield.insert(1.0, printout)
        textfield["state"] = "disabled"
        if contact[-1] == "TRUE":
            manage_text = "Unmark contact"
        else:
            manage_text = "Mark contact for deletion"
        self._insert_contact_buttons(manage_text)

    def clear_frame(self, frame: ttk.LabelFrame):
        """A general method for clearing a selected frame before repopulating it. 

        Can be used for multiple purposes. 

        Args:
            frame (ttk.LabelFrame): LabelFrame widget in which the buttons are to be embedded.
        """
        for widgets in frame.winfo_children():
            widgets.destroy()

    def _insert_contact_buttons(self, manage_text: str):
        """A method for creating new buttons when a contact is selected in Treeview widget.

        Args:
            manage_text (str): A varying text depending on whether the contact is marked for deletion or not.
        """
        self.clear_frame(self.contact_management_frame)
        selected = self.treeview.focus()
        selected_item = self.treeview.item(selected, "values")

        button_mark_contact = ttk.Button(
            master=self.contact_management_frame,
            text=manage_text,
            command=lambda: self._mark_contact_for_deletion(selected_item[0]),
            style="Custom.TButton"
        )

        button_delete = ttk.Button(
            master=self.contact_management_frame,
            text="Delete selected",
            command=self._delete_marked_contacts,
            style="Custom.TButton"
        )

        button_mark_contact.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky=constants.E
        )

        button_delete.grid(
            row=0,
            column=1,
            padx=10,
            pady=5,
            sticky=constants.E
        )

    def _populate_treeview(self, treeview: ttk.Treeview):
        """A method for populating the Treeview with contact data

        Args:
            treeview (ttk.Treeview): a Treeview widget
        """
        contacts = self._contact_management.fetch_treeview_contact_info()
        for contact in contacts:
            treeview.insert('', constants.END, values=contact)

    def _delete_contact(self, c_id: int):
        """A method for deleting a selected contact

        Args:
            c_id (int): rowid of the selected contact
        """
        self._contact_management.delete_contact(c_id)

    def _mark_keybind(self, event):
        """A method for handling right mouse click

        Args:
            event (event): activates on right mouse click
        """
        item = self.treeview.identify_row(event.y)
        if item:
            selected_item = self.treeview.item(item, 'values')
            self._mark_contact_for_deletion(selected_item[0])

    def _mark_contact_for_deletion(self, c_id: int):
        """A method that handles changing a contact's deletion status.

        Contact can be selected or de-selected for deletion.

        Args:
            c_id (int): rowid of the selected contact
        """
        selected = self.treeview.focus()
        selected_item = list(self.treeview.item(selected, "values"))
        if selected_item:
            if selected_item[-1] == "":
                selected_item[-1] = "TRUE"
            else:
                selected_item[-1] = ""
            updated_selected = tuple(selected_item)
            self.treeview.item(selected, text="", values=(updated_selected))
            self._contact_management.mark_contact_for_deletion(
                c_id, selected_item[-1])

    def _delete_marked_contacts(self):
        """A method that initiates the deletion of all marked contacts.
        """
        check_ok = messagebox.askokcancel(
            title="Confirm deletion",
            message="Selected entries will be deleted.",
            icon=messagebox.WARNING)
        if not check_ok:
            return
        self.clear_frame(self.textview_frame)
        self.clear_frame(self.treeview_frame)
        self._contact_management.delete_marked_contacts()
        self._init_textfield(self.textview_frame)
        self._init_treeview(self.treeview_frame)
        self._populate_treeview(self.treeview)
        self.clear_frame(self.contact_management_frame)
        self._init_contact_management_buttons(self.contact_management_frame)
        self.treeview.bind('<<TreeviewSelect>>', self.item_selected)

    def _init_contact_management_buttons(self, selected_frame: ttk.Labelframe):
        """A method that creates the initial contact management buttons.

        Before a selection has been made the buttons are disabled. 

        Args:
            selected_frame (_type_): _description_
        """
        button_mark_contact = ttk.Button(
            master=selected_frame,
            text="Mark contact for deletion",
            state="disabled",
            style="Custom.TButton"
        )

        button_delete = ttk.Button(
            master=selected_frame,
            text="Delete selected",
            state="disabled",
            style="Custom.TButton"
        )

        button_mark_contact.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky=constants.E
        )

        button_delete.grid(
            row=0,
            column=1,
            padx=10,
            pady=5,
            sticky=constants.E
        )
