import pygame


class Hearth:
    def __init__(self):
        self.size = 40
        self.image = pygame.transform.scale(pygame.image.load("resources/hearth.png"), (self.size, self.size))

    def draw(self, screen, position):
        screen.blit(self.image, position)
