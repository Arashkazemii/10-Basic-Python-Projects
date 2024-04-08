import tkinter as tk

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

        self.task_label = tk.Label(root, text="Task Description:")
        self.task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.priority_label = tk.Label(root, text="Task Priority:")
        self.priority_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.priority_entry = tk.Entry(root, width=30)
        self.priority_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, width=20)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, width=20)
        self.remove_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.display_tasks()

    def add_task(self):
        description = self.task_entry.get()
        priority = self.priority_entry.get()
        task = Task(description, priority)
        self.tasks.append(task)
        self.task_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.display_tasks()

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.display_tasks()
        except IndexError:
            pass

    def toggle_completed(self, index):
        self.tasks[index].completed = not self.tasks[index].completed
        self.display_tasks()

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            description = f"Description: {task.description}, Priority: {task.priority}"
            if task.completed:
                description += " (Completed)"
            checkbox = tk.Checkbutton(self.task_listbox, text=description, command=lambda i=index: self.toggle_completed(i))
            checkbox.select() if task.completed else checkbox.deselect()
            checkbox.grid(row=index, column=0, sticky="w")

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