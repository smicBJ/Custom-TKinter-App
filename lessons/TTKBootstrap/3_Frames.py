from pathlib import Path
import ttkbootstrap as tb
from ttkbootstrap.constants import *

PATH = Path(__file__).parent / "assets/images"


class SideBar(tb.Frame):

    def __init__(self, master, nav_call):
        super().__init__(master, padding=10, bootstyle=SECONDARY)
        self.pack(side=LEFT, fill=Y)

        # self.label = tb.Label(self, image="logo", width=10)
        # self.label.pack(fill=X, pady=(0, 10))

        self.home_button = tb.Button(self, text="Home", width=10, command=lambda: nav_call("home"))
        self.home_button.pack(pady=(0, 10))

        self.search_button = tb.Button(self, text="Search", width=10, command=lambda: nav_call("search"))
        self.search_button.pack(pady=(0, 10))


class HomeFrame(tb.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))

        self.label = tb.Label(self, image="logo", width=10)
        self.label.pack(fill=X, pady=(0, 10))

        header_text = "Welcome to the Athletic and Academic Records App"
        header = tb.Label(master=self, text=header_text, width=50)
        header.pack(fill=X, pady=10)


class SearchForm(tb.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))

        self.name = tb.StringVar(value="")

        header_text = "Search Student Academic Records"
        header = tb.Label(master=self, text=header_text, width=50)
        header.pack(fill=X, pady=10)

        container = tb.Frame(self)
        container.pack(fill=X, expand=True, pady=5)

        self.label = tb.Label(container, text="No search results")
        self.label.pack(side=LEFT, pady=30)

        self.create_form_entry("name", self.name)
        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        container = tb.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = tb.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = tb.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        container = tb.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = tb.Button(master=container, text="Submit", command=self.on_submit, bootstyle=SUCCESS)
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = tb.Button(master=container, text="Cancel", command=self.on_cancel, bootstyle=DANGER)
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        print("Name:", self.name.get())

    def on_cancel(self):
        self.quit()


class App(tb.Window):

    def __init__(self):
        super().__init__("Academic Classes", "lumen", iconphoto=PATH / "logor.png")

        self.geometry("640x480")

        self.current_frame = ""
        self.images = [
            tb.PhotoImage(name="logo", file=PATH / "logo.png"),
            tb.PhotoImage(name="logo32", file=PATH / "logo32.png")
        ]

        self.side_bar = SideBar(self, nav_call=self.change_frame)

        self.container = tb.Frame(self)
        self.container.pack(side=LEFT, anchor=N)

        # Setup Frames
        self.frames = {
            "home": HomeFrame(self.container),
            "search": SearchForm(self.container)
        }

        self.set_frame("home")

    def change_frame(self, next_frame):
        self.remove_frame()
        self.set_frame(next_frame)

    def set_frame(self, name):
        self.current_frame = name
        self.frames[name].pack(side=LEFT, anchor=N)

    def remove_frame(self):
        self.frames[self.current_frame].pack_forget()


if __name__ == "__main__":
    app = App()
    app.place_window_center()
    app.mainloop()
