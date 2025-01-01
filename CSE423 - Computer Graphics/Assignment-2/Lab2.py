from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_width = 500
window_height = 800
fall_speed = 0.001

catcher_pos_x = 0
catcher_pos_y = 50
pause_active = False
diamond_pos_x = random.randint(-240, 240)
diamond_pos_y = 200
diamond_width = 20
diamond_height = 10

current_score = 0
game_over = False

# Global variable to store the diamond's color
diamond_color = (0.79, 0.93, 0.87)  # Default color

def draw_pixels(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_line(x1, y1, x2, y2):
    zone = determine_zone(x1, y1, x2, y2)
    x1, y1, x2, y2 = zone_conversion(zone, x1, y1, x2, y2)
    line_points = midpoint_algorithm(x1, y1, x2, y2)
    zone_back_conversion(zone, line_points)

def midpoint_algorithm(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    d = dy - (dx / 2)
    x = int(x1)
    y = int(y1)
    points += [[x, y]]

    for x in range(int(x1) + 1, int(x2) + 1):
        if d < 0:
            d += dy
        else:
            d += (dy - dx)
            y += 1
        points += [[x, y]]

    return points

def determine_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx > 0 and dy >= 0:
        if abs(dx) > abs(dy):
            return 0
        else:
            return 1
    elif dx <= 0 <= dy:
        if abs(dx) > abs(dy):
            return 3
        else:
            return 2
    elif dx < 0 and dy < 0:
        if abs(dx) > abs(dy):
            return 4
        else:
            return 5
    elif dx >= 0 > dy:
        if abs(dx) > abs(dy):
            return 7
        else:
            return 6

def zone_conversion(zone, x1, y1, x2, y2):
    if zone == 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    elif zone == 2:
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    elif zone == 3:
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
    elif zone == 4:
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
    elif zone == 5:
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
    elif zone == 6:
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2
    elif zone == 7:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2
    return x1, y1, x2, y2

def zone_back_conversion(zone, points):
    if zone == 0:
        for x, y in points:
            draw_pixels(x, y)
    elif zone == 1:
        for x, y in points:
            draw_pixels(y, x)
    elif zone == 2:
        for x, y in points:
            draw_pixels(-y, x)
    elif zone == 3:
        for x, y in points:
            draw_pixels(-x, y)
    elif zone == 4:
        for x, y in points:
            draw_pixels(-x, -y)
    elif zone == 5:
        for x, y in points:
            draw_pixels(-y, -x)
    elif zone == 6:
        for x, y in points:
            draw_pixels(y, -x)
    elif zone == 7:
        for x, y in points:
            draw_pixels(x, -y)

def draw_diamond(x, y, width, height):
    draw_line(x, y, x + width // 2, y - height)  
    draw_line(x + width // 2, y - height, x + width, y)  
    draw_line(x, y, x + width // 2, y + height)  
    draw_line(x + width // 2, y + height, x + width, y)  

def generate_random_color():
    """Generate a random color."""
    return (random.random(), random.random(), random.random())

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    """Diamond"""
    global diamond_pos_x, diamond_pos_y, diamond_width, diamond_height, game_over, diamond_color
    if game_over:
        glColor3f(0, 0, 0)  # Black color when game is over
    else:
        glColor3f(*diamond_color)  # Use the current diamond color
    draw_diamond(diamond_pos_x, diamond_pos_y, diamond_width, diamond_height)

    """Play-Pause Button"""
    glColor3f(0.98, 0.92, 0.37)
    if pause_active:
        draw_line(-10, 225, 10, 235)
        draw_line(10, 235, -10, 245)
        draw_line(-10, 245, -10, 225)
    else:
        draw_line(-4, 225, -4, 245)
        draw_line(4, 225, 4, 245)

    """Restart Button"""
    glColor3f(0.44, 0.68, 0.94)
    draw_line(-240, 235, -230, 245)
    draw_line(-240, 235, -230, 225)
    draw_line(-240, 235, -215, 235)

    """Exit Button"""
    glColor3f(0.88, 0.21, 0.21)
    draw_line(240, 225, 220, 245)
    draw_line(240, 245, 220, 225)

    """Diamond Catcher"""
    if game_over:
        glColor3f(1.0, 0.0, 0.0)  # Red color when game is over
    else:
        glColor3f(0.96, 0.97, 0.87)  # Default color
    draw_line(catcher_pos_x - 70, -235, catcher_pos_x + 70, -235)
    draw_line(catcher_pos_x - 50, -250, catcher_pos_x + 50, -250)
    draw_line(catcher_pos_x - 50, -250, catcher_pos_x - 70, -235)
    draw_line(catcher_pos_x + 50, -250, catcher_pos_x + 70, -235)

    glutSwapBuffers()

def keyboard_input(key, x, y):
    global catcher_pos_x

    move_value = 20
    if key == GLUT_KEY_LEFT:
        if catcher_pos_x - 70 <= -250:
            pass
        else:
            if not pause_active and not game_over:
                catcher_pos_x -= move_value

    if key == GLUT_KEY_RIGHT:
        if catcher_pos_x + 70 >= 250:
            pass
        else:
            if not pause_active and not game_over:
                catcher_pos_x += move_value

    glutPostRedisplay()

def mouse_input(button, state, x, y):
    global catcher_pos_x, catcher_pos_y, diamond_pos_x, diamond_pos_y, pause_active, game_over, diamond_color
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            if 230 <= x <= 260 and 0 <= y <= 50:
                pause_active = not pause_active
            elif 10 <= x <= 30 and 25 <= y <= 40:
                if game_over:  # Only restart if game is over
                    print("Starting Over!")
                    print("-----------------------------")
                    catcher_pos_x = 0
                    catcher_pos_y = 50
                    diamond_pos_x = random.randint(-240, 240)
                    diamond_pos_y = 200
                    fall_speed = 0.001  # Reset fall speed
                    pause_active = False
                    game_over = False  # Reset game over state
                    diamond_color = generate_random_color()  # Get a new random color
            elif 445 <= x <= 490 and 10 <= y <= 50:
                glutLeaveMainLoop()

        glutPostRedisplay()

def update():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def animate_diamond():
    global diamond_pos_y, diamond_pos_x, catcher_pos_x, catcher_pos_y, pause_active, fall_speed, current_score, game_over, diamond_color

    if not pause_active and not game_over:
        diamond_pos_y -= fall_speed
        fall_speed += 0.0001
        if (catcher_pos_x - 70 <= diamond_pos_x <= catcher_pos_x + 70) and (diamond_pos_y <= -240):
            current_score += 1
            print("Score:", current_score)
            diamond_pos_x = random.randint(-240, 240)
            diamond_pos_y = 200
            diamond_color = generate_random_color()  # Set new random color
        elif diamond_pos_y <= -250:
            print("Game Over! Final Score:", current_score)
            print("-----------------------------")
            game_over = True
            diamond_pos_x = random.randint(-240, 240)
            diamond_pos_y = 200
            current_score = 0
            catcher_pos_x = 0
            catcher_pos_y = 50
            fall_speed = 0.001  # Reset fall speed
            pause_active = False

    glutPostRedisplay()

def initialize():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(500, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
window = glutCreateWindow(b"Catch The Diamond")
initialize()
glutDisplayFunc(display)
glutIdleFunc(animate_diamond)
glutSpecialFunc(keyboard_input)
glutMouseFunc(mouse_input)
glutMainLoop()
