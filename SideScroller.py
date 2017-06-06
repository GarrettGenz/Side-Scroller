import pygame

screenDim = (800, 600)
gameTitle = 'Game Title'

def initializeScreen(dim):
    pygame.init()
    gameDisplay = pygame.display.set_mode(screenDim)
    pygame.display.set_caption(gameTitle)

initializeScreen(screenDim)

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)

pygame.quit()

quit()
