from tkinter import Tk, ttk

class setTheme:

    def __init__(self, root):
        self._root = root
        self.app_style = ttk.Style(root)
        self.app_style.theme_use("clam")
        
        self.set_default_style()
        

    def set_default_style(self):

        self._root.option_add('*Dialog.msg.font', 'Calibri 10')

        self.app_style.configure('Custom.TFrame',
                                    background="grey95",
                                    foreground="black")

        self.app_style.configure('Custom.TLabelframe',
                                    background="grey95",
                                    foreground="black")

        self.app_style.configure('TLabelframe.Label',
                                    background="grey95",
                                    foreground="black")

        self.app_style.configure('Custom.TButton',
                                    background="grey95",
                                    foreground="black",
                                    focuscolor="grey48",
                                    font='Calibri 10 bold')

        self.app_style.map('TButton', background=[("active", "grey78")])

        self.app_style.configure('Custom.TLabel',
                                    background="grey95",
                                    foreground="grey12",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Centered.TLabel',
                                    background="grey95",
                                    foreground="grey12",
                                    justify="center",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Success.TLabel',
                                    background="grey95",
                                    foreground="green",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Error.TLabel',
                                    background="grey95",
                                    foreground="red",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Header1.TLabel',
                                    background="grey95",
                                    foreground="black",
                                    font='Cambria 14 bold')

        self.app_style.configure('Custom.TEntry',
                                    background="grey95",
                                    foreground="black",
                                    font='Calibri 10')

        self.app_style.configure('Custom.TCheckbutton',
                                    background="grey95",
                                    foreground="black")
        self.app_style.map('TCheckbutton', background=[("disabled", "grey95")])

        self.app_style.configure('Custom.TRadiobutton',
                                    background="grey95",
                                    foreground="black",
                                    font='Calibri 10')

        self.app_style.map('TRadiobutton', background=[("disabled", "grey95")])

        self.app_style.configure('Custom.Treeview',
                                    background="white",
                                    foreground="black",
                                    font='Calibri 10')

        self.app_style.configure('Vertical.TScrollbar',
                                    background="grey95",
                                    foreground="black")

        # TEST BUILDING DARK MODE HERE
        # ADD SELECTION TO LOGIN AS A FIRST STEP
    def set_dark_mode(self):
        self._root.option_add('*Dialog.msg.font', 'Calibri 10')

        self.app_style.configure('Custom.TFrame',
                                    background="grey14",
                                    foreground="grey95")

        self.app_style.configure('Custom.TLabelframe',
                                    background="grey14",
                                    foreground="grey95")

        self.app_style.configure('TLabelframe.Label',
                                    background="grey14",
                                    foreground="grey95")

        self.app_style.configure('Custom.TButton',
                                    background="grey14",
                                    foreground="grey95",
                                    focuscolor="grey48",
                                    font='Calibri 10 bold')

        self.app_style.map('TButton', background=[("active", "grey78")])

        self.app_style.configure('Custom.TLabel',
                                    background="grey14",
                                    foreground="grey95",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Centered.TLabel',
                                    background="grey14",
                                    foreground="grey95",
                                    justify="center",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Success.TLabel',
                                    background="grey14",
                                    foreground="green",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Error.TLabel',
                                    background="grey14",
                                    foreground="red",
                                    font='Calibri 10 bold',
                                    wraplength=400)

        self.app_style.configure('Header1.TLabel',
                                    background="grey14",
                                    foreground="grey95",
                                    font='Cambria 14 bold')

        self.app_style.configure('Custom.TEntry',
                                    background="grey14",
                                    foreground="grey95",
                                    font='Calibri 10')

        self.app_style.configure('Custom.TCheckbutton',
                                    background="grey14",
                                    foreground="grey95")
        self.app_style.map('TCheckbutton', background=[("disabled", "grey14")])

        self.app_style.configure('Custom.TRadiobutton',
                                    background="grey14",
                                    foreground="grey95",
                                    font='Calibri 10')

        self.app_style.map('TRadiobutton', background=[("disabled", "grey14")])

        self.app_style.configure('Custom.Treeview',
                                    background="grey14",
                                    foreground="grey95",
                                    font='Calibri 10')

        self.app_style.configure('Vertical.TScrollbar',
                                    background="grey14",
                                    foreground="grey95")