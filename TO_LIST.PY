import tkinter as tk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        title_label = tk.Label(root, text='TODO List App', font=('Helvetica', 24))
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.task_entry = tk.Entry(root)
        self.task_entry.grid(row=1, column=0, padx=10, pady=5)

        add_button = tk.Button(root, text='Add Task', command=self.add_task)
        add_button.grid(row=1, column=1, padx=10, pady=5)

        tasks_label = tk.Label(root, text='Tasks:', font=('Helvetica', 18))
        tasks_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        mark_button = tk.Button(root, text='Mark Task as Completed', command=self.mark_task_completed)
        mark_button.grid(row=4, column=0, padx=10, pady=5)

        remove_button = tk.Button(root, text='Remove Task', command=self.remove_task)
        remove_button.grid(row=4, column=1, padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_task_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.task_listbox.get(task_index)
            self.tasks[task_index] = f'[COMPLETED] {task}'
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, self.tasks[task_index])

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('TODO List')
    app = TodoListApp(root)
    root.mainloop()