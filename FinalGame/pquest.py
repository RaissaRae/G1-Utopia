import pygame

pygame.init()
screen=pygame.display.set_mode((480,720))
screen.fill((33,33,33))

q0=pygame.image.load("C:/Users/Rae/Downloads/game (2)/FinalGame/q0.png")#change the path accordingly
yes=pygame.image.load("C:/Users/Rae/Downloads/game (2)/FinalGame/yes.png")#change the path accordingly
no=pygame.image.load("C:/Users/Rae/Downloads/game (2)/FinalGame/no.png")#change the path accordingly
q0_rect = q0.get_rect()
yes_rect = yes.get_rect()
no_rect = no.get_rect()
q0_rect.top = 20
q0_rect.left = 15
yes_rect.top = 360
yes_rect.left = 15
no_rect.top = 390
no_rect.left = 15
screen.blit(yes, yes_rect)
screen.blit(no, no_rect)

pygame.display.update()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            import main
            main
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if yes_rect.collidepoint(x,y):
                from puzzel1 import puzzel1
                puzzel1(10)
                running=False
            elif no_rect.collidepoint(x,y):
                from puzzel1 import puzzel1
                puzzel1(0)
                running=False