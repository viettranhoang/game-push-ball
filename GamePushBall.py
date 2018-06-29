from tkinter import *
import time
import random
from tkinter import messagebox



'''
' final variables
'''
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
BALL_SPEED = 3
SCROLL_BAR_SPEED = 3
IS_START_GAME = True
SCORE = 0


'''
' object Ball
'''
class Ball:
    def __init__(this, canvas, color, scrollBar):
        this.canvas = canvas
        this.scrollBar = scrollBar
        this.ball = canvas.create_oval(10, 10, 30, 30, fill = color)
        this.canvas.move(this.ball, 100, 200)
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        this.x = start[0]
        this.y = 3
        this.dead = False
    
    def draw(this):
        this.canvas.move(this.ball, this.x , this.y)
        position = this.canvas.coords(this.ball)
        positionBar = this.canvas.coords(this.scrollBar.bar)
    
        if position[1] <= 0:
            this.y = BALL_SPEED
        if position[3] >= SCREEN_HEIGHT:
            this.dead = True
        if position[0] <= 0:
            this.x = BALL_SPEED
        if position[2] >= SCREEN_WIDTH:
            this.x = -BALL_SPEED
        if collision(position, positionBar) == True:
            this.y = -BALL_SPEED

         
'''
' object ScrollBar 
'''
class ScrollBar:
    def __init__(this, canvas, color):
        this.canvas = canvas
        this.bar = canvas.create_rectangle(0, 0, 100, 20, fill = color)
        this.canvas.move(this.bar, 200, 400)
        this.x = 0
        this.y = 0
        this.canvas.bind_all('<KeyPress-Left>', this.left)
        this.canvas.bind_all('<KeyPress-Right>', this.right)

    def draw(this):
        this.canvas.move(this.bar, this.x, this.y)

    def left(this, event):
        this.x = -SCROLL_BAR_SPEED

    def right(this, event):
        this.x = SCROLL_BAR_SPEED


'''
' functions 
'''
## draw and update object
def drawObject():
    bar = ScrollBar(cans, 'blue')
    ball = Ball(cans, 'red', bar)
    while ball.dead == False:
        ball.draw()
        bar.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

## handing collision of ball and b?
def collision(posBall, posBar):
    center = [(posBall[0] + posBall[2])/2, (posBall[1] + posBall[3])/2]
    if center[0] <= posBar[2] and center[0] >= posBar[0] :
        if posBall[3] >= posBar[1] and posBall[3] <= posBar[3] - 10 :
            global SCORE
            SCORE += 1
            return True
    return False

## restart game when gane over
def restartGame():
    cans.delete(ALL)
    global SCORE
    SCORE = 0


## message box when game over
def messageBoxGameOver():
    answer = messagebox.askyesno("Play again?", "Score : " + str(SCORE))
    if answer == True:
        restartGame()
    else:
        global IS_START_GAME
        IS_START_GAME = False
        messagebox.showinfo("F*ck","Why don't you want to play again?")
        
        

'''
' init screen 
'''
tk = Tk()
tk.title("GameBall")
tk.resizable(0, 0)
cans = Canvas(tk, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
cans.pack()


'''
' main 
'''
while IS_START_GAME == True:
    drawObject()
    messageBoxGameOver()


                        
