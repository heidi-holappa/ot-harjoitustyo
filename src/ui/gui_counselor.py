from tkinter import ttk, constants, Frame, StringVar, IntVar, Radiobutton, Text
from services.contact_management import ContactManagement
from services.user_management import default_user_management


class CounselorView:
    def __init__(self, root,
                 main_view,
                 admin_view,
                 user_management=default_user_management):
        self._root = root
        self._main_view = main_view
        self._admin_view = admin_view
        self._frame = None

        self._content_var = None
        self._content_field = None

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

        self.label_and_navigation(0, 0)

        self.init_channel(2, 0)
        self.init_type(7, 0)
        self.init_gender(2, 1)
        self.init_age(8, 1)

        self.init_content(16, 0)

        self.submit(18, 1)

    def label_and_navigation(self, r, c):
        label = ttk.Label(
            master=self._frame, text="You are now in the Counselor View")

        button_logout = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._main_view
        )

        if self._user_management.get_active_user_role() == "admin":
            button_admin_view = ttk.Button(
                master=self._frame,
                text="Admin view",
                command=self._admin_view
            )
            button_admin_view.grid(row=r, column=c+2,
                                   padx=10, pady=5,
                                   sticky=constants.E)

        label.grid(row=r, column=c, pady=5, sticky=constants.W)
        button_logout.grid(row=r, column=c+1,
                           padx=10, pady=5,
                           sticky=constants.E)

    def init_channel(self, r, c):
        # Select channel
        self._channel_var = IntVar()
        channel_label = ttk.Label(
            master=self._frame, text="Select channel")
        channel_R1 = Radiobutton(
            self._frame, text="phone", variable=self._channel_var, value=1)
        channel_R2 = Radiobutton(
            self._frame, text="chat", variable=self._channel_var, value=2)
        channel_R3 = Radiobutton(
            self._frame, text="e-letter", variable=self._channel_var, value=3)

        channel_label.grid(row=r, column=c, sticky=constants.W)
        channel_R1.grid(row=r+1, column=c, sticky=constants.W)
        channel_R2.grid(row=r+2, column=c, sticky=constants.W)
        channel_R3.grid(row=r+3, column=c, sticky=constants.W)

    def init_type(self, r, c):
        # Select type
        self._type_var = IntVar()
        type_label = ttk.Label(
            master=self._frame, text="Select type")
        type_R1 = Radiobutton(self._frame, text="counseling",
                              variable=self._type_var, value=1)
        type_R2 = Radiobutton(
            self._frame, text="non-counseling", variable=self._type_var, value=2)
        type_R3 = Radiobutton(self._frame, text="silent",
                              variable=self._type_var, value=3)
        type_R4 = Radiobutton(
            self._frame, text="non-target group", variable=self._type_var, value=4)

        type_label.grid(row=r, column=c, sticky=constants.W)
        type_R1.grid(row=r+1, column=c, sticky=constants.W)
        type_R2.grid(row=r+2, column=c, sticky=constants.W)
        type_R3.grid(row=r+3, column=c, sticky=constants.W)
        type_R4.grid(row=r+4, column=c, sticky=constants.W)

    def init_gender(self, r, c):
        self._gender_var = IntVar()
        gender_label = ttk.Label(
            master=self._frame, text="Select gender")
        gender_R1 = Radiobutton(self._frame, text="girl",
                                variable=self._gender_var, value=1)
        gender_R2 = Radiobutton(self._frame, text="boy",
                                variable=self._gender_var, value=2)
        gender_R3 = Radiobutton(
            self._frame, text="something else", variable=self._gender_var, value=3)
        gender_R4 = Radiobutton(
            self._frame, text="unknown", variable=self._gender_var, value=4)

        gender_label.grid(row=r, column=c, sticky=constants.W)
        gender_R1.grid(row=r+1, column=c, sticky=constants.W)
        gender_R2.grid(row=r+2, column=c, sticky=constants.W)
        gender_R3.grid(row=r+3, column=c, sticky=constants.W)
        gender_R4.grid(row=r+4, column=c, sticky=constants.W)

    def init_age(self, r, c):
        self._age_var = IntVar()
        age_label = ttk.Label(
            master=self._frame, text="Select age")
        age_R1 = Radiobutton(self._frame, text="under 9",
                             variable=self._age_var, value=1)
        age_R2 = Radiobutton(self._frame, text="9-11",
                             variable=self._age_var, value=2)
        age_R3 = Radiobutton(self._frame, text="12-14",
                             variable=self._age_var, value=3)
        age_R4 = Radiobutton(self._frame, text="15-17",
                             variable=self._age_var, value=4)
        age_R5 = Radiobutton(self._frame, text="18-21",
                             variable=self._age_var, value=5)
        age_R6 = Radiobutton(self._frame, text="22-25",
                             variable=self._age_var, value=6)
        age_R7 = Radiobutton(self._frame, text="over 25",
                             variable=self._age_var, value=7)

        age_label.grid(row=r, column=c, sticky=constants.W)
        age_R1.grid(row=r+1, column=c, sticky=constants.W)
        age_R2.grid(row=r+2, column=c, sticky=constants.W)
        age_R3.grid(row=r+3, column=c, sticky=constants.W)
        age_R4.grid(row=r+4, column=c, sticky=constants.W)
        age_R5.grid(row=r+5, column=c, sticky=constants.W)
        age_R6.grid(row=r+6, column=c, sticky=constants.W)
        age_R7.grid(row=r+7, column=c, sticky=constants.W)

    def init_content(self, r, c):
        self._content_var = StringVar()
        content_label = ttk.Label(
            master=self._frame, text="Write a summary of the contact")
        self._content_field = Text(self._frame, height=5, width=52)
        content_label.grid(row=r, column=c, pady=10, sticky=constants.W)
        self._content_field.grid(row=r+1, column=c, sticky=constants.W)

    def submit(self, r, c):
        button_submit = ttk.Button(
            master=self._frame,
            text="Submit",
            command=self._try_submit
        )
        button_submit.grid(row=r, column=c, sticky=constants.E, padx=20)

    def _try_submit(self):
        if self._content_field:
            input = self._content_field.get(1.0, constants.END)
            input = input.strip()
            self._content_field.delete(1.0, constants.END)
        else:
            input = ""

        # MANAGE CONTACT SUBMISSION

        c_channel = self._channel_var.get()
        c_type = self._type_var.get()
        c_age = self._age_var.get()
        c_gender = self._gender_var.get()
        submission_status = self._contact_management.manage_new_contact_submission(
            c_channel, c_type, c_age, c_gender, input)
        if submission_status[0]:
            label_success = ttk.Label(
                master=self._frame, text="Contact stored successfully.", foreground="green")
            label_success.grid(row=1, column=0, columnspan=4)
            label_success.after(3000, lambda: label_success.destroy())
            self._channel_var.set(0)
            self._type_var.set(0)
            self._gender_var.set(0)
            self._age_var.set(0)
        else:
            label_success = ttk.Label(
                master=self._frame, text=submission_status[1], foreground="red")
            label_success.grid(row=1, column=0, columnspan=4)
            label_success.after(3000, lambda: label_success.destroy())
