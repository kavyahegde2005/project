from tkinter import Tk,messagebox,Label,Button

root = Tk()
root.title("Click a number")

score = 0
score_label =Label(root, text=f"Score:{score}")
score_label.grid(row=0,column=3)

def number_clicked(num):
    global score
    if num == 0:
        messagebox.showinfo("Game Over!",f"You clicked 0. Game Over! \n your total score is {score}")
        root.destroy() 
    else:
        score+=num
        score_label.config(text=f"Score: {score}")
        

for i in range(10):
    button = Button(root, text=" ", width=10, height=5,
                    command=lambda number=i: number_clicked(number))
    button.grid(row=i//3, column=i%3)


root.mainloop()
