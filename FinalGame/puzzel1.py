import pygame
import time
import threading

def puzzel1(t):

    pygame.init()
    screen=pygame.display.set_mode((480,720))
    

    screen.fill((33,33,33))
    a1=pygame.image.load("C:/Users/Rae/Downloads/game (2)/FinalGame/a1.png")#change the path accordingly
    a1_rect = a1.get_rect()
    a1_rect.top = 360
    a1_rect.left = 220
    screen.blit(a1, a1_rect)
    a2=pygame.image.load("C:/Users/Rae/Downloads/game (2)/FinalGame/a2.png")#change the path accordingly
    a2_rect = a2.get_rect()
    a2_rect.top = 360
    a2_rect.left = 15
    screen.blit(a2, a2_rect)
    q=pygame.image.load("C:/Users/Rae/Downloads/game (2)/FinalGame/design.png")#change the path accordingly
    q_rect = q.get_rect()
    q_rect.top = 220
    q_rect.left = 15
    screen.blit(q, q_rect)

    pygame.display.update()

    print(t)
    
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if a1_rect.collidepoint(x,y):
                    from results import results
                    results(10, t)
                    running=False
                elif a2_rect.collidepoint(x,y):
                    from results import results
                    results(0, t)
                    running=False