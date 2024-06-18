import winsound

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
TICK="✔"

# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps=0
breaks=0
def start_timer():
    global reps,breaks
    
    
    if reps%4==0 and reps>0:
        timer.config(text="Long Break",fg=RED)
        tick.config(text=TICK*reps)
        winsound.Beep(1000,500)
        count_down(LONG_BREAK_MIN*60)
    elif reps>breaks:
        breaks+=1
        timer.config(text="Short Break",fg=PINK)
        tick.config(text=TICK*reps)
        winsound.Beep(1000,500)
        count_down(SHORT_BREAK_MIN*60)
    else:
        timer.config(text="Work Time",fg=GREEN)
        reps+=1
        winsound.Beep(1000,500)
        count_down(WORK_MIN*60)    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global win
    minutes=int(count/60)
    seconds=count%60
    if len(str(seconds))==1:
        seconds=f"0{seconds}"
    elif seconds==0:
        seconds="00"
    time=f"{minutes}:{seconds}"
    canvas.itemconfig(s,text=time)
    if count>0:
        win=window.after(1000,count_down,count-1 )
    else:
        start_timer()
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global l,reps,breaks,win
    window.after_cancel(win)
    canvas.itemconfig(s,text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    reps=0
    breaks=0   
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodaro")
window.config(padx=100,pady=100,bg=YELLOW)

photo=PhotoImage(file="E:/python/pomodaro/tomato.png")


#Image and timer
canvas=Canvas(width=300,height=300,highlightthickness=0)
canvas.create_image(150,150,image=photo)
s=canvas.create_text(150,170,text="00:00",font=("Courier",25),fill="white")
canvas.config(bg=YELLOW,border=0)
canvas.grid(column=1,row=1)

#Main Title
timer=Label()
timer.config(text="Timer",font=("courier",40,"bold"),bg=YELLOW,fg=GREEN)
timer.grid(column=1,row=0)

#start button
start=Button(command=start_timer,text="Start",width=10,font=("Arial",10),highlightthickness=0)
start.grid(column=0,row=2)

#reset button
reset=Button(text="Reset",font=("Arial",10),width=10,highlightthickness=0,command=timer_reset)
reset.grid(column=2,row=2)

#tick label
tick=Label()
tick.grid(column=1,row=3)

window.mainloop()