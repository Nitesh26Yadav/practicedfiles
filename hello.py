# name = input('What is your name?\n')

# Enter_Hours = 35
# Enter_Rate = 2.75
# Pay = Enter_Hours * Enter_Rate
# print(Pay)


# Python Program to convert temperature in celsius to fahrenheit
# fahrenheit = int(input())

# celsius = (fahrenheit - 32) / 1.8
# print(celsius)


# inp = input('Enter Fahrenheit Temperature:')

# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Please enter a number')


# try:
#     Enter_Hours = int(input())
#     Enter_Rate = int(input())
# except:
#     print("Error, please enter numeric input")


'''
Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:'''

# try:
#     scr = float(input("Enter Score: "))
#     if scr > 1.0 or scr == int:
#         print("Bad score")
#     elif scr >= 0.9:
#         print("A")
#     elif scr >= 0.8:
#         print("B")
#     elif scr >= 0.7:
#         print("C")
#     elif scr >= 0.6:
#         print("D")
#     elif scr < 0.6:
#         print("F")
#     else:
#         print("Bad score")
# except:
#     print("Bad score")


# To install graphics in python --- pip install graphics.py
# import graphics

from graphics import *

# win = GraphWin('Shapes')
# # Draw a red circle centered at point (100,100) with radius 30
# center = Point(100, 100)
# circ = Circle(center, 30)
# circ.setFill('red')
# circ.draw(win)
# # Put a textual label in the center of the circle
# label = Text(center, "Red Circle")
# label.draw(win)
# # Draw a square using a Rectangle object
# rect = Rectangle(Point(30, 30), Point(70, 70))
# rect.draw(win)
# # Draw a line segment using a Line object
# line = Line(Point(20, 30), Point(180, 165))
# line.draw(win)


# # Draw an oval using the
# oval = Oval(Point(20, 150), Point(180, 199))
# oval.draw(win)


# def main():
#     # Introduction

#     print("This program plots the growth of a 10-year investment . ")
#     # Get principal and interest rate
#     principal = float(input("Enter the initial principal : "))
#     apr = float(input("Enter the annualized interest rate : "))

#     # Create a graphics window with labels on left edge
#     win = GraphWin(" Investment Growth Chart ", 700, 700)
#     win.setBackground("white")
#     win.setCoords(-1.75, -200, 11.5, 10400)
#     Text(Point(-1, 0), '0 . 0K') . draw(win)
#     Text(Point(-1, 2500), '2 . 5K') . draw(win)
#     Text(Point(-1, 5000), '5.0K') . draw(win)
#     Text(Point(-1, 7500), '7 . 5k') . draw(win)
#     Text(Point(-1, 10000), '10 . 0K') . draw(win)
#     # Draw bar for initial principal
#     bar = Rectangle(Point(0, 0), Point(1, principal))
#     bar.setFill("green")
#     bar.setWidth(2)
#     bar.draw(win)
#     # Draw a bar for each subsequent year
#     for year in range(1, 11):
#         principal = principal * (1 + apr)
#         bar = Rectangle(Point(year, 0), Point(year+1, principal))
#         bar . setFill("green")
#         bar.setWidth(2)
#         bar . draw(win)
#     input("Press <Enter> to quit . ")
#     win . close()


# main()

from graphics import *


def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win . setCoords(0.0, 0.0, 3.0, 4.0)
    # Draw the interface
    Text(Point(1, 3), " Celsius Temperature : ") . draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature : ") . draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText . setText("O . O")
    inputText . draw(win)
    outputText = Text(Point(2.25, 1), " ")
    outputText . draw(win)
    button = Text(Point(1.5, 2.0), "Convert It ")
    button . draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)) . draw(win)
    # wait for a mouse click
    win . getMouse()
    # convert input
    celsius = float(inputText . getText())
    fahrenheit = 9.0/5.0 * celsius + 32
    # display output and change button
    outputText . setText(round(fahrenheit, 2))
    button . setText("Quit ")
    # wait for click and then quit
    win.getMouse()
    win.close()


main()
