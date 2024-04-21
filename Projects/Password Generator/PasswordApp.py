import tkinter as tk
import string
import secrets

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        password_label.config(text="Error: Please enter a valid positive integer for password length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry('400x150')
root.resizable(False,False)

label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_label = tk.Label(root, text="")
password_label.pack(pady=5)

root.mainloop()