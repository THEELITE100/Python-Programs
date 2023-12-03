import tkinter as tk
from tkinter import filedialog
class NoteTaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taker")
        self.text = tk.Text(root)
        self.text.pack()
        save_button = tk.Button(root, text="Save", command=self.save_note)
        save_button.pack()
    def save_note(self):
        note_content = self.text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(note_content)
root = tk.Tk()
app = NoteTaker(root)
root.mainloop()