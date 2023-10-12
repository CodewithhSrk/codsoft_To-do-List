

import tkinter as tk
from tkinter import *

def add():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def edit():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        selected_task = task_entry.get()
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, selected_task)
        task_entry.delete(0, tk.END)

def show_details():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        selected_task = tasks_listbox.get(selected_task_index)
        task_details_text.config(state=tk.NORMAL)  
        task_details_text.delete('1.0', tk.END) 
        task_details_text.insert(tk.END, selected_task) 
        task_details_text.config(state=tk.DISABLED)  

root = tk.Tk()
root.title("TO-DO LIST")
root.geometry("400x500")
root.resizable(False, False)

TopImage = tk.PhotoImage(file="images/taskbar.png")
tk.Label(root, image=TopImage).pack(pady=10)

task_entry = tk.Entry(root,  width=50)
task_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, padx=10, pady=10)

add_button = tk.Button(button_frame, text="ADD TASK",
 bg="#A9A9A9", fg="white",width=12, command=add)

remove_button = tk.Button(button_frame, text="DELETE",
 bg="#A9A9A9", fg="white",width=12, command=remove)

edit_button = tk.Button(button_frame, text="EDIT",  
 bg="#A9A9A9", fg="white",width=12, command=edit)

show_details_button = tk.Button(button_frame, text="SHOW DETAILS",
 bg="#A9A9A9", fg="white",width=16, command=show_details)

add_button.grid(row=0, column=0, padx=8)
remove_button.grid(row=0, column=1, padx=8)
edit_button.grid(row=0, column=2, padx=8)
show_details_button.grid(row=1, column=0, columnspan=3, pady=10)

tasks_listbox = tk.Listbox(root, bd=3, width=40, height=15, bg="#D3D3D3")
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
tasks_listbox.config(selectmode=tk.SINGLE)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

task_details_label = tk.Label(root, text="TASK DETAILS",
font=("Times New Roman", 12), foreground="black")
task_details_label.pack()

task_details_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
task_details_text.pack()

root.mainloop()



