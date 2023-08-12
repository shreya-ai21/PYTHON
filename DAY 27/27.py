from tkinter import *
window = Tk()


def button_click():
    mytext.config(text=f"{input.get()}")


window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

mytext = Label(text="Label 1", font=('Arial', 24, 'bold'))
mytext.grid(column=0, row=0)

input = Entry()
input.grid(column=3, row=2)

button = Button(text="BUTTONNNN", command=button_click)
button.grid(row=1, column=1)

button1 = Button(text='NEW BUTTON')
button1.grid(column=2, row=0)

# .place(x,y)
# .grid(column=,row=)

window.mainloop()
