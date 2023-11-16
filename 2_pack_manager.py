import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self):
        super().__init__()

        self.title("Pack Manager")
        self.geometry("500x450")

        self.label_1 = tb.Label(self, text="Box 1", padding=20, bootstyle=(INVERSE, PRIMARY))
        self.label_2 = tb.Label(self, text="Box 2", padding=20, bootstyle=(INVERSE, DANGER))
        self.label_3 = tb.Label(self, text="Box 3", padding=20, bootstyle=(INVERSE, WARNING))

        # The most common options of the pack manager are as follows: side, expand, fill, anchor, padx, pady
        # Side deals with what side to start packing from
        # self.label_1.pack(side=BOTTOM)
        # self.label_2.pack(side=BOTTOM)
        # self.label_3.pack(side=RIGHT)

        # Expand tells the pack manager to use all available space to place the widget
        # self.label_1.pack(expand=True)
        # self.label_2.pack()
        # self.label_3.pack()

        # While expand deals with using the available space to place the objectm
        # Fill tells the pack manager to use the available space to actually expand the object itself
        # Options include fill x, fill y, and both
        # self.label_1.pack(fill=X)
        # self.label_2.pack()
        # self.label_3.pack(expand=True, fill=Y)

        # Anchor tells the pack manager to place the object closer to the cardinal direction
        # Options N, S, W, E, NW, NE, SW, SE
        self.label_1.pack(fill=X, anchor=E)
        self.label_2.pack()
        self.label_3.pack(expand=True, fill=Y, anchor=W)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
