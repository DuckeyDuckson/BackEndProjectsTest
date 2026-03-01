import tkinter as tk
import sqlite3
import SignUp
from tkinter import messagebox

def start_app():
    def login():
        # Get values from the UI
        username = user_name_input.get()
        password = pass_input.get()

        # Connect to database
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()

        # Check if user exists (Note: In a real app, hash the password!)
        cursor.execute("SELECT * FROM users WHERE username=? AND password_hash=?", (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Success", f"Welcome back, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        conn.close

    root = tk.Tk()
    root.title("Login")
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

    login_btn = tk.Button(root, text="Login", command=lambda: login())
    login_btn.pack()
    def GoToSignUp():
        root.destroy()
        SignUp.start_app()

    sign_up_btn = tk.Button(root, text="Sign Up", command=lambda : GoToSignUp())
    sign_up_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    start_app()
