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
        label = ttk.Label(
            master=self._frame, text="You are now in the Admin View")
        label.grid(row=0, column=0, pady=5, sticky=constants.W)

        self._init_buttons(0)
        
        self._init_treeview()
        self._populate_treeview(self.treeview)

        self.treeview.bind('<<TreeviewSelect>>', self.item_selected)

    def _init_buttons(self, set_row = 0):
        button_logout = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._main_view
        )

        button_counselor = ttk.Button(
            master=self._frame,
            text="Counselor view",
            command=self._counselor_view
        )

        button_admin_stuff = ttk.Button(
            master=self._frame,
            text="Create dummy data",
            command=self._create_dummy_data
        )


        button_admin_stuff.grid(row=0, column=0,
                                padx=20,
                                sticky=constants.E)
        button_counselor.grid(row=0, column=1,
                              padx=10, pady=5,
                              sticky=constants.E)
        button_logout.grid(row=0, column=2,
                           padx=10, pady=5,
                           sticky=constants.E)

    def _init_treeview(self):
        columns = ("username", "date_and_time", "channel",
                   "type", "gender", "age", "content")
        self.treeview = ttk.Treeview(
            master=self._frame, columns=columns, show="headings")
        self.treeview.heading("username", text="username")
        self.treeview.heading("date_and_time", text="date and time")
        self.treeview.heading("channel", text="channel")
        self.treeview.heading("type", text="type")
        self.treeview.heading("gender", text="gender")
        self.treeview.heading("age", text="age")
        self.treeview.heading("content", text="content")

        self.treeview.grid(row=2, column=0, sticky=constants.NSEW)
        scrollbar = ttk.Scrollbar(
            master=self._frame, orient=constants.VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=2, column=1, sticky='ns')

    def item_selected(self, event):
        '''insert selected row into a Text widget'''
        printout = ""
        for selected_item in self.treeview.selection():
            item = self.treeview.item(selected_item)
            parts = item["values"]
            printout = (f"Username: {str(parts[0])}\n")
            printout += "date and time: " + str(parts[1]) + "\n"
            printout += "channel: " + str(parts[2])
            printout += ", type: " + str(parts[3])
            n = len(printout) // 100 + 3
            if parts[4] != "None":
                printout += ", gender: " + str(parts[4])
                printout += ", age: " + str(parts[5])
                printout += "\n\n" + "content:\n"
                printout += str(parts[6])
                n = len(printout) // 100 + 5
        textfield = Text(master=self._frame, wrap="word")
        textfield.grid(row=3, column=0)
        textfield.insert(1.0, printout)
        textfield["state"] = "disabled"
        print(printout)

    def _populate_treeview(self, treeview):
        contacts = self._contact_management.fetch_all_contacts_as_tuples()
        for contact in contacts:
            treeview.insert('', constants.END, values=contact)

    def _delete_contact(self, c_id):
        print("Now in delete_contact - method. Contact-id: ", c_id)
        self._contact_management.delete_contact(c_id)
        self._admin_view


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