from customtkinter import *

app = CTk()
app.geometry("500x500")

set_appearance_mode("dark")

def click_handler():
    print("Button clicked")

user = CTkEntry(master=app, placeholder_text="Your e-mail", width=300, text_color="#fff")

password = CTkEntry(master=app, placeholder_text="Your password", width=300, text_color="#fff")

btn = CTkButton(master=app, text="Login", command=click_handler, corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", border_width=2)

switch = CTkSwitch(master=app, text="Remember Login?")

label = CTkLabel(master=app, text="Create a new account")


# Layouts
user.place(relx=0.5, rely=0.30, anchor="center")

password.place(relx=0.5, rely=0.40, anchor="center")

switch.place(relx=0.5, rely=0.6, anchor="center")

label.place(relx=0.5, rely=0.7, anchor="center")

btn.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()
