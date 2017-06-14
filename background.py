import pygame
import time
import random
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MOVE_SPEED = 5

class Background(pygame.sprite.Sprite):

    groundOne = GREEN
    groundTwo = BLUE

    def loadImage(self, name):
        image = pygame.image.load(name).convert_alpha()
        image = pygame.transform.scale(image, (1000 * 2, 800))
        return image

    def __init__(self,  width, height, displayHeight):
        super().__init__()

        self.width = width
        self.height = height
        self.displayHeight = displayHeight

        self.x = 0
        self.y = self.displayHeight - self.height

        random.seed()

        self.image = pygame.Surface([width * 2, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.groundImage = self.loadImage('images/Ground.png')

        self.image = self.groundImage

    def update(self):
        self.rect = self.image.get_rect()
        self.x = self.x - MOVE_SPEED

        # If the end of the ground has been reached
        if self.x < -(self.width):
            # Draw the second piece of ground in the beginning of the surface
            self.image.blit(self.image, (0, 0), (self.width, 0, self.width, self.height))

            self.x = 0
            self.y = self.displayHeight - self.height

        self.rect.x = self.x
        self.rect.y = self.y
