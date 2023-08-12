from tkinter import *
window = Tk()
window.config(padx=20, pady=20)


def calc():
    miles = float(miles_entry.get())
    km = Label(text=miles*1.609).grid(row=1, column=1)


miles_entry = Entry()
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equals = Label(text='equals').grid(row=1, column=0)

km_label = Label(text="Km").grid(row=1, column=2)

calculate = Button(text="Calculate", command=calc).grid(row=2, column=1)

window.mainloop()
