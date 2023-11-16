import ttkbootstrap as tb

FONT_TITLE = ("Verdana", 38)


class App(tb.Window):

    def __init__(self, theme):
        super().__init__(themename=theme, iconphoto="logor.png")

        self.title("TTK Bootstrap with Classes")
        self.geometry("640x480")

        self.label_1 = tb.Label(text="Hello World!", font=FONT_TITLE)
        self.label_1.pack(pady=40)

        self.button_1 = tb.Button(text="Submit", bootstyle="success, outline", command=self.submit)
        self.button_1.pack(pady=20)

    def submit(self):
        text = self.label_1.cget("text")
        print(text)


app = App(theme="lumen")
app.place_window_center()
app.mainloop()
