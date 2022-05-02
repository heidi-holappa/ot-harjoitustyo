from tkinter import ttk, constants, Frame, StringVar, IntVar, Text, Menu, messagebox
import webbrowser
from services.contact_management import ContactManagement
from services.user_management import default_user_management


class CounselorView:
    """A class that creates an object that constructs the counselor view.

    Attributes:
        root: root component for constructing the view
        main_view: a reference to the method that calls view MainView
        admin_view: a reference to the method that calls view AdminView
        dummy_data: a reference to the method that calls view CreateDummyData
        default_user_management: default service class for user management
    """
    def __init__(self, root,
                 main_view,
                 admin_view,
                 dummy_data_view,
                 user_management=default_user_management):

        """Constructor for initializing an object of the class.

        Args:
            root (Tk): root component for constructing views
            main_view (MainView): a reference to the methong that calls view MainView
            admin_view (AdminView): a reference to the method that calls view AdminView
            dummy_data (CreateDummyData): a reference to the method that calls view CreateDummyData.
            _frame: Frame to be created
            _state: a changing state to indicate if some widgets are disabled
            _content_var: a variable for the content
            _content_field: a variable for the content field
            _contact_management: a service class object for managing contacts. 
            user_management (UserManagement, optional): Service class object for user management.
            Defaults to default_user_management.
        """

        self._root = root
        self._main_view = main_view
        self._admin_view = admin_view
        self._dummy_data_view = dummy_data_view
        self._frame = None
        self._state = "disabled"

        self._content_var = None
        self._content_field = None

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
        print(self._user_management.get_active_user())
        self._frame = Frame(master=self._root,
                            padx=50,
                            pady=50,
                            bg="grey95")

        # self._create_menubar()

        self.label_and_nav_frame = ttk.LabelFrame(
            master=self._frame,
            text="",
            style="Custom.TLabelframe"
        )
        self.channel_and_type_frame = ttk.LabelFrame(
            master=self._frame,
            text="",
            style="Custom.TLabelframe"
        )
        self.age_and_gender_frame = ttk.LabelFrame(
            master=self._frame,
            text="",
            style="Custom.TLabelframe"
        )

        self.content_frame = ttk.LabelFrame(
            master=self._frame,
            text="",
            style="Custom.TLabelframe"
        )

        self.label_and_nav_frame.grid(
            columnspan=2,
            sticky=constants.EW)

        self.channel_and_type_frame.grid(
            row=1,
            column=0,
            sticky=constants.NSEW
        )
        self.age_and_gender_frame.grid(
            row=1,
            column=1,
            sticky=constants.NSEW
        )

        self.content_frame.grid(
            columnspan=2,
            sticky=constants.EW)

        self.label_and_navigation(0, 0)

        self.init_channel(2, 0)
        self.init_type(7, 0)
        self.init_gender(2, 1)
        self.init_age(8, 1)

        self.init_content(16, 0)

        self.init_submit(18, 1)

    # def _create_menubar(self):
    #     menubar = Menu(self._root)
    #     filemenu = Menu(menubar, tearoff=0)
    #     filemenu.add_command(label="Logout", command=self._main_view)
    #     filemenu.add_separator()
    #     filemenu.add_command(label="Exit", command=self.exit)
    #     menubar.add_cascade(label="File", menu=filemenu)

    #     if self._user_management.get_active_user_role() == "admin":
    #         adminmenu = Menu(menubar, tearoff=0)
    #         adminmenu.add_command(label="Manage submission", command=self._admin_view)
    #         adminmenu.add_command(label="Create dummy content", command=self._dummy_data_view)
    #         menubar.add_cascade(label="Admin", menu=adminmenu)

    #     helpmenu = Menu(menubar, tearoff=0)
    #     helpmenu.add_command(label="Help (opens browser)", command=self._open_help)
    #     helpmenu.add_command(label="About", command=self._show_about)
    #     menubar.add_cascade(label="Help", menu=helpmenu)
    #     self._root.config(menu=menubar)

    # def donothing(self):
    #     pass

    # def exit(self):
    #     self._root.destroy()

    def label_and_navigation(self, r: int, c: int):
        """A method that creates the heading label and navigation buttons for the view

        Args:
            r (int): starting row
            c (int): starting column
        """
        label = ttk.Label(
            master=self.label_and_nav_frame,
            text="You are now in the Counselor View",
            style="Header1.TLabel"
        )

        button_logout = ttk.Button(
            master=self.label_and_nav_frame,
            text="Logout",
            command=self._main_view,
            style="Custom.TButton"
        )

        if self._user_management.get_active_user_role() == "admin":
            button_admin_view = ttk.Button(
                master=self.label_and_nav_frame,
                text="Admin view",
                command=self._admin_view,
                style="Custom.TButton"
            )
            button_admin_view.grid(row=r, column=c+2,
                                   padx=10, pady=5,
                                   sticky=constants.E)

        label.grid(row=r, column=c, pady=5, sticky=constants.W)
        button_logout.grid(row=r, column=c+1,
                           padx=10, pady=5,
                           sticky=constants.E)

    def init_channel(self, r: int, c: int):
        """A method for creating the channel selection

        Args:
            r (int): starting row
            c (int): starting column
        """
        # Select channel
        self._channel_var = IntVar()
        channel_label = ttk.Label(
            master=self.channel_and_type_frame,
            text="Select channel",
            style="Custom.TLabel"
        )
        channel_R1 = ttk.Radiobutton(
            self.channel_and_type_frame,
            text="phone",
            variable=self._channel_var,
            value=1,
            style="Custom.TRadiobutton"
        )
        channel_R2 = ttk.Radiobutton(
            self.channel_and_type_frame,
            text="chat",
            variable=self._channel_var,
            value=2,
            style="Custom.TRadiobutton")
        channel_R3 = ttk.Radiobutton(
            self.channel_and_type_frame,
            text="e-letter",
            variable=self._channel_var,
            value=3,
            style="Custom.TRadiobutton")

        channel_label.grid(row=r, column=c, sticky=constants.W)
        channel_R1.grid(row=r+1, column=c, sticky=constants.W)
        channel_R2.grid(row=r+2, column=c, sticky=constants.W)
        channel_R3.grid(row=r+3, column=c, sticky=constants.W)

    def init_type(self, r: int, c: int):
        """A method for creating the type selection

        Args:
            r (int): starting row
            c (int): starting column
        """
        # Select type
        self._type_var = IntVar()
        type_label = ttk.Label(
            master=self.channel_and_type_frame,
            text="Select type",
            style="Custom.TLabel")
        type_R1 = ttk.Radiobutton(self.channel_and_type_frame,
                                  text="counseling",
                                  variable=self._type_var,
                                  value=1,
                                  style="Custom.TRadiobutton",
                                  command=self._change_state)
        type_R2 = ttk.Radiobutton(
            self.channel_and_type_frame,
            text="non-counseling",
            variable=self._type_var,
            value=2,
            style="Custom.TRadiobutton",
            command=self._change_state)
        type_R3 = ttk.Radiobutton(
            self.channel_and_type_frame,
            text="silent",
            variable=self._type_var,
            value=3,
            style="Custom.TRadiobutton",
            command=self._change_state)
        type_R4 = ttk.Radiobutton(
            self.channel_and_type_frame,
            text="non-target group",
            variable=self._type_var,
            value=4,
            style="Custom.TRadiobutton",
            command=self._change_state)

        type_label.grid(row=r, column=c, sticky=constants.W)
        type_R1.grid(row=r+1, column=c, sticky=constants.W)
        type_R2.grid(row=r+2, column=c, sticky=constants.W)
        type_R3.grid(row=r+3, column=c, sticky=constants.W)
        type_R4.grid(row=r+4, column=c, sticky=constants.W)

    def init_gender(self, r: int, c: int):
        """A method for creating the gender selection

        Args:
            r (int): starting row
            c (int): starting column 
        """
        self._gender_var = IntVar()
        gender_label = ttk.Label(
            master=self.age_and_gender_frame,
            text="Select gender",
            style="Custom.TLabel")
        gender_R1 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="girl",
            variable=self._gender_var,
            value=1,
            style="Custom.TRadiobutton",
            state=self._state)
        gender_R2 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="boy",
            variable=self._gender_var,
            value=2,
            style="Custom.TRadiobutton",
            state=self._state)
        gender_R3 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="something else",
            variable=self._gender_var,
            value=3,
            style="Custom.TRadiobutton",
            state=self._state)
        gender_R4 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="unknown",
            variable=self._gender_var,
            value=4,
            style="Custom.TRadiobutton",
            state=self._state)

        gender_label.grid(row=r, column=c, sticky=constants.W)
        gender_R1.grid(row=r+1, column=c, sticky=constants.W)
        gender_R2.grid(row=r+2, column=c, sticky=constants.W)
        gender_R3.grid(row=r+3, column=c, sticky=constants.W)
        gender_R4.grid(row=r+4, column=c, sticky=constants.W)

    def init_age(self, r: int, c: int):
        """A method for creating the age selection

        Args:
            r (int): starting row
            c (int): starting column
        """
        self._age_var = IntVar()
        age_label = ttk.Label(
            master=self.age_and_gender_frame,
            text="Select age",
            style="Custom.TLabel")
        age_R1 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="under 9",
            variable=self._age_var,
            value=1,
            style="Custom.TRadiobutton",
            state=self._state)
        age_R2 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="9-11",
            variable=self._age_var,
            value=2,
            style="Custom.TRadiobutton",
            state=self._state)
        age_R3 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="12-14",
            variable=self._age_var,
            value=3,
            style="Custom.TRadiobutton",
            state=self._state)
        age_R4 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="15-17",
            variable=self._age_var,
            value=4,
            style="Custom.TRadiobutton",
            state=self._state)
        age_R5 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="18-21",
            variable=self._age_var,
            value=5,
            style="Custom.TRadiobutton",
            state=self._state)
        age_R6 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="22-25",
            variable=self._age_var,
            value=6,
            style="Custom.TRadiobutton",
            state=self._state)
        age_R7 = ttk.Radiobutton(
            self.age_and_gender_frame,
            text="over 25",
            variable=self._age_var,
            value=7,
            style="Custom.TRadiobutton",
            state=self._state)

        age_label.grid(row=r, column=c, sticky=constants.W)
        age_R1.grid(row=r+1, column=c, sticky=constants.W)
        age_R2.grid(row=r+2, column=c, sticky=constants.W)
        age_R3.grid(row=r+3, column=c, sticky=constants.W)
        age_R4.grid(row=r+4, column=c, sticky=constants.W)
        age_R5.grid(row=r+5, column=c, sticky=constants.W)
        age_R6.grid(row=r+6, column=c, sticky=constants.W)
        age_R7.grid(row=r+7, column=c, sticky=constants.W)

    def init_content(self, r: int, c: int):
        """A method for creating the content submission area

        Args:
            r (int): starting row
            c (int): starting column
        """
        self._content_var = StringVar()
        content_label = ttk.Label(
            master=self.content_frame,
            text="Write a summary of the contact",
            style="Custom.TLabel"
        )
        self._content_field = Text(
            self.content_frame,
            height=5,
            width=52,
            bg="white",
            font="calibri 10"
        )
        if self._state == "disabled":
            default_printout = "Content is written only for counseling contacts."
            self._content_field.insert(1.0, default_printout)
            self._content_field.configure(state="disabled", bg="grey88")
        else:
            self._content_field.configure(state="normal", bg="white")
        content_label.grid(row=r, column=c, pady=10, sticky=constants.EW)
        self._content_field.grid(row=r+1, column=c, sticky=constants.EW)

    def init_submit(self, r: int, c: int):
        """Generates a button for submitting the contact

        Args:
            r (int): row position
            c (int): column position
        """
        button_submit = ttk.Button(
            master=self.content_frame,
            text="Submit",
            command=self._try_submit,
            style="Custom.TButton"
        )
        button_submit.grid(row=r, column=c, sticky=constants.E, padx=20)

    def _try_submit(self):
        """A method that initiaties contact submission.

        Submission is validated. If validation fails, an error messagebox is shown

        If submission succeeds a messagebox informing of success is shown. 
        """
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
            # label_success = ttk.Label(
            #     master=self._frame,
            #     text="Contact stored successfully.",
            #     style="Success.TLabel"
            # )
            # label_success.grid(
            #     row=1,
            #     column=0,
            #     columnspan=4
            # )
            # label_success.after(3000, lambda: label_success.destroy())
            messagebox.showinfo(
                title="Success!",
                message="Contact stored successfully.",
                icon=messagebox.INFO)
            self._channel_var.set(0)
            self._type_var.set(0)
            self._gender_var.set(0)
            self._age_var.set(0)
        else:
            # label_success = ttk.Label(
            #             master=self._frame,
            #             text=submission_status[1],
            #             foreground="red",
            #             style="Error.TLabel")
            # label_success.grid(row=1, column=0, columnspan=4)
            # label_success.after(3000, lambda: label_success.destroy())

            messagebox.showinfo(
                title="Error!",
                message=submission_status[1],
                icon=messagebox.ERROR)

    def _change_state(self):
        """Handles the disabling/enabling of selected widget.

        When _type_var == 1, all widgets are enabled. Otherwise selected
        widgets are disabled. 

        When the state changes, widgets are destroyed and recreated. 
        """
        if self._state == "disabled" and self._type_var.get() != 1:
            return
        if self._state == "disabled" and self._type_var.get() == 1:
            self._state = "normal"
        elif self._type_var.get() != 1:
            self._state = "disabled"
        self.clear_frame(self.age_and_gender_frame)
        self.clear_frame(self.content_frame)
        
        #Repeating code, refactor.
        self.init_gender(2, 1)
        self.init_age(8, 1)
        self.init_content(16, 0)
        self.init_submit(18, 1)

    def clear_frame(self, frame: ttk.LabelFrame):
        """A general method for destroying frame content.

        Args:
            frame (ttk.LabelFrame): A Labelframe for which the widgets are to be destroyed
        """
        for widgets in frame.winfo_children():
            widgets.destroy()

    # def _open_help(self):
    #     webbrowser.open_new("https://github.com/heidi-holappa/ot-harjoitustyo/blob/master/documentation/architecture.md")

    # def _show_about(self):
    #     messagebox.showinfo(
    #         title="About the application",
    #         message="Version 0.1\n\nCreated as a University project in 2022",
    #         icon=messagebox.INFO
    #     )
