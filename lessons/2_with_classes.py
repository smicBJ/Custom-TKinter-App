import customtkinter as cttk
import requests as req


class App(cttk.CTk):

    def __init__(self):
        super().__init__()
        self.base_url = "http://10.6.21.76:8000"

        self.title("GUI with Classes")
        # To add icon:
        # self.iconbitmap("path/to_icon.ico")
        self.geometry("400x250")

        """
        Options for a button to review:
        text="Push Me"  command=self.greeting   height=50   width=200   font=("Times", 18)  text_color="black"
        fg_color="yellow"   hover_color="orange"    corner_radius=50    bg_color="black"    border_width=2
        border_color="red"  # state="disabled"
        """
        self.button = cttk.CTkButton(self, text="Push Me", command=self.greeting)
        self.entry = cttk.CTkEntry(self, placeholder_text="Search... ")
        self.label = cttk.CTkLabel(self, text="Waiting for update...")

        self.label.pack(pady=15)
        self.entry.pack(pady=(45, 15))
        self.button.pack(pady=(0, 15))

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
