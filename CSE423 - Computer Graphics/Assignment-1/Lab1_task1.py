import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_lines(a, b, c, d):
    glLineWidth(7)
    glColor3f(0.5, 0.0, 0.5)  # color of the house
    glBegin(GL_LINES)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glEnd()


"""Raindrops"""
rain_pt = []  # An empty list that will hold instances of the Raindrop class.
angle = 0  # A variable used to control the angle at which rain falls.
background_r = 0  # Red component
background_g = 0  # Green component
background_b = 0  # Blue component


class Raindrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.random() * 2


def draw(rain):
    glLineWidth(5)
    # glColor3f(0.0, 0.0, 1.0)
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(rain.x, rain.y)  # Specifies the starting point of the raindrop.
    # Calculate the new position of the raindrop
    new_x = rain.x + angle * rain.speed
    new_y = rain.y - rain.speed
    glVertex2f(new_x, new_y)
    glEnd()


def raindrops(rain):  # This function updates the position of a raindrop based on its speed.
    rain.y -= rain.speed  # Decreases the y-coordinate of the raindrop by its speed. This makes the raindrop fall.
    if rain.y < 0:
        rain.y += 500
    #  If the raindrop goes off the screen (y-coordinate < 0), it resets its position to the bottom of the window.


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global rain_pt, angle, background_r, background_g, background_b
    glClearColor(background_r, background_g, background_b, 1.0)  # alpha refers to the transparency of the color.
    # 1.0 means fully opaque.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # House color
    # glColor3f(0.5, 0.0, 0.5)

    """House"""
    # House Top
    draw_lines(100, 250, 400, 250)
    draw_lines(100, 250, 250, 300)
    draw_lines(250, 300, 400, 250)

    # House Box
    draw_lines(100, 250, 100, 0)
    draw_lines(400, 250, 400, 0)
    draw_lines(100, 0, 400, 0)

    # Door
    draw_lines(150, 0, 150, 130)
    draw_lines(150, 130, 200, 130)
    draw_lines(200, 130, 200, 0)

    # Door Knob
    draw_points(190, 70)

    # Window
    draw_lines(300, 200, 350, 200)
    draw_lines(300, 200, 300, 150)
    draw_lines(300, 150, 350, 150)
    draw_lines(350, 150, 350, 200)

    # Window Bars
    draw_lines(325, 150, 325, 200)
    draw_lines(300, 175, 350, 175)
    
    # The for loop iterates over each raindrop in the rain_pt list.
    # For each raindrop, the raindrops() function is called to update its position.
    # Then, the draw() function is called to draw the raindrop on the screen.

    # raindrops
    for rain in rain_pt:
        raindrops(rain)
        draw(rain)

    glutSwapBuffers()
    # This function swaps the front and back buffers of the current window.
    # It is typically used with double-buffered windows to display rendered images without flickering.


def init():
    global rain_pt
    for i in range(500):
        x = random.uniform(0, 500)  # Start raindrops from anywhere along the x-axis
        y = random.uniform(250, 500)  # Start raindrops from top half of the window
        rain_pt.append(Raindrop(x, y)) # Add a new raindrop to the list of raindrops.


def mouse(key):
    global angle
    if key == GLUT_LEFT_BUTTON:
        angle -= 45
    elif key == GLUT_RIGHT_BUTTON:
        angle += 45


def special(key, x, y):
    global background_r, background_g, background_b
    if key == GLUT_KEY_UP:
        background_r += 0.3
        background_g += 0.3
        background_b += 0.3
    elif key == GLUT_KEY_DOWN:
        background_r -= 0.3
        background_g -= 0.3
        background_b -= 0.3


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Raining on House")
init()
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(special)
glutMotionFunc(mouse)
glutMainLoop()
