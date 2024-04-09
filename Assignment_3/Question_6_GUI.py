import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def get_amount():
    pass

def save_changes():
    pass

def exit_program():
    main_window.destroy()

main_window = tk.Tk()
main_window.title("Edit Sales Amount")
main_window.geometry("335x175")

frame = ttk.Frame(main_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

title_label = ttk.Label(frame, text="Enter date and region to get sales amount.")
title_label.grid(column=0, row=0, columnspan=3)

date_label = ttk.Label(frame, text="Date: ")
date_label.grid(column=0, row=1, sticky=tk.E)

date_text = tk.StringVar()
date_entry = ttk.Entry(frame, width=27, textvariable=date_text)
date_entry.grid(column=1, row=1)

region_label = ttk.Label(frame, text="Region: ")
region_label.grid(column=0, row=2, sticky=tk.E)

region_text = tk.StringVar()
region_entry = ttk.Entry(frame, width=27, textvariable=region_text)
region_entry.grid(column=1, row=2)

amount_label = ttk.Label(frame, text="Amount: ")
amount_label.grid(column=0, row=3, sticky=tk.E)

amount_float = tk.StringVar()
amount_entry = ttk.Entry(frame, width=27, textvariable=amount_float)
amount_entry.grid(column=1, row=3)

id_label = ttk.Label(frame, text="ID: ")
id_label.grid(column=0, row=4, sticky=tk.E)

id_int = tk.IntVar(value="")
id_entry = ttk.Entry(frame, width=27, textvariable=id_int, state="readonly")
id_entry.grid(column=1, row=4)

button1 = ttk.Button(frame, text="Get Amount!", command=get_amount)
button1.grid(column=2, row=2, padx=10, stick=tk.W)
button2 = ttk.Button(frame, text="Save Changes", command=save_changes)
button2.grid(column=1, row=5, sticky=tk.W)
button3 = ttk.Button(frame, text="Exit", command=exit_program)
button3.grid(column=1, row=5, sticky=tk.E)


for child in frame.winfo_children():
    child.grid_configure(pady=2)



main_window.mainloop()