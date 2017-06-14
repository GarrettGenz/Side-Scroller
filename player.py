import pygame
WHITE = (255, 255, 255)

MOVE_SPEED = 10
ANIMATION_SPEED = 5
JUMP_FORCE = 9
HANGTIME = 2

displayWidth = 1000
displayHeight = 800
floorHeight = 200

class Player(pygame.sprite.Sprite):
    playerWidth = 150
    playerHeight = 150

    x = 0
    y = 0

    isJumping = False
    onGround = True
    jumpCounter = 0

    # Force and Mass
    v = JUMP_FORCE
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

    def jump(self):
        self.isJumping = True
        self.image = self.jumpImages[0]

    def update(self):
        if self.isJumping:

            self.jumpCounter += 1
            if self.jumpCounter % HANGTIME == 0:
                # Calculate force
                if self.v > 0:
                    F = (0.5 * self.m * (self.v * self.v))
                else:
                    F = -(0.5 * self.m * (self.v * self.v))

                # Change position
                self.y = self.y - F
                self.v = self.v - 1

                self.jumpCounter = 0

#        if not self.onGround:
#            self.y = self.y + 10

        else:
            self.animationCounter += 1
         #   self.y = self.y + (0.5 * self.m * (JUMP_FORCE * JUMP_FORCE))
            if self.animationCounter % ANIMATION_SPEED == 0:
                # Rotate through walking images
                self.index += 1
                if self.index >= len(self.walkImages):
                    self.index = 0
                self.image = self.walkImages[self.index]

                self.animationCounter = 0

        self.rect = self.image.get_rect()
        self.rect.y = self.y

