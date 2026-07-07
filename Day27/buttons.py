from tkinter import *
window=Tk()
window.minsize(200,100)
window.title("coverter")

input=(Entry(width=10,textvariable="Enter miles here"))
input.grid(row=0,column=1)
num=input.get()

lable=Label(text="Miles")
lable.grid(row=0,column=0)
label_two=Label(text="kilometre") 
label_two.grid(row=1,column=0)

def convert():
    num=float(input.get())
    num=num*1.60934
    lable_three=Label(text=num)
    lable_three.grid(row=1,column=1)
button=Button(text="Calculate",command=convert,bg="red",fg="white",border="5px")
button.grid(row=2,column=1)

mainloop()