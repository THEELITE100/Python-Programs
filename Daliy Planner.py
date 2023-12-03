import tkinter as tk
class DailyPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Planner")
        self.tasks = {}
        self.time_label = tk.Label(root, text="Time:")
        self.time_label.pack()
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()
        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        self.tasks_text = tk.Text(root, height=10, width=30)
        self.tasks_text.pack()
    def add_task(self):
        time = self.time_entry.get()
        task = self.task_entry.get()
        self.tasks.setdefault(time, []).append(task)
        self.update_tasks()
    def update_tasks(self):
        self.tasks_text.delete(1.0, tk.END)
        for time, tasks in self.tasks.items():
            self.tasks_text.insert(tk.END, f"{time}:\n")
            for task in tasks:
                self.tasks_text.insert(tk.END, f"  - {task}\n")
            self.tasks_text.insert(tk.END, "\n")
root = tk.Tk()
app = DailyPlannerApp(root)
root.mainloop()