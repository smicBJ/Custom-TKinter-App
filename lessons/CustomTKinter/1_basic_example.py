import customtkinter


def greeting():
    print("Hello World!")


app = customtkinter.CTk()
app.geometry("400x250")

button = customtkinter.CTkButton(app, text="Push Me", command=greeting)
button.pack(padx=20, pady=20)

app.mainloop()
