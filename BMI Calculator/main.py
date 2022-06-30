from tkinter import *
from tkinter import messagebox


def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showwarning("warning", "Warning")


ws = Tk()
ws.title('BMI CALCULATOR')
ws.geometry('300x400')
ws.config(bg='#FFFFFF')

var = IntVar()

frame = Frame(
    ws,
    padx=20,
    pady=50
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Age",
    pady="20",
    padx="10",
    font=("serif", 15, 'bold')
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Gender',
    pady="20",
    font=("serif", 15, 'bold')
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text='Male',
    variable=var,
    value=1,
    font=("serif", 15, 'bold')

)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text='Female',
    variable=var,
    value=2,
    font = ("serif", 15, 'bold')
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Height (cm)",
    pady="20",
    font = ("serif", 15, 'bold')
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Weight (kg)",
    pady="20",
    font = ("serif", 15, 'bold')
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi,
    activeforeground="red",
    activebackground="blue",
    pady=3,
    font=("serif", 15, 'bold')

)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry,
    pady=3,
    font=("serif", 15, 'bold')
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda: ws.destroy(),
    pady=3,
    font=("serif", 15, 'bold')
)
exit_btn.pack(side=LEFT)
ws.geometry('400x500+300+150')
ws.mainloop()
