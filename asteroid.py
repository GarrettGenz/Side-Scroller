import pygame

WHITE = (255, 255, 255)
MOVE_SPEED = 10
ASTEROID_COLOR = (255, 0, 0)

class Asteroid(pygame.sprite.Sprite):

    x = 0
    y = 0

    def loadImage(self, name):
        image = pygame.image.load(name).convert_alpha()
        image = pygame.transform.scale(image, (30, 30))
        return image

    def __init__(self, xpos, ypos):
        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.asteroidImage = self.loadImage('images/Asteroid.png')

        self.x = xpos
        self.y = ypos

        self.image = self.asteroidImage

    def update(self):
        self.rect = self.image.get_rect()
        self.x -= MOVE_SPEED
        self.rect.x = self.x
        self.rect.y = self.y