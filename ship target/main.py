from random import randint
import pgzrun
#itertools helps us cycle through a set of items repeatedly
import itertools

WIDTH=400
HEIGHT=400



block_pos=[
    (350,50),(350,350),(50,350),(50,50)
]
b_pos=itertools.cycle(block_pos)

block1=Actor("block",center=(50,50))
robot1=Actor("robot",center=(200,200))

def draw():
    screen.clear()
    block1.draw()
    robot1.draw()

def move_block():
    animate(block1,"bounce_end",duration=1,pos=next(b_pos))

def ship_target():
    x=randint(100,300)
    y=randint(100,300)
    robot1.target=x,y
    target_angle=robot1.angle_to(robot1.target)
    target_angle += 360*((robot1.angle-target_angle+ 180)//360)
    animate(
        robot1,angle=target_angle,duration=0.3,on_finished=move_ship,
    )
    
def move_ship():
    anim=animate(
        robot1,
        tween="accel_decel",
        pos=robot1.target,
        duration=robot1.distance_to(robot1.target)/400,
        on_finished=ship_target,
    )
def update():
    pass

move_block()
ship_target()
clock.schedule_interval(move_block,1)
pgzrun.go()
