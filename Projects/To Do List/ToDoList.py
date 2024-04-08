import tkinter as tk
from tkinter import font

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_label = tk.Label(root, text="Task Description:", font=("Helvetica", 12))
        self.task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.priority_label = tk.Label(root, text="Task Priority:", font=("Helvetica", 12))
        self.priority_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.priority_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.priority_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, width=20, font=("Helvetica", 12))
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks, width=20, font=("Helvetica", 12))
        self.clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(root, width=50, font=("Helvetica", 12), bg="#f0f0f0", selectbackground="#a0a0a0")
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.display_tasks()

    def add_task(self):
        description = self.task_entry.get()
        priority = self.priority_entry.get()
        task = Task(description, priority)
        self.tasks.append(task)
        self.task_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.display_tasks()

    def clear_tasks(self):
        self.tasks = []
        self.display_tasks()

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            description = f"☐ {task.description}, Priority: {task.priority}"
            if task.completed:
                description = f"☑ {task.description}, Priority: {task.priority}"
            self.task_listbox.insert(tk.END, description)
            self.task_listbox.itemconfig(tk.END, fg="green" if task.completed else "black")
            self.task_listbox.bind("<Double-1>", self.toggle_task_completion)

    def toggle_task_completion(self, event):
        index = self.task_listbox.curselection()[0]
        task = self.tasks[index]
        task.completed = not task.completed
        self.display_tasks()

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Calculate position x and y coordinates
    x = (screen_width/2) - (root.winfo_reqwidth()/2)
    y = (screen_height/2) - (root.winfo_reqheight()/2)
    # Set geometry for the root window
    root.geometry("+%d+%d" % (x, y))
    root.mainloop()

if __name__ == "__main__":
    main()