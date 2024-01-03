import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((500, 500))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
root = tk.Tk()
root.title("Image Viewer")
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)
image_label = tk.Label(root)
image_label.pack()
root.mainloop()