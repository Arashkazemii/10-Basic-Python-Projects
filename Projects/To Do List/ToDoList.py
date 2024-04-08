import tkinter as tk

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x300")

        self.tasks = []

        self.task_label = tk.Label(root, text="Task Description:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.priority_label = tk.Label(root, text="Task Priority:")
        self.priority_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.priority_entry = tk.Entry(root, width=30)
        self.priority_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

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

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"Description: {task.description}, Priority: {task.priority}")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()