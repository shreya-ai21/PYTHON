from tkinter import *
window = Tk()

window.title('My First GUI Program')
window.minsize(width=500, height=300)
mytext = Label(text="Label 1", font=('Arial', 24, 'bold'))
mytext.pack()


def button_click():
    mytext.config(text="BUttion is clicked")


button = Button(text="BUTTONNNN", command=button_click)
button.pack()

window.mainloop()
