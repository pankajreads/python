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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=20,pady=20,bg=YELLOW)

canvas=Canvas(width=224,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="256 - pomodoro-start/tomato.png")
canvas.create_image(112,112,image=img)
canvas.create_text(106,130,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=0,column=1)

start=Button(text="Start")
start.grid(row=1,column=0)
reset=Button(text="Reset")
reset.grid(row=1,column=2)

tick=Label(text="✔",fg=GREEN,background=YELLOW,font=(FONT_NAME,20,"bold"))
tick.grid(row=2,column=1)

mainloop()