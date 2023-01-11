from tkinter import *
import math

work_min=30
short_break=5
long_break=25
reps=0
timer=None

# UI
window=Tk()
window.title("Pomodoro")
window.config(bg="#89C4E1")
label=Label(text="Timer")
label.config(bg="#89C4E1",fg="yellow", font=("Lato", 40, "bold"))
label.grid(row=0,column=1, padx=100)

canvas = Canvas(width=350, height=350, bg="#89C4E1", highlightthickness=0)
clock= PhotoImage(file="E:\PYTHON\pomodorro\Red_clock.png")
canvas.create_image(175, 175, image=clock)
timer_text=canvas.create_text(180, 225 , text="00:00", font=("Helvetica",30,"bold"), fill="Lime green")
canvas.grid(row=1,column=1)

def onStart():
    global reps
    reps+=1
    work_min_sec=30*60
    short_break_sec=5*60
    long_break_sec=25*60
    
    if(reps%8==0):
        countdown(long_break_sec)
        label.config(text="Break",bg="#89C4E1",fg="#FD8A8A", font=("Lato", 40, "bold"))
    elif(reps%2==0):
        countdown(short_break_sec)
        label.config(text="Break",bg="#89C4E1",fg="#F1F7B5", font=("Lato", 40, "bold"))
    else:
        countdown(work_min_sec)
        label.config(text="Work",bg="#89C4E1",fg="#9CFF2E", font=("Lato", 40, "bold"))    
    
def countdown(count):
    count_min=math.floor(count/60)
    count_Sec=count%60
    if int(count_Sec) <10:
        count_Sec=f"0{count_Sec}"    
    if count_Sec==0:
        count_Sec="00"
    global timer
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_Sec}")
    if count>0:
        timer=window.after(1000,countdown,count-1)
    else:
        onStart()  
        marks=""
        work_seccion=math.floor(reps/2)
        for _ in range(work_seccion):
            marks+="✔"
        checkmarks.config(text=marks)      
def onReset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", bg="#89C4E1",fg="yellow", font=("Lato", 40, "bold") )
    checkmarks.config(text="")
    global reps
    reps=0
           
start=Button(text="Start", command=onStart , width=10, highlightthickness=0 , font=("aerial", 18, "bold"), bg="orange")
reset=Button(text="Reset", command=onReset , width=10, highlightthickness=0 , font=("aerial", 18, "bold"), bg="red")
start.grid(row=1, column=0, padx=30, pady=30)
reset.grid(row=1, column=2, padx=30, pady=30)

checkmarks=Label(fg="red", bg="#89C4E1", pady=25, font=(20))
checkmarks.grid(row=2, column=1)

window.mainloop()
