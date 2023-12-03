import tkinter as tk
def on_digit_click(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + digit)
def on_operator_click(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)
def on_equal_click():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
# Create an entry widget to display the expression and result
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)
# Create buttons for digits
for i in range(9):
    digit = str(i + 1)
    btn = tk.Button(root, text=digit, command=lambda digit=digit: on_digit_click(digit))
    btn.grid(row=i // 3 + 1, column=i % 3)
# Create buttons for arithmetic operators
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    btn = tk.Button(root, text=operator, command=lambda operator=operator: on_operator_click(operator))
    btn.grid(row=i + 1, column=3)
# Create the equal button
equal_btn = tk.Button(root, text='=', command=on_equal_click)
equal_btn.grid(row=4, column=0, columnspan=4)
# Start the GUI main loop
root.mainloop()