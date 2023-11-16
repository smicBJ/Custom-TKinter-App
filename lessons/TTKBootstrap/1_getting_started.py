import ttkbootstrap as tkb
from ttkbootstrap.constants import *

root = tkb.Window(themename="darkly")

b1 = tkb.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=(30, 5), pady=10)

b2 = tkb.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=(5, 30), pady=10)

root.place_window_center()
root.mainloop()
