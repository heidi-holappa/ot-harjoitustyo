from tkinter import ttk, constants, Frame, Text, Scrollbar, messagebox
from services.contact_management import ContactManagement
from services.user_management import default_user_management


class AdminView:
    def __init__(self,
                 root,
                 main_view,
                 counselor_view,
                 admin_view,
                 dummy_data,
                 user_management=default_user_management):

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
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root, padx=50, pady=50)
        self.nav_buttons_frame = ttk.LabelFrame(
            master=self._frame, text="Navigation buttons")
        self.treeview_frame = ttk.LabelFrame(
            master=self._frame, text="Submitted contacts")
        self.textview_frame = ttk.LabelFrame(
            master=self._frame, text="Preview selected contact")
        self.contact_management_frame = ttk.LabelFrame(
            master=self._frame, text="Manage selected contact")

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
        button_logout = ttk.Button(
            master=selected_frame,
            text="Logout",
            command=self._main_view
        )

        button_counselor = ttk.Button(
            master=selected_frame,
            text="Counselor view",
            command=self._counselor_view
        )

        button_admin_stuff = ttk.Button(
            master=selected_frame,
            text="Create dummy data",
            command=self._create_dummy_data
        )

        button_counselor.grid(row=0, column=0,
                              padx=10, pady=5,
                              sticky=constants.W)

        button_admin_stuff.grid(row=0, column=1,
                                padx=20,
                                sticky=constants.W)
        button_logout.grid(row=0, column=2,
                           padx=10, pady=5,
                           sticky=constants.E)

    def _init_treeview(self, selected_frame):
        columns = ("rowid", "username", "date_and_time",
                   "channel", "type", "delete")
        self.treeview = ttk.Treeview(
            master=selected_frame,
            columns=columns,
            show="headings",
            selectmode="browse")
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

        self.treeview.grid(row=0, column=0, sticky=constants.NSEW)
        scrollbar = ttk.Scrollbar(
            master=self.treeview_frame, orient=constants.VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=0, column=1, sticky=constants.NS)
        self.treeview.bind("<Return>", self._mark_keybind)
        self.treeview.bind("<Delete>", self._delete_keybind)

    def _init_textfield(self, selected_frame):
        printout = "Choose contact to view more details and options."
        textfield = Text(master=selected_frame, wrap="word")
        textfield.grid(row=3, column=0)
        textfield.insert(1.0, printout)
        textfield["state"] = "disabled"

    def item_selected(self, event):
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
        textfield = Text(master=self.textview_frame, wrap="word")
        textfield.grid(row=3, column=0)
        textfield.insert(1.0, printout)
        textfield["state"] = "disabled"
        if contact[-1] == "TRUE":
            manage_text = "Unmark contact"
        else:
            manage_text = "Mark contact for deletion"
        self._insert_contact_buttons(manage_text)

    def clear_frame(self, frame: ttk.LabelFrame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    
    def _insert_contact_buttons(self, manage_text):
        self.clear_frame(self.contact_management_frame)
        selected = self.treeview.focus()
        selected_item = self.treeview.item(selected, "values")

        button_mark_contact = ttk.Button(
            master=self.contact_management_frame,
            text=manage_text,
            command=lambda: self._mark_contact_for_deletion(selected_item[0])
        )

        button_delete = ttk.Button(
            master=self.contact_management_frame,
            text="Delete selected",
            command=self._delete_marked_contacts
        )

        button_mark_contact.grid(row=0, column=0,
                                 padx=10, pady=5,
                                 sticky=constants.E)

        button_delete.grid(row=0, column=1,
                           padx=10, pady=5,
                           sticky=constants.E)

    def _populate_treeview(self, treeview):
        contacts = self._contact_management.fetch_treeview_contact_info()
        for contact in contacts:
            treeview.insert('', constants.END, values=contact)

    def _delete_contact(self, c_id):
        self._contact_management.delete_contact(c_id)

    def _mark_keybind(self, event):
        item = self.treeview.identify_row(event.y)
        if item: 
            selected_item = self.treeview.item(item, 'values')
            self._mark_contact_for_deletion(selected_item[0])

    def _delete_keybind(self, event):
        item = self.treeview.identify_row(event.y)
        if item:
            self._delete_marked_contacts()

    
    def _mark_contact_for_deletion(self, c_id):
        selected = self.treeview.focus()
        selected_item = list(self.treeview.item(selected, "values"))
        if selected_item[-1] == "":
            selected_item[-1] = "TRUE"
        else:
            selected_item[-1] = ""
        updated_selected = tuple(selected_item)
        self.treeview.item(selected, text="", values=(updated_selected))
        self._contact_management.mark_contact_for_deletion(c_id, selected_item[-1])

    def _delete_marked_contacts(self):
        self._contact_management.delete_marked_contacts()
        for row in self.treeview.get_children():
            if self.treeview.item(row)["values"][-1] == "TRUE":
                self.treeview.delete(row)
                
                


    def _init_contact_management_buttons(self, selected_frame):
        button_mark_contact = ttk.Button(
            master=selected_frame,
            text="Mark contact for deletion",
            state="disabled"
        )

        button_delete = ttk.Button(
            master=selected_frame,
            text="Delete selected",
            state="disabled"
        )

        button_mark_contact.grid(row=0, column=0,
                                 padx=10, pady=5,
                                 sticky=constants.E)

        button_delete.grid(row=0, column=1,
                           padx=10, pady=5,
                           sticky=constants.E)

    # REFACTORED CODE - REMOVE WHEN NOT NEEDED ANYMORE
    # def _fetch_contacts(self):

        # contacts = self._contact_management.fetch_all_contacts()
        # buttons = {}
        # fields = {}
        # if contacts:
        #     for c_id in contacts:
        #         parts = contacts[c_id].split(";")
        #         printout = (f"Username: {str(parts[0])}\n")
        #         printout += "date and time: " + str(parts[1]) + "\n"
        #         printout += "channel: " + str(parts[2])
        #         printout += ", type: " + str(parts[3])
        #         n = len(printout) // 100 + 3
        #         if parts[4] != "None":
        #             printout += ", gender: " + str(parts[4])
        #             printout += ", age: " + str(parts[5])
        #             printout += "\n\n" + "content:\n"
        #             printout += str(parts[6])
        #             n = len(printout) // 100 + 5

        #         fields[c_id] = Text(
        #             master=self._frame, width=100, height=n, wrap="word"
        #         )
        #         fields[c_id].insert(1.0, printout)
        #         fields[c_id]["state"] = "disabled"
        #         # labels[c_id] = ttk.Label(
        #         #     master=self._frame, text=printout, background="white")

        #         def button_action(x=c_id):
        #             return self._delete_contact(x)
        #         buttons[c_id] = ttk.Button(
        #             master=self._frame,
        #             text=f"Delete {c_id}",
        #             command=button_action
        #         )
        #         fields[c_id].grid(row=c_id+10, column=1,
        #                           pady=5, padx=5, sticky=constants.W)
        #         # labels[c_id].grid(row=c_id+10, column=1,
        #         #   pady=5, padx=5, sticky=constants.W)
        #         buttons[c_id].grid(row=c_id+10, column=2,
        #                            pady=5, padx=5, sticky=constants.E)

        # return

        # DELETED FROM TREEVIEW - DELETE WHEN NOT NEEDED
        # for selected_item in self.treeview.selection():
        #     # Check if this line is needed, delete if not
        #     item = self.treeview.item(selected_item)
        #     def delete_contact():
        #         for selected_item in self.treeview.selection():
        #             item = self.treeview.item(selected_item)
        #             contact_id = int(item["values"][0])
        #             self._delete_contact(contact_id)
        #             self.treeview.delete(selected_item)

        #     def mark_contact():
        #         for selected_item in self.treeview.selection():
        #             item = self.treeview.item(selected_item)
        #             contact_id = int(item["values"][0])
        #             self._mark_contact_for_deletion(contact_id)
        #             edited_item = (selected_item[:-1], )
        #             self.treeview.item(selected_item, )
