"""
Deven Kanwal
Computational Creativity

This program utilizes python's Turtle package and a Markov Matrix to create a piece of artwork created of four shapes
that have been influential to me throughout my life.
"""

import numpy as np
import turtle 


t = turtle.Turtle()

"""
Placement of each shape is determined by Markov Martrix
Color of each shape is determined by Markov Matrix
Random Choice from Markov Matrix
"""

def get_matrix():
    """Function creates a markov matrix"""
    matrix = np.array([[.1, .5, .2, .2],[.3, .4, .1, .2],[.2, .2, .2, .4],[.25, .25, .3, .2]]) #Probablility Matrix for each of the 4 states
    return matrix

def get_next_state(curr_state):
    """Function get's the next state from markov matrix"""
    matrix = get_matrix()
    next_state = np.random.choice([0, 1, 2, 3], p=matrix[curr_state])
    return next_state

def triangle(curr_state, color):
    """creates a triangle of a fixed size. Placement determined
    by a Markov Matrix"""
    t.up()
    #the followiing lines determine where the triangle should be drawn based on the current state
    if curr_state == 0:
        cord_1 = 0
        cord_2 = 0
    elif curr_state == 1:
        cord_1 = 100
        cord_2 = 100
    elif curr_state == 2:
        cord_1 = -100
        cord_2 = -100
    elif curr_state == 3:
        cord_1 = 50
        cord_2 = 50 
    t.goto((cord_1, cord_2))
    t.color(color)
    t.right(60)
    t.down()
    for i in range(2):  
        t.forward(20)
        t.right(120)
    t.forward(20)
    t.right(60)
    t.up()

def circle(curr_state, color):
    """creates a circle of a fixed size. Placement determined
    by a Markov Matrix"""
    #the followiing lines determine where the circle should be drawn based on the current state
    if curr_state == 0:
        cord_1 = 50
        cord_2 = 50
    elif curr_state == 1:
        cord_1 = 0
        cord_2 = 0
    elif curr_state == 2:
        cord_1 = -25
        cord_2 = -25
    elif curr_state == 3:
        cord_1 = -75
        cord_2 = -75
    t.goto(cord_1, cord_2)
    t.color(color)
    t.down()
    t.circle(50)
    t.up()
    
def square(curr_state, color):
    """creates a square of a fixed size. Placement determined
    by a Markov Matrix"""
    #the followiing lines determine where the square should be drawn based on the current state
    if curr_state == 0:
        cord_1 = -200
        cord_2 = -200
    elif curr_state == 1:
        cord_1 = -20
        cord_2 = -20
    elif curr_state == 2:
        cord_1 = 200
        cord_2 = 200
    elif curr_state == 3:
        cord_1 = 0
        cord_2 = -100
    t.goto(cord_1, cord_2)
    t.color(color)
    t.down()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.up()
    
    
def pentagon(curr_state, color):
    """creates a trapezoid of a fixed size. Placement determined
    by a Markov Matrix"""
    #the followiing lines determine where the pentagon should be drawn based on the current state
    if curr_state == 0:
        cord_1 = -300
        cord_2 = 10
    elif curr_state == 1:
        cord_1 = 5
        cord_2 = -30
    elif curr_state == 2:
        cord_1 = 300
        cord_2 = -50
    elif curr_state == 3:
        cord_1 = 25
        cord_2 = -10
    t.goto(cord_1, cord_2)
    t.color(color)
    t.down()
    t.right(90)
    for i in range(5):
        t.forward(50)
        t.right(60)
    t.forward(50)
    t.up()
    
    
def main():
    """Main method runs the program to create an image of shapes
    with placement determined by the Markov Matrix"""
    start_state = 0 #the start state will always correspond to the first row of the Markov Matrix
    curr_state = start_state 
    #The following for-loop creates the image, with the range being how many times a a state is queried for
    for i in range(1):
        state = get_next_state(curr_state)
        if state == 0:
            color = 'blue'
        elif state == 1:
            color = 'cyan'
        elif state == 2:
            color = 'red'
        elif state == 3:
            color = 'green'
        print(state)
        triangle(curr_state=state, color=color)
        circle(curr_state=state, color=color)
        square(curr_state=state, color=color)
        pentagon(curr_state=state, color=color)
        curr_state = state
    t.getscreen()._root.mainloop()

main() #runs the program


