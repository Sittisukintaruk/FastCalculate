import RandomNumber
from tkinter import *





root = Tk()
frame = Frame(root)
frame.pack()
text = StringVar()
namberdecimal = StringVar()
number = RandomNumber.FuntionRandomNamber()
numberstr = str(number)
text.set(numberstr)
numberDecimal = RandomNumber.FuntionRandomdecmai()
namberdecimal.set(numberDecimal)

def setnumber():
    number = RandomNumber.FuntionRandomNamber()
    numberstr = str(number)
    numberDecimal = RandomNumber.FuntionRandomdecmai()
    text.set(numberstr)
    namberdecimal.set(numberDecimal)


    
    





bottomframe = Frame(root)

mylabel = Label(root , textvariable=text ,fg= "red" , bg = "dark green", font = "Helvetica 149 bold italic")
mylabel.pack( side = TOP)

mylabel = Label(root , textvariable=namberdecimal ,fg= "red" , bg = "yellow", font = "Helvetica 100 bold")
mylabel.pack( side = BOTTOM)


myButton0 = Button(root , text = "ROLL", padx = 40, pady = 20 ,bg = "blue"   , command = lambda:setnumber())
myButton0.pack( side = BOTTOM)

root.mainloop()

"""
print(number)
print(numberDecimal)
"""