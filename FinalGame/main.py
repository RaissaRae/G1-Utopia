import pygame

pygame.init()
screen=pygame.display.set_mode((480,720))
screen.fill((33,33,33))

# start=pygame.image.load("py\\game\\start.png")#need to make an image
start=pygame.image.load("C:/Users/Rae/Downloads/game (2)/FinalGame/START (1).jpg")
start_rect = start.get_rect()
start_rect.top = 360
start_rect.left = 15
screen.blit(start, start_rect)

pygame.display.update()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if start_rect.collidepoint(x,y):
                import pquest
                pquest
                running=False