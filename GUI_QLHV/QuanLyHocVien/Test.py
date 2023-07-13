import tkinter as tk
from tkinter import ttk

def get_combobox_value():
    value = combobox.get()
    print("Selected value:", value)

root = tk.Tk()

# Tạo một combobox
combobox = ttk.Combobox(root)
combobox['values'] = ('Option 1', 'Option 2', 'Option 3')
combobox.pack()

button = tk.Button(root, text="Get Value", command=get_combobox_value)
button.pack()

root.mainloop()
