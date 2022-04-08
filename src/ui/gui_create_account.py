from tkinter import ttk, constants

class CreateAccountView:
    def __init__(self, root, main_view):
        self._root = root
        self._main_view = main_view
        self._frame = None

        self._initialize()

    def pack(self):
        if self._frame:
            self._frame.pack(fill=constants.X)

    def destroy(self):
        print("DESTROYING: OMNOMNOMNOMNOM")
        if self._frame:
            self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # self._root.geometry("600x300")
        label = ttk.Label(master=self._frame, text="Create a new account")
        
        button_login = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._main_view
        )

        label.grid(row=0, column=1)
        button_login.grid(row=1, column=1)

