import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self, theme):
        super().__init__(themename=theme)

        self.geometry("400x200")

        self.button = tb.Button(self, text="Cancel", bootstyle=(DANGER, OUTLINE))
        self.button_two = tb.Button(self, text="Submit", bootstyle=SUCCESS)

        self.button.pack(padx=5, pady=10, side=LEFT)
        self.button_two.pack(padx=5, pady=10, side=BOTTOM)


if __name__ == '__main__':
    app = App(theme="vapor")
    app.place_window_center()
    app.mainloop()
