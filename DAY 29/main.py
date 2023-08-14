from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# logo
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='E:/Shreya Shastry/UDEMY/PYTHON/DAY 29/logo.png')
canvas.create_image(98, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website Entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website = Entry(width=35)
website.focus()
website.insert(END, string="https://")
website.grid(row=1, column=1, columnspan=2)

# Email Entry
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email = Entry(width=35)
email.insert(END, string='shreya.shastry@gmail.com')
email.grid(row=2, column=1, columnspan=2)

# password Entry
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password = Entry(width=17)
password.grid(row=3, column=1)

# Generate password button
generate = Button(text="Generate Password", width=15, padx=0)
generate.grid(row=3, column=2)

# Add password
add = Button(text="Add", width=36)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
