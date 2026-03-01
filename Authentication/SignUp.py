import tkinter as tk
import Login as login
import DataBase
from tkinter import messagebox

def start_app():
    def sign_up():
        DataBase.create_new_user(user_name_input.get(), pass_input.get())

    root = tk.Tk()
    root.title("SignUp")
    root.geometry("400x400")

    label = tk.Label(root, text="Please Enter Account", font=("Arial", 14))
    label.pack(pady=20)

    user_name_label = tk.Label(root, text="Username", font=("Arial", 14))
    user_name_label.pack()

    user_name_input = tk.Entry(root)
    user_name_input.pack()

    pass_label = tk.Label(root, text="Password", font=("Arial", 14))
    pass_label.pack()

    pass_input = tk.Entry(root)
    pass_input.pack()

    sign_up_btn = tk.Button(root, text="Sign Up", command=lambda: sign_up())
    sign_up_btn.pack()

    def BackToLogin():
        root.destroy()
        login.start_app()
    


    back_to_login_btn = tk.Button(root, text="Back To Login", command=lambda: BackToLogin())
    back_to_login_btn.pack()

    root.mainloop()
def MessageBox(IsError : bool):
    if IsError:
        messagebox.showinfo("Sign Up Success")
    else:
        messagebox.showerror("Sign Up Failure")

if __name__ == "__main__":
    start_app()