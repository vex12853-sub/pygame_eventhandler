import pygame
from pygame.locals import *
import sys


SCREEN_SIZE = (320, 140)
clock = pygame.time.Clock()
fullscreen_flag = False
event_handlers = {}
 
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(u"hoge")


def event_handler(event_type):
    def decorator(func):
        event_handlers[event_type] = func
        return func
    return decorator


@event_handler(QUIT)
def on_quit(event):
    pygame.quit()
    sys.exit()

@event_handler(KEYDOWN)
def on_keydown(event):
    global screen
    if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()
    if event.key == K_F2:
        fullscreen_flag = not fullscreen_flag
        if fullscreen_flag:
            screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        else:
            screen = pygame.display.set_mode(SCREEN_SIZE, 0)

@event_handler(MOUSEMOTION)
def on_mouse_motion(event):
    x, y = event.pos
    pygame.draw.line(screen, (255,255,255), (SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2), (x,y), 1)


while True:
    screen.fill((0,0,0))
    clock.tick(120)
    for event in pygame.event.get():
        if event.type in event_handlers:
            event_handlers[event.type](event)
    pygame.display.update()
  
