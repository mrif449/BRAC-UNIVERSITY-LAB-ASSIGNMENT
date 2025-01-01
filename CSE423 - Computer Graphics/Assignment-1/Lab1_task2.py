from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


class RandomPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blinking = False
        self.color = [random.random(), random.random(), random.random()]
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed


freeze_points = False
random_points = []
speed = 0.01
boundary = 250


def create(pt):
    if pt.blinking:
        time_seconds = int(glutGet(GLUT_ELAPSED_TIME) / 1000)
        if time_seconds % 2 != 0:
            glColor3f(*pt.color)
        else:
            glColor3f(0, 0, 0)
    else:
        glColor3f(*pt.color)


def draw_point(pt):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(pt.x, pt.y)
    glEnd()


def create_points(x, y):
    new_pt = RandomPoint(x - boundary, boundary - y)
    random_points.append(new_pt)


def mouse_listener(button, state, x, y):
    global random_points, freeze_points
    if not freeze_points:
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            create_points(x, y)
            glutPostRedisplay()
        elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            for pt in random_points:
                pt.blinking = not pt.blinking
            glutPostRedisplay()


def keyboard_listener(key, x, y):
    global freeze_points, speed
    if key == b' ' or key == ord(' '):
        freeze_points = not freeze_points
        if freeze_points:
            speed = 0
        else:
            speed = 0.01
    if key == b' ' and freeze_points:
        freeze_points = True
        speed = 0
    elif key == b' ' and not freeze_points:
        freeze_points = False
        speed = 0.01
    elif not freeze_points:
        if key == GLUT_KEY_UP:
            speed *= 3
            update_speed(3)
        elif key == GLUT_KEY_DOWN:
            speed /= 3
            update_speed(0.3)


def update_speed(factor):
    global random_points
    for pt in random_points:
        pt.dx *= factor
        pt.dy *= factor


def update_points():
    global random_points
    for pt in random_points:
        if not freeze_points:
            pt.x += pt.dx
            pt.y += pt.dy
            if pt.x <= -boundary or pt.x >= boundary:
                pt.dx *= -1
            if pt.y <= -boundary or pt.y >= boundary:
                pt.dy *= -1


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    for pt in random_points:
        create(pt)
        draw_point(pt)
    glutSwapBuffers()


def idle():
    if not freeze_points:
        update_points()
        glutPostRedisplay()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Building the Amazing Box")


glClearColor(0, 0, 0, 1)
gluOrtho2D(-boundary, boundary, -boundary, boundary)


glutDisplayFunc(display)
glutIdleFunc(idle)
glutMouseFunc(mouse_listener)
glutSpecialFunc(keyboard_listener)
glutMainLoop()
