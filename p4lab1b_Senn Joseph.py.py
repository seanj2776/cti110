#Joseph Robert Eli Senn
#P4LAB1
#11/5/2024
#This program sets up an animation of an object drawing my initials.


import turtle

# Function to draw the letter 'J'
def draw_j(t):
    t.penup()
    t.goto(-150, 0)  # Start drawing 'J' at this position
    t.pendown()
    t.right(90)  # Face the turtle downward
    t.forward(100)  # Draw the vertical line of "J"
    t.right(90)
    t.forward(50)  # Draw the horizontal line at the bottom
    t.right(90)
    t.forward(25)  # Draw the small curve part at the bottom

# Function to draw the letter 'S'
def draw_s(t):
    t.penup()
    t.goto(50, 0)  # Move to the starting position for 'S'
    t.pendown()
    
    # Start at the top of 'S'
    t.setheading(0)  # Face the turtle to the right (horizontal)

    t.forward(50)  # Draw the top horizontal line of "S"
    t.left(90)  # Turn the turtle downward
    t.forward(25)  # Draw the middle vertical part of "S"
    t.left(90)  # Turn the turtle to the left to draw the bottom horizontal part
    t.forward(50)  # Draw the bottom horizontal line of "S"
    t.right(90)  # Turn the turtle to the right
    t.forward(25)  # Complete the bottom curve of 'S'
    t.right(90)  # Face the turtle upwards
    t.forward(50)  # Complete the bottom curve of 'S'

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)  # Set pen size
t.color("blue")  # Set pen color

# Draw the initials 'J' and 'S' using the loop
drawing_functions = [draw_j, draw_s]

# Loop through the functions to draw the initials
for draw in drawing_functions:
    draw(t)  # Call each drawing function with the turtle object
    t.penup()  # Lift the pen up to move it to the next position after drawing each initial
    t.forward(150)  # Move the turtle to the right after drawing each initial
    t.pendown()  # Lower the pen to start drawing the next initial

# Hide the turtle and finish
t.hideturtle()
turtle.done()

