import pygame

WHITE = (255, 255, 255)
platformHeight = 10
platformColor = (23, 89, 155)
MOVE_SPEED = 5

class Platform(pygame.sprite.Sprite):

    x = 0
    y = 0
    length = 0

    def __init__(self, xpos, ypos, length):
        super().__init__()

        self.image = pygame.Surface([length, platformHeight])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, platformColor, [xpos, ypos, length, platformHeight] )

        self.rect = self.image.get_rect()

        self.x = xpos
        self.y = ypos
        self.length = length

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.x -= MOVE_SPEED

    def repaint(self):
        self.color = platformColor
        pygame.draw.rect(self.image, platformColor, [0, 0, self.length, platformHeight])