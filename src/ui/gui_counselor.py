from tkinter import ttk, constants


class CounselorView:
    def __init__(self, root, main_view):
        self._root = root
        self._main_view = main_view
        self._frame = None

        self._initialize()

    def pack(self):
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame, text="You are now in the Counselor View")

    
        button_logout = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._main_view
        )

        label.grid(row=0, column=1)
        button_logout.grid(row=1, column=1)
        
