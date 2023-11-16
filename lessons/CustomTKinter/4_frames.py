import customtkinter as cttk
import requests as req


class SideBarNav(cttk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.button_1 = cttk.CTkButton(self, text="Academic List")
        self.button_2 = cttk.CTkButton(self, text="Search Academic Record")

        self.button_1.pack(pady=10)
        self.button_2.pack(pady=10)


class Main(cttk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.button = cttk.CTkButton(self, text="Push Me", command=self.greeting)
        self.entry = cttk.CTkEntry(self, placeholder_text="  Search... ")
        self.label = cttk.CTkLabel(self, text="Waiting for update...")

        self.label.pack()
        self.entry.pack()
        self.button.pack()

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


class App(cttk.CTk):

    def __init__(self):
        super().__init__()
        self.base_url = "http://10.6.21.76:8000"

        self.title("Using Frames")
        self.geometry("640x480")

        self.nav_frame = SideBarNav(self)
        self.main_frame = Main(self)

        self.nav_frame.pack(side="left", fill="y")
        self.main_frame.pack(side="left", expand=True, fill="both")


app = App()
app.mainloop()
