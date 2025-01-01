from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

width = 500
height = 750
reset= False
pause = False
game_over= False
score=0
  
bubbles=[]
bullets=[]  

initial= time.time()

def pick_zone(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0: 
            return 0
        elif dx < 0 and dy >= 0: 
            return 3
        elif dx < 0 and dy < 0: 
            return 4
        elif dx >= 0 and dy < 0: 
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx < 0 and dy >= 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        elif dx >= 0 and dy < 0:
            return 6

def convet_to_zero(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y
    else:
        return None

def convert_to_actual(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y
    else:
        return None

def point(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def line_mpl(x0, y0, x1, y1):
    zone = pick_zone(x0, x1, y0, y1)
    x0, y0 = convet_to_zero(x0, y0, zone)
    x1, y1 = convet_to_zero(x1, y1, zone)
    dx = x1 - x0
    dy = y1 - y0

    d = (2 * dy) - dx
    East = 2 * dy
    NorthEast = (2 * dy) - (2 * dx)
    y = y0

    for x in range(int(x0), int(x1) + 1):
        xi, yi = convert_to_actual(x, y, zone)
        point(xi, yi)
        if d > 0:
            y += 1
            d += NorthEast
        else:
            d += East

def cut_b():
    glColor3f(0.8, 0.006,0.000003)
    x1 = (width - 100)
    x2 = (width - 50)
    y1 = (height - 100)
    y2 = (height - 50)
    line_mpl(x1, y1, x2, y2)
    line_mpl(x1, y2, x2, y1)
    glColor3f(0,0,0)

def pause_b():
    glColor3f(0.3,0.7, 0.1)
    x1 = width - 200
    x2 = width - 240
    y1 = height - 40
    y2 = height - 100

    line_mpl(x1, y1, x1, y2)
    line_mpl(x2, y1, x2, y2)
    glColor3f(0,0,0)

def play_b():
    glColor3f(0.3,0.05, 0)
    x1 = width - 260
    x2 = width - 200
    y1 = height - 100
    y2 = height - 40
    y3 = height - 70

    line_mpl(x1, y1, x1, y2)
    line_mpl(x1, y2, x2, y3)
    line_mpl(x1, y1, x2, y3)
    glColor3f(0,0,0)

def play_pause():
    global pause
    if pause==False:
        pause_b()
    else:
        play_b()

def back_b():
    glColor3f(0, 0, 0.90)
    x1 = 50
    x2 = 120
    x3 = 75
    y1 = height - 40
    y2 = height - 100
    y3 = height - 65
    line_mpl(x1, y3, x2, y3)
    line_mpl(x1, y3, x3, y2)
    line_mpl(x1, y3, x3, y1)
    glColor3f(1,0,0)
    
def draw_circle(r,cir_x,cir_y):
    x=0
    y=r
    d=1-r
    
    while x<=y:
        if d<0:
            x+=1
            d=d+2*x+3 #East pixel
            
        else:
            x+=1
            y-=1
            d= d+2*(x-y)+5 #South East Pixel
        point(x + cir_x, y + cir_y)
        point(y + cir_x, x + cir_y)
        point(y + cir_x, -x + cir_y)
        point(x + cir_x, -y + cir_y)
        point(-x + cir_x, -y + cir_y)
        point(-y + cir_x, -x + cir_y)
        point(-y + cir_x, x + cir_y)
        point(-x + cir_x, y + cir_y)
        
b_s= random.randint(40,60)
b_x= random.uniform(b_s,width-b_s)
b_y= height-150  


bubbles.append({"x":b_x,"y":b_y, "size":b_s})

def bubble():
    global game_over, bubbles
    
    if not game_over:
        glColor3f(0.3,0.1,0.2)
        for i in bubbles:
            draw_circle(i["size"]//2,i["x"],i["y"])
        glColor3f(1,1,1)
    
missed_bullet=0
missed_bubble=0
shooter_x= width//2
shooter_h= 50

def shooter():
    global shooter_x, shooter_h
    
    x1= shooter_x-shooter_h//2
    x2= shooter_x+shooter_h//2
    y1= 20
    y2= 20+shooter_h//2
    
    x=(x1+x2)//2
    y=(y1+y2)//2
    
    if game_over== True:
        glColor3f(1,0,0)
    else:
        glColor3f(0.1,0.6,0.3)
        
    draw_circle((x2-x1)/2,x,y)
    glColor3f(0,0,0)
    
def bullets_():
    global bullets 
    glColor3f(0.3,0.2,0)
    for i in bullets:
        draw_circle(i["size"],i["x"],i["y"])
              
def game_over_():
    global score, game_over, initial, bullets, bubbles,missed_bullet, missed_bubble
    
    score=0
    missed_bubble=0
    missed_bullet=0
    game_over=True
    
    bullets.clear()
    bubbles.clear()
    
    glutPostRedisplay()
    
def fire_bullets(_):
    global bullets, missed_bullet  
    for i in bullets :
        i["y"] += 10  
    
def collusion(bullet, bubble):
    bullet_x = bullet["x"]
    bullet_y = bullet["y"]
    bubble_x = bubble["x"]
    bubble_y = bubble["y"]

    d_x = abs(bullet_x - bubble_x)
    d_y = abs(bullet_y - bubble_y)
    
    rad = bullet['size'] // 2 + bubble['size'] // 2

    if d_x <= rad and d_y <= rad:
        return True
    return False

def keyboard(key, x, y):
    global shooter_x, game_over, reset, pause, shooter_h, bullets, width
 
    if  game_over== False and reset==False and pause==False:
        if key == b'a':
            shooter_x -= 5
            if shooter_x - shooter_h // 2 < 0:
                shooter_x = shooter_h // 2
        elif key == b'd':
            shooter_x += 5
            if shooter_x + shooter_h // 2 > width:
                shooter_x = width - shooter_h // 2
        elif key == b' ': 
            bullets.append({'x': shooter_x, 'y': 10 + shooter_h, 'size': 10}) 
    glutPostRedisplay()
    
b_s = random.randint(40, 60) 
def new_bubble(_):
    global bubbles, pause, game_over, reset, width, height,b_s
    
    if pause == False and reset == False and game_over == False:
       
        b_x = random.uniform(b_s, width - b_s)  
        b_y = height - 150  
        bubbles.append({"x": b_x, "y": b_y, "size": b_s})

        glutPostRedisplay()
        glutTimerFunc(1000, new_bubble, 0)


def update_bubble(_):
    global shooter_h, shooter_x, game_over, score, bubbles, bullets, missed_bubble, missed_bullet
    
    s_l = shooter_x - shooter_h // 2
    s_r = shooter_x + shooter_h // 2
    s_b = 20
    s_t = 20 + shooter_h // 2
    
    if game_over== False and reset== False and pause== False:
 
        i = 0
        while i < len(bubbles):
            x = bubbles[i]
            if s_t > x['y']-20 - x["size"] // 2 and s_l <= x['x'] <=s_r:
                game_over_()
                return
            elif s_t > x['y']-20 - x["size"] // 2 and s_l <= x['x']+x['size']//2 <=s_r:
                game_over_()
                return
            elif s_t > x['y']-20 - x["size"] // 2 and s_l <= x['x']-x['size']<=s_r:
                game_over_()
                return

            elif x['y'] < 20:  
                missed_bubble += 1
                print("Missed bubble: ", missed_bubble)
                bubbles.pop(i)  
                if missed_bubble== 3:
                    game_over_()
                    return
            else:
                x['y'] -= 1
                i += 1 
        
        i = 0
        while i < len(bullets):
            x = bullets[i]
            x['y'] += 5
            if x['y'] > height:  
                missed_bullet += 1
                print('Misfire: ', missed_bullet)
                bullets.pop(i)  
                if missed_bullet >= 3:
                    game_over_()
                    return
            else:  
                hit = False
                for j in range(len(bubbles)):
                    if collusion(x, bubbles[j]):
                        score += 1
                        print("Score: ", score)
                        bubbles.pop(j)
                        bullets.pop(i)  
                        hit = True
                        break
                if not hit:
                    i += 1  

    glutTimerFunc(50, update_bubble, 0)
    glutPostRedisplay()

def reset_bubble():
    global bubbles, reset, game_over, height, b_x
    
    for i in bubbles:
        if game_over:
            i['y'] = 800
        elif reset:
            i["y"]= height-200
        else:
            i["y"]= height-200
        i['x']= random.uniform(b_s,width-i['size'])

def restart_game():
    global score, game_over, reset, initial, bubbles, bullets, missed_bubble, missed_bullet, pause
    
    score = 0
    missed_bullet = 0
    missed_bubble = 0
    initial = time.time()
    bubbles.clear()
    bullets.clear()
    reset_bubble()
    
    print("Starting the game")  # This will show when the game restarts
    reset = False
    pause = False
    game_over = False
    
    glutTimerFunc(1000, new_bubble, 0) 
    glutTimerFunc(10, update_bubble, 0)  

def Mouse_click(button, state, x, y):
    global reset, game_over, pause, score, width, height
    mouse_y = height - y

    play_pause_b_zone = ((width - 260, height - 100), (width - 200, height - 40))
    back_b_zone = ((50, height - 100), (120, height - 40))
    cut_b_zone = ((width - 100, height - 100), (width - 50, height - 50))
    
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print(f"Mouse clicked at: ({x}, {mouse_y})")  # Debugging output
        if click_zone((x, mouse_y), back_b_zone):
            print("Restart button clicked")  # Debugging output
            restart_game()
            
        elif click_zone((x, mouse_y), cut_b_zone):
            print("Game Over!!!")
            print("Total Score:", score)
            glutLeaveMainLoop()
            
        elif click_zone((x, mouse_y), play_pause_b_zone):
            pause = not pause
            if pause:
                print("You have paused the game")
            else:
                print("Playing the game")

def click_zone(point, box):
    x, y = point    
    (x1, y1), (x2, y2) = box
    print(f"Checking point {point} against box {box}")  # Debugging output
    return x1 <= x <= x2 and y1 <= y <= y2


       
def iterate():
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def show_screen():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    cut_b()
    play_pause()
    back_b()
    back_b()
    back_b()
    shooter()
    bubble()
    bullets_()
    glutTimerFunc(20, fire_bullets, 0)
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"Bubble Game")
glutDisplayFunc(show_screen)

glutKeyboardFunc(keyboard)
glutMouseFunc(Mouse_click)

glutTimerFunc(10,update_bubble, 0)

glutTimerFunc(20, fire_bullets, 0)
glutTimerFunc(1000, new_bubble, 0)
glutMainLoop()
