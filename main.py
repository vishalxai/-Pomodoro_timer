from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
#------------------------------GLOBAL VARIABLE----------------------------#
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg= GREEN)
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.bell()  # Play a beep sound when the countdown finishes
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
#Timer label Top
timer_label = Label(text="Timer",bg=GREEN,fg=YELLOW,font=(FONT_NAME,50))
timer_label.grid(column=1,row=0)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.grid(column=1,row=1)

tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img )
timer_text = canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
#START and Reset buttons (botton left and right)
start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

#Check marks or Progress below
check_marks = Label(text= "",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

check_marks.config(text="✔")





window.mainloop()
