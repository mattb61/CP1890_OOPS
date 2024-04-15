import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# Button Functionality:
def get_amount():
    """
    Get's data from database.
    """
    conn = sqlite3.connect("../Question_5/sales_database.sqlite")
    c = conn.cursor()
    query = f"select amount from Sales where salesDate = '{date_entry.get()}' and region = '{region_entry.get()}'"
    c.execute(query)
    amount = c.fetchall()
    conn.close()
    
    conn = sqlite3.connect("../Question_5/sales_database.sqlite")
    c = conn.cursor()
    query = f"select id from Sales where salesDate = '{date_entry.get()}' and region = '{region_entry.get()}'"
    c.execute(query)
    sale_id = c.fetchall()
    conn.close()
    
    if amount_float == []:
        messagebox.showinfo("Info", "No sale found.")
    else:
        amount_float.set(amount)
        id_text.set(sale_id)


def save_changes():
    """
    Saves changes made.
    """
    conn = sqlite3.connect("../Question_5/sales_database.sqlite")
    c = conn.cursor()
    query = f"update Sales set amount = {amount_entry.get()} where salesDate = '{date_entry.get()}' and region = '{region_entry.get()}'"
    c.execute(query)
    conn.commit()
    conn.close()


def exit_program():
    """
    Closes the window.
    """
    main_window.destroy()


# Window:
main_window = tk.Tk()
main_window.title("Edit Sales Amount")
main_window.geometry("335x175")

frame = ttk.Frame(main_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

# Title:
title_label = ttk.Label(frame, text="Enter date and region to get sales amount.")
title_label.grid(column=0, row=0, columnspan=3)

# Date:
date_label = ttk.Label(frame, text="Date: ")
date_label.grid(column=0, row=1, sticky=tk.E)

date_text = tk.StringVar()
date_entry = ttk.Entry(frame, width=27, textvariable=date_text)
date_entry.grid(column=1, row=1)

# Region: 
region_label = ttk.Label(frame, text="Region: ")
region_label.grid(column=0, row=2, sticky=tk.E)

region_text = tk.StringVar()
region_entry = ttk.Entry(frame, width=27, textvariable=region_text)
region_entry.grid(column=1, row=2)

# Amount:
amount_label = ttk.Label(frame, text="Amount: ")
amount_label.grid(column=0, row=3, sticky=tk.E)

amount_float = tk.StringVar()
amount_entry = ttk.Entry(frame, width=27, textvariable=amount_float)
amount_entry.grid(column=1, row=3)

# ID:
id_label = ttk.Label(frame, text="ID: ")
id_label.grid(column=0, row=4, sticky=tk.E)

id_text = tk.IntVar(value="")
id_entry = ttk.Entry(frame, width=27, textvariable=id_text, state="readonly")
id_entry.grid(column=1, row=4)

# Buttons:
button1 = ttk.Button(frame, text="Get Amount!", command=get_amount)
button1.grid(column=2, row=2, padx=10, stick=tk.W)
button2 = ttk.Button(frame, text="Save Changes", command=save_changes)
button2.grid(column=1, row=5, sticky=tk.W)
button3 = ttk.Button(frame, text="Exit", command=exit_program)
button3.grid(column=1, row=5, sticky=tk.E)


for child in frame.winfo_children():
    child.grid_configure(pady=2)


if __name__ == "__main__":
    main_window.mainloop()
