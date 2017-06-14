import pygame
import time
import random
from player import Player
from background import Background
from platform import Platform
from asteroid import Asteroid

class App:

    displayWidth = 1000
    displayHeight = 800
    floorHeight = 200
    # This is the extra space between the players feet and the bottom of the image
    playerImageExtra = 20
    framesPerSec = 60

    score = 0
    scoreCounter = 0

    platformCounter = 0
    platformFreq = 150

    asteroidCounter = 0
    asteroidFreq = 100

    def __init__(self):
        self.gameOver = False
        self.gameExit = False

        screenDim = (self.displayWidth, self.displayHeight)
        gameTitle = 'Robot Runner'


        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        pygame.init()
        self.gameDisplay = pygame.display.set_mode(screenDim)
        pygame.display.set_caption(gameTitle)
        random.seed()

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(None, 35)

        self.platformList = []
        self.asteroidList = []

        self.all_sprites_list = pygame.sprite.Group()
        self.playerSprite = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        self.background = Background(self.displayWidth, self.floorHeight, self.displayHeight)
        self.player = Player(self.white, 0, self.displayHeight - self.floorHeight + self.playerImageExtra)

        self.all_sprites_list.add(self.background)
        #self.all_sprites_list.add(self.player)
        self.playerSprite.add(self.player)

    def messageToScreen(self, msg, color):
        screen_text = self.font.render(msg, True, color)
        self.gameDisplay.blit(screen_text, [self.displayWidth / 4, self.displayHeight / 2])

    def showScore(self):
        screen_text = self.font.render("Score: " + str(self.score), True, self.black)
        self.gameDisplay.blit(screen_text, [self.displayWidth - 200, 0])

    def createPlatform(self):
        self.platformList.append(Platform(self.displayWidth + random.randrange(0, 400), random.randrange(0, 600),
                                          random.randrange(40, 1000)))
        self.all_sprites_list.add(self.platformList[len(self.platformList) - 1])
        self.platforms.add(self.platformList[len(self.platformList) - 1])

    def createAsteroid(self):
        self.asteroidList.append(Asteroid(self.displayWidth + random.randrange(0, 400), random.randrange(0, 600)))
        self.all_sprites_list.add(self.asteroidList[len(self.asteroidList) - 1])
        self.asteroids.add(self.asteroidList[len(self.asteroidList) - 1])

    def onSurface(self):
        if self.player.isJumping:
            if self.player.v < 0:
                for platform in self.platforms:
                    if pygame.sprite.collide_rect(self.player, platform):
                        if self.player.y + self.player.playerHeight - self.playerImageExtra < platform.rect.y:
                            self.player.y = platform.rect.y - self.player.playerHeight
                            self.player.isJumping = False
                            self.player.onGround = True
                            self.player.image = self.player.walkImages[self.player.index]
                            self.player.v = 9
                            print ("On Platform")
                            break
                if self.player.y > self.displayHeight - self.floorHeight + self.playerImageExtra - self.player.playerHeight - 100:
                    self.player.y = self.displayHeight - self.floorHeight + self.playerImageExtra - self.player.playerHeight
                    self.player.isJumping = False
                    self.player.image = self.player.walkImages[self.player.index]
                    self.player.v = 9

    def checkAsteroids(self):
        for asteroid in self.asteroids:
            if pygame.sprite.collide_rect(self.player, asteroid):
                self.gameOver = True

    def updateScore(self):
        self.scoreCounter += 1
        if self.scoreCounter >= 50:
            self.score += 10
            self.scoreCounter = 0


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
                if event.type == pygame.QUIT:
                    self.gameExit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.jump()

    def updateGame(self):
        if not self.gameOver:
            self.player.update()
            self.background.update()
            self.updateScore()

            self.platformCounter += 1
            if self.platformCounter > self.platformFreq:
                self.createPlatform()
                self.platformCounter = 0

            self.asteroidCounter += 1
            if self.asteroidCounter > self.asteroidFreq:
                self.createAsteroid()
                self.asteroidCounter = 0

            self.onSurface()
            for platform in self.platforms:
                platform.update()

            for asteroid in self.asteroids:
                asteroid.update()

            self.checkAsteroids()

    def updateScreen(self):
        self.gameDisplay.fill(self.white)
        if self.gameOver:
            self.messageToScreen("Game over. Score: " + str(self.score), self.red)
        else:
            self.showScore()
#            self.all_sprites_list.update()

    def drawScreen(self):
        if not self.gameOver:
            for platform in self.platforms:
                platform.repaint()

            self.all_sprites_list.draw(self.gameDisplay)
            self.asteroids.draw(self.gameDisplay)
            self.playerSprite.draw(self.gameDisplay)

        pygame.display.update()
        self.clock.tick(self.framesPerSec)

if __name__ == "__main__":
    theApp = App()
    theApp.gameLoop()
