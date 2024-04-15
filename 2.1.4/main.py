#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    if(ent_username.get() == "username" and ent_password.get() == "password"):
        frame_auth.tkraise()
    else:
        fail_label = tk.Label(frame_login, text="invalid user/password. Please try again")
        fail_label.pack()

# main window
root = tk.Tk()
root.wm_geometry("500x500")

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

#TODO: Add a label to frame_auth

auth_label = tk.Label(frame_auth, text="")

#TODO: Use get method of ent_password when the button is pressed, and store result

#TODO: Configure the label in frame_auth to display the password

frame_login.tkraise()

lbl_username = tk.Label(frame_login, text="Username")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=180, pady=5)

lbl_password = tk.Label(frame_login, text="Password")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack()




root.mainloop()