import pygame
from pygame.locals import *
import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab

#using https://stackoverflow.com/questions/48093361/using-matplotlib-in-pygame
def results(a,t):
    
    var = a+(0.5*t)
    name = ["ACS", "biology"]
    value = [var, 0]

    fig = pylab.figure(figsize=[4, 4], dpi=100,)
    ax = fig.gca()
    ax.plot(name, value)

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    pygame.init()
    screen=pygame.display.set_mode((480,720))

    screen.fill((33,33,33))
    pygame.display.update()

    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (40,15))
    pygame.display.flip()

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False