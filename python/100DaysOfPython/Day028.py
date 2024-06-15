# Day 28
# Pomodoro timer

# ---------------------------- MODULES ------------------------------- #
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    screen.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    lb_check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(n):
    count_min = math.floor(n / 60)
    count_sec = n % 60
    if not count_sec:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer
    if n > 0:
        timer = screen.after(1000, count_down, n - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        lb_check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Timer")
screen.config(bg=YELLOW, padx=75, pady=50)

IMAGE = PhotoImage(file="Day028_tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=IMAGE)
timer_text = canvas.create_text(100, 150, text="00:00", font=(FONT_NAME, 20, "bold"))

bt_start = Button(text="START", command=start_timer)
bt_stop = Button(text="RESET", command=reset_timer)

lb_timer = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
lb_check = Label(text="", fg=GREEN, bg=YELLOW)

lb_timer.grid(column=1, row=0)
canvas.grid(column=1, row=1)
bt_start.grid(column=0, row=2)
bt_stop.grid(column=2, row=2)
lb_check.grid(column=1, row=3)

screen.mainloop()
