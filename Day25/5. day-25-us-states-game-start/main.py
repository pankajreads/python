from turtle import Turtle , Screen, shape,turtles,onscreenclick,mainloop,shapesize
import pandas as pd

screen=Screen()
screen.bgcolor("Black")
screen.title("state game")
image="/home/pankaj/python/Day25/5. day-25-us-states-game-start/india.gif"
screen.addshape(image)


x_cor=[]
y_cor=[]
def get_click_coor(x,y):
    x_cor.append(x)
    y_cor.append(y)
onscreenclick(get_click_coor)

indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
    "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
    "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]
print(x_cor)
print(y_cor)
mainloop()