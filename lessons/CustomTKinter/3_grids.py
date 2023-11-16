import customtkinter as cttk
import requests as req


class App(cttk.CTk):

    def __init__(self):
        super().__init__()
        self.base_url = "http://10.6.21.76:8000"

        self.title("GUI with Classes")
        self.geometry("400x250")

        # The weight tells you how much of the width/height the row/col should take up
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure((1, 2), weight=1)

        self.button = cttk.CTkButton(self, text="Push Me", command=self.greeting)
        self.entry = cttk.CTkEntry(self, placeholder_text="  Search... ")
        self.label = cttk.CTkLabel(self, text="Waiting for update...")

        # sticky − What to do if the cell is larger than widget. By default, with sticky='',
        # widget is centered in its cell. sticky may be the string concatenation of zero or more of
        # N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the
        # cell to which widget sticks.
        self.button.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        self.entry.grid(row=1, column=0, padx=30, pady=(20, 0), sticky="ew")
        self.label.grid(row=0, column=0, pady=30)

    def greeting(self):
        name = self.entry.get()
        student = self.get_academic_record(name)
        if "msg" in student:
            self.label.configure(text=student["msg"])
        else:
            self.label.configure(text=f"Student {student['name']} has a {student['gpa']} gpa")

    def get_academic_record(self, name):
        url = f"{self.base_url}/academics/{name}"
        res = req.get(url=url)
        return res.json()


app = App()
app.mainloop()
