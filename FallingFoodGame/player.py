from parameters import *


class Player:
    def __init__(self):
        self.size = player_size
        self.x = width // 2
        self.y = height - player_size
        self.image = pygame.transform.scale(pygame.image.load("resources/head.png"), (player_size, player_size))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 7

    def move_left(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x >= width - self.size:
            self.x = width - self.size

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
