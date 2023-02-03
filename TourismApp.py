from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Pittsburgh, PA Tourism App").grid(column=0, row=0)
ttk.Button(frm, text="Dining", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text="Attractions", command=root.destroy).grid(column=2, row=1)
ttk.Button(frm, text="Lodging", command=root.destroy).grid(column=3, row=1)
ttk.Button(frm, text="Itinerary", command=root.destroy).grid(column=4, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=5, row=1)
root.mainloop()
