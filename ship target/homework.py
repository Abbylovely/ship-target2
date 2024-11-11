import pgzrun
from random import randint
WIDTH=600
HEIGHT=500
TITLE="bumblee bee and th flower"
bee=Actor("bee")
bee.pos=100,100
flower=Actor("flower")
flower.pos=150,150
score=0
game_over=False
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score:"+str(score),color=(139,0,0),topleft=(10,10))
    if game_over:
        screen.fill((220,20,60))
        screen.draw.text("Time up your final score is"+str(score),midtop=(WIDTH/2,HEIGHT/2),color=(205,92,92),fontsize=50)
def place_flower():
    flower.x=randint(70,(WIDTH-70))
    flower.y=randint(70,(HEIGHT-70))
def timeup():
    global game_over
    game_over=True
def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    if bee.colliderect(flower):
        place_flower()
        score=score+5
clock.schedule(timeup,60.0)

pgzrun.go()
