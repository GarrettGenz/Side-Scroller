import pygame
WHITE = (255, 255, 255)

MOVE_SPEED = 10
ANIMATION_SPEED = 5

displayWidth = 1000
displayHeight = 800
floorHeight = 200

class Player(pygame.sprite.Sprite):
    playerWidth = 150
    playerHeight = 150

    x = 0
    y = 0

    isJumping = False

    # Force and Mass
    v = 8
    m = 2

    def loadImage(self, name):
        image = pygame.image.load(name).convert_alpha()
        image = pygame.transform.scale(image, (self.playerWidth, self.playerHeight))
        return image

    def __init__(self, color, startX, startY):
        super().__init__()

        self.index = 0
        self.animationCounter = 0
        self.walkImages = []
        self.jumpImages = []
        self.walkImages.append(self.loadImage('images/Run (1).png'))
        self.walkImages.append(self.loadImage('images/Run (2).png'))
        self.walkImages.append(self.loadImage('images/Run (3).png'))
        self.walkImages.append(self.loadImage('images/Run (4).png'))
        self.walkImages.append(self.loadImage('images/Run (5).png'))
        self.walkImages.append(self.loadImage('images/Run (6).png'))
        self.walkImages.append(self.loadImage('images/Run (7).png'))
        self.walkImages.append(self.loadImage('images/Run (8).png'))
        self.jumpImages.append(self.loadImage('images/Jump.png'))
        self.image = pygame.Surface([self.playerWidth, self.playerHeight])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.groundY = startY - self.playerHeight

        self.x = startX
        self.y = self.groundY

        self.image = self.walkImages[self.index]

    def setSprite(self, path):
        self.image = pygame.image.load(path).convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.playerWidth, self.playerHeight))

        self.rect = self.image.get_rect()

    def jump(self):
        self.isJumping = True
        self.image = self.jumpImages[0]

    def update(self):
        if self.isJumping:
            # Calculate force
            if self.v > 0:
                F = (0.5 * self.m * (self.v * self.v))
            else:
                F = -(0.5 * self.m * (self.v * self.v))

            # Change position
            self.y = self.y - F
            self.v = self.v - 1

            # Stop when you hit the ground
            if self.y > self.groundY:
                self.y = displayHeight - floorHeight - self.playerHeight
                self.y = self.groundY
                self.isJumping = False
                self.image = self.walkImages[self.index]
                self.v = 8
        else:
            self.animationCounter += 1
            if self.animationCounter % ANIMATION_SPEED == 0:
                # Rotate through walking images
                self.index += 1
                if self.index >= len(self.walkImages):
                    self.index = 0
                self.image = self.walkImages[self.index]

                self.animationCounter = 0

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

