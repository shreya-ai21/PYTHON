from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
# GREEN = "#9bdeac"
GREEN = "#1D8348"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    check_mark.config(text='')
    canvas.itemconfig(time_onscreen, text='00:00')
    timer_label.config(text="TIMER", fg=GREEN)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    if reps > 8:
        reset_timer()

    i = 0
    reps += 1
    checks = int(reps/2)
    if reps % 8 == 0:
        countdown(int(LONG_BREAK_MIN*60))
        timer_label.config(text="BREAK", fg=RED)
        check_mark.config(text='✔'*checks)
    elif reps % 2 == 0:
        countdown(int(SHORT_BREAK_MIN*60))
        timer_label.config(text="BREAK", fg=PINK)
        check_mark.config(text='✔'*checks)
        i += 1
    else:
        countdown(int(WORK_MIN*60))
        timer_label.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_min < 6:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_onscreen, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 25, 'bold'))
timer_label.grid(row=0, column=1)

# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="E:/Shreya Shastry/UDEMY/PYTHON/DAY 28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(row=1, column=1)
time_onscreen = canvas.create_text(100, 130, text="00:00", fill="white",
                                   font=(FONT_NAME, 35, 'bold'))

# Start
start = Button(text="Start", font=(FONT_NAME, 10, 'bold'), command=start_timer)
start.grid(row=2, column=0)

# Reset
start = Button(text="Reset", font=(FONT_NAME, 10, 'bold'), command=reset_timer)
start.grid(row=2, column=2)

# checkmark
check_mark = Label(text='', fg=GREEN, bg=YELLOW,
                   font=(FONT_NAME, 20, 'bold'))
check_mark.grid(row=3, column=1)

window.mainloop()
