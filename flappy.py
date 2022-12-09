import pgzrun
import random

TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 708

#Game Logic
gravity = 0.3
gap = 200 #pipe gap
pipe_speed = 1.5


#Actors
bird = Actor("bird1")
top_pipe = Actor("top")
bottom_pipe = Actor("bottom")



def draw():
    screen.blit("background", (0, 0))
    bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()
    screen.draw.text(f"Score : {bird.score}", (0, 0), color = "Black")

def on_mouse_down():
    global gravity
    if bird.alive:
        bird.y += -50
        bird.speed = -6.5
    bird.angle += -90


# def on_key_down():
#     global bird_alive
#     if(keys.O):
#         print("OK")

def update():
    global top_pipe, bottom_pipe, gap
    bird.angle += 5
    #bird moving
    bird.speed += gravity
    bird.y += bird.speed
    if bird.left > WIDTH: 
        bird.x = 0
    #pipe move
    top_pipe.x += -pipe_speed
    bottom_pipe.x += -pipe_speed
    if top_pipe.right < 0:
        offset = random.randint(-150, 200)
        top_pipe.midleft = (WIDTH, offset)
        bottom_pipe.midleft = (WIDTH, offset + top_pipe.height + gap)
        bird.score += 1 
    #bird dies
    if bird.y > HEIGHT or bird.y < 0:
        reset()
    if (bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe)):
        hit_pipe()

    #Animation
    if bird.alive:
        if bird.speed > 0:
            bird.image = "bird1"
        else:
            bird.image = "bird0"

def hit_pipe():
    print("Hit pipe!")
    bird.image = "birddead"
    bird.alive = False


def reset(): #runs on start and reset 
    global bird, top_pipe, bottom_pipe, gap, score
    print ("Back to the start...")
    bird.image = ("bird1")
    bird.center = (75, 50)
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
    bird.speed = 1

    bird.alive = True
    bird.score = 0
    top_pipe.pair_number = 1

reset()



pgzrun.go()