import pygame
import time
import random
from player import Player
from background import Background

class App:

    displayWidth = 1000
    displayHeight = 800
    floorHeight = 200
    # This is the extra space between the players feet and the bottom of the image
    playerImageExtra = 20
    framesPerSec = 30

    def __init__(self):
        self.gameOver = False
        self.gameExit = False

        screenDim = (self.displayWidth, self.displayHeight)
        gameTitle = 'Game Title'


        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        pygame.init()
        self.gameDisplay = pygame.display.set_mode(screenDim)
        pygame.display.set_caption(gameTitle)

        self.clock = pygame.time.Clock()

        font = pygame.font.SysFont(None, 25)

        self.all_sprites_list = pygame.sprite.Group()

        self.background = Background(self.displayWidth, self.floorHeight, self.displayHeight)
        self.player = Player(self.white, 0, self.displayHeight - self.floorHeight + self.playerImageExtra)

        self.all_sprites_list.add(self.background)
        self.all_sprites_list.add(self.player)

    def message_to_screen(self, msg, color):
        screen_text = pygame.font.render(msg, True, color)
        self.gameDisplay.blit(screen_text, [self.displayWidth / 2, self.displayHeight / 2])

    def gameLoop(self):
        while not self.gameExit:
            self.getEvents()
            self.updateGame()
            self.updateScreen()
            self.drawScreen()
        pygame.quit()
        quit()

    def getEvents(self):
        if self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        self.gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                if event.type == pygame.KEYDOWN:
                  #  if event.key == pygame.K_LEFT:
                     #   lead_x_change = -5
                  #  elif event.key == pygame.K_RIGHT:
                      #  lead_x_change = 5
                    if event.key == pygame.K_UP:
                        self.player.jump()
            #    if event.type == pygame.KEYUP:
             #       if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
             #           lead_x_change = 0
             #           lead_y_change = 0

    def updateGame(self):
        self.player.update()
        self.background.update()
        #        if player.rect.x >= displayWidth or player.rect.x <= 0 or lead_y >= displayHeight or lead_y <= 0:
        #            gameOver = True

    def updateScreen(self):
        self.gameDisplay.fill(self.white)
        if self.gameOver:
            self.message_to_screen("Game over, press C to play again or Q to quit", self.red)
#        else:
#            self.all_sprites_list.update()

    def drawScreen(self):
        if not self.gameOver:
            self.all_sprites_list.draw(self.gameDisplay)

        pygame.display.update()
        self.clock.tick(self.framesPerSec)

if __name__ == "__main__":
    theApp = App()
    theApp.gameLoop()
