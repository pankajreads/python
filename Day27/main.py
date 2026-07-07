import tkinter
window= tkinter.Tk()
window.title("GUI program")
window.minsize(1139,500)

#label are normal text or string that are shown on screen using pack method
my_label= tkinter.Label(text=("A Label"),font=("Arial",24,"bold"))
my_label.pack(side="bottom")
window.mainloop()