from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps=0
check_marks=""
timer= None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps, check_marks
    reps=0
    check_marks=""
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    print(reps)
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check_marks
    count_minutes=math.floor(count / 60)
    count_seconds= count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count == 0:
        if reps % 2 == 1:
            check_marks += "✔"
            print(check_marks)
            check_label.config(text=f"{check_marks}")
        start_timer()
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

start_buton = Button(text="Start", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 8, "bold"), command=start_timer)
start_buton.grid(row=2, column=0)

reset_buton = Button(text="Reset", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 8, "bold"), command=reset_timer)
reset_buton.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 8, "bold"))
check_label.grid(row=3, column=1)
window.mainloop()
