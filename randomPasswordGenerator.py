import random
from graphics import *
from random import randrange
from time import *

"""
Created on Wed Jan 2 2022
@author: Miksam Kurumbang
"""


def window():
    win = GraphWin("Random Password Generator", 600, 600)
    win.setBackground("orange")
    win.setCoords(0,0,20,20)
    return win

def getInfo():

   title = Text(Point(10, 18), "Random Password Generator")
   title.setStyle("bold")
   title.setSize(15)
   title.draw(win)

   lowerCase = Text(Point(6, 15), "Lower case characters:")
   lowerCase.draw(win)
   lowerCaseAns = Entry(Point(11.5,15), 15)
   lowerCaseAns.draw(win)

   upperCase = Text(Point(6, 14), "Upper case characters:")
   upperCase.draw(win)
   upperCaseAns = Entry(Point(11.5, 14), 15)
   upperCaseAns.draw(win)

   numbers = Text(Point(7.5, 13), "Numbers:")
   numbers.draw(win)
   numbersAns = Entry(Point(11.5, 13), 15)
   numbersAns.draw(win)

   specialChar = Text(Point(6.4, 12), "Special characters:")
   specialChar.draw(win)
   specialCharAns = Entry(Point(11.5, 12), 15)
   specialCharAns.draw(win)

   passLen = Text(Point(6.6, 11), "Password length:")
   passLen.draw(win)
   passLenAns = Entry(Point(11.5, 11), 15)
   passLenAns.draw(win)


   button = Rectangle(Point(8.1, 8), Point(11.9, 9))
   button.setFill("yellow")
   buttonLabel = Text(Point(10, 8.5), "Generate")
   button.draw(win)
   buttonLabel.draw(win)

   return title, lowerCase,lowerCaseAns , upperCase, upperCaseAns, button , buttonLabel, numbers, numbersAns, specialChar,specialCharAns,passLen,passLenAns

def checkButtonClick(clickedPoint,leftLower,rightUpper):
    # gets the x and y coordinate of the leftLower point of the rectangle
    leftX = leftLower.getX()
    leftY = leftLower.getY()
    # gets the x and y coordinate of the rightUpper point of the rectangle
    rightX = rightUpper.getX()
    rightY = rightUpper.getY()
    #gets the x and y coordinate of the clickedpoint
    checkClickX = clickedPoint.getX()
    checkClickY = clickedPoint.getY()

    #checks if the mouse click is in the rectangle
    if leftX < checkClickX and rightX > checkClickX and leftY < checkClickY and rightY > checkClickY:
        return "in"
    else:
        return "out"

def checkSubmit():
   checkSubmit = "out"
   while checkSubmit != "in":

      clickedPoint = win.getMouse()
      checkSubmit = checkButtonClick(clickedPoint, button.getP1(), button.getP2())

      if checkSubmit == "in":

         lowCasechars = str(lowerCaseAns.getText())
         upperCasechars =str(upperCaseAns.getText())
         nums = str(numbersAns.getText())
         special = str(specialCharAns.getText())
         passLength = str(passLenAns.getText())




         password = ""
         for i in range(int(passLength)):
             CharGroup = random.randint(1,4)
             if CharGroup == 1:
                index = round(abs(random.random() * (len(lowCasechars) - 1)))
                password = password + lowCasechars[index]
             elif CharGroup == 2:
                index = round(abs(random.random() * (len(upperCasechars) - 1)))
                password = password + upperCasechars[index]

             elif CharGroup == 3:
                index = round(abs(random.random() * (len(nums) - 1)))
                password = password + nums[index]

             elif CharGroup == 4:
                index = round(abs(random.random() * (len(special) - 1)))
                password = password + special[index]

         newPassbox = Rectangle(Point(3, 3), Point(17, 6))
         newPassbox.setFill("white")
         newPassbox.draw(win)

         passwordText = Text(Point(10, 5), password)
         passwordText.setStyle("bold")
         passwordText.draw(win)





if __name__=='__main__':
    win = window()
    title, lowerCase,lowerCaseAns , upperCase, upperCaseAns, button , buttonLabel, numbers, numbersAns, specialChar,specialCharAns,passLen,passLenAns= getInfo()
    checkSubmit()





win.getMouse()
win.close()







