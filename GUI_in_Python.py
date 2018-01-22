# File: GUI_in_Python.py
# Description: Graphic representation of program in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Graphic representation of program in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/GUI_in_Python (date of access: XX.XX.XXXX)


import math
import random
import turtle
import assistant  # Importing functions from assistant.py

# Defining the constants, so we can use them everywhere
PHI = 360 / 7
R = 50


# Function for changing the position of the pen
def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# Function for creating the shape of the gun
def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


# Function for creating the gun
def draw_gun(x, y):
    # Drawing the circle
    gotoxy(x, y)
    turtle.circle(80)
    # Drawing the sight
    gotoxy(x, y + 160)
    draw_circle(5, 'red')

    # Drawing the places for bullets
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 60)
        draw_circle(20, 'white')


# Function for spinning the roulette
def spin(start, x, y):
    for i in range(start, random.randrange(7, 15)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 60)
        draw_circle(20, 'yellow')
        draw_circle(20, 'white')

    gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 60)
    draw_circle(20, 'yellow')

    # Returning the updating variable 'start'
    return i % 7


# Setting the speed of drawing
turtle.speed(0)

start = 0
answer = ''

draw_gun(100, 100)

while answer != 'N' and answer != 'n':
    answer = turtle.textinput("Do you want to play?", "Y/N")
    if answer == 'Y' or answer == 'y':

        # Returning the initial position and executing the function at the same time
        start = spin(start, 100, 100)

        if start == 0:
            gotoxy(-50, 200)
            turtle.write('Shoot!', font=('Arial', 18, 'normal'))
            assistant.duplicating_files_in_current_directory('.')

    else:
        pass
