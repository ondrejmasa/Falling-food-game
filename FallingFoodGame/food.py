from parameters import *
import random


class Food:
    def __init__(self, image):
        self.size = food_size
        self.x = random.randint(0, width - food_size)
        self.y = -food_size
        self.image = image
        self.speed = 6

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.y += self.speed


class GoodFood(Food):
    def __init__(self):
        super().__init__(image=random.choice(good_food_images))
        self.poisonous = False


class BadFood(Food):
    def __init__(self):
        super().__init__(image=random.choice(bad_food_images))
        self.poisonous = True
