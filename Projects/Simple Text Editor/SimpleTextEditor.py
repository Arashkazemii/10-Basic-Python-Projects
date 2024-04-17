from tkinter import *
import tkinter as tk
from tkinter import filedialog
import random
from tkinter import messagebox

def openFile():
    if len(editor.get('1.0', END)) > 0:
        response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
        if response is None:
            return
        elif response:
            saveFile()
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            editor.delete('1.0', END)
            editor.insert(END, file.read())

def saveFile():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(editor.get('1.0', END))

def newFile():
    if len(editor.get('1.0', END)) > 0:
        response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
        if response is None:
            return
        elif response:
            saveFile()
    editor.delete('1.0', END)


root = tk.Tk()
root.geometry('1280x720')
root.configure(background='#fcf6f5')
root.title("Text Editor")

heading = tk.Label(root, text='Text Editor', font='bold, 20', bg='#fcf6f5', fg='#990011')
heading.pack()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side='right', fill='y')

editor = tk.Text(root, width=400, height=400, bg='white', font=(10), yscrollcommand=scrollbar.set)
editor.pack(fill='both', padx=30, pady=20)

scrollbar.config(command=editor.yview)

saveButton = tk.Button(root, text='Save', fg='#fcf6f5', bg='#990011', command=saveFile)
saveButton.place(x=20, y=10)

openButton = tk.Button(root, text='Open File', fg='#fcf6f5', bg='#990011', command=openFile)
openButton.place(x=67, y=10)

newButton = tk.Button(root, text='New File', fg='#fcf6f5', bg='#990011', command=newFile)
newButton.place(x=140, y=10)

root.mainloop()