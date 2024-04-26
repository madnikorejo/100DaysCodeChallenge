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

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,)


timer_label = Label(text="Timer",bg=YELLOW, font=(FONT_NAME, 35, "bold"),fg=GREEN)
timer_label.grid(column=1, row=0)

canva = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(100,113, image= tomato_img)
canva.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canva.grid(column=1,row=1)

button1 = Button(text="Start", highlightthickness=0)
button1.grid(column=0, row=2)
button2 = Button(text="Reset", highlightthickness=0)
button2.grid(column=2, row=2)

check_mark = Label(text="✔", fg=GREEN,bg=YELLOW)
check_mark.grid(column= 1, row= 3)

window.mainloop()
