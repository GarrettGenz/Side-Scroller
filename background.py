import pygame
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MOVE_SPEED = 5

class Background(pygame.sprite.Sprite):

    groundOne = GREEN
    groundTwo = BLUE

    def __init__(self,  width, height, displayHeight):
        super().__init__()

        self.width = width
        self.height = height
        self.displayHeight = displayHeight

        self.x = 0
        self.y = self.displayHeight - self.height

        self.image = pygame.Surface([width * 2, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, self.groundOne, [0, 0, width, height])
        pygame.draw.rect(self.image, self.groundTwo, [width, 0, width, height])

        self.rect = self.image.get_rect()

    def swapGround(self):
        if self.groundOne == GREEN:
            self.groundOne = BLUE
            self.groundTwo = GREEN
        else:
            self.groundOne = GREEN
            self.groundTwo = BLUE

        pygame.draw.rect(self.image, self.groundOne, [0, 0, self.width, self.height])
        pygame.draw.rect(self.image, self.groundTwo, [self.width, 0, self.width, self.height])

    def update(self):
        self.x = self.x - MOVE_SPEED

        # If the end of the ground has been reached
        if self.x < -(self.width):
            self.swapGround()
            self.x = 0
            self.y = self.displayHeight - self.height

        self.rect.x = self.x
        self.rect.y = self.y
