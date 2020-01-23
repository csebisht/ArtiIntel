import tkinter as tk
from tkinter import ttk

win =tk.Tk()
win.title('Pradeep')

Username_label = ttk.Label(win,text='Username')
Username_label.grid(row=0,column=0,sticky=tk.W)
Username_label_var = tk.StringVar
Username_label_entry = ttk.Entry(win,width=16,textvariable=Username_label_var)
Username_label_entry.grid(row=0,column=1)

name_label = ttk.Label(win,text='Name')
name_label.grid(row=1,column=0,sticky=tk.W)
name_var = tk.StringVar
name_text = ttk.Entry(win,width=16,textvariable=name_var)
name_text.grid(row=1,column=1)

Email_label = ttk.Label(win,text='Email')
Email_label.grid(row=2,column=0,sticky=tk.W)
Email_var = tk.StringVar
Email_label_Entry = ttk.Entry(win,width=16,textvariable=Email_var)
Email_label_Entry.grid(row=2,column=1)

Mobile_label = ttk.Label(win,text='Mobile')
Mobile_label.grid(row=3,column=0,sticky=tk.W)
Mobile_var = tk.StringVar
Mobile_label_Entry = ttk.Entry(win,width=16,textvariable=Mobile_var)
Mobile_label_Entry.grid(row=3,column=1)
def action():
    Username = Username_label_var.get()
    Name = name_var.get()
    Email = Email_var.get()
    Mobile = Mobile_var.get()
    with open('file.txt', 'a') as f:
        f.write(f'{Username},{Name},{Email},{Mobile}\n')
    Username_label_entry.delete(0, tk.END)
    name_text.delete(0, tk.END)
    Email_label_Entry.delete(0, tk.END)
    Mobile_label_Entry.delete(0, tk.END)
save_button=ttk.Button(win,text='Submit',command=action)
save_button.grid(row=4,column=0,sticky=tk.W)
win.mainloop()