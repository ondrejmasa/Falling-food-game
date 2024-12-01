import os
import pygame

width = 500
height = 600

player_size = 120
food_size = 70


def get_good_food_images():
    lst = []
    images = []
    for image in os.listdir("resources/food/good"):
        lst.append(image.split(".")[0])
    for food in lst:
        image = pygame.image.load(f"resources/food/good/{food}.png")
        image = pygame.transform.scale(image, (food_size, food_size))
        images.append(image)
    return images


def get_bad_food_images():
    lst = []
    images = []
    for image in os.listdir("resources/food/bad"):
        lst.append(image.split(".")[0])
    for food in lst:
        image = pygame.image.load(f"resources/food/bad/{food}.png")
        image = pygame.transform.scale(image, (food_size, food_size))
        images.append(image)
    return images


good_food_images = get_good_food_images()
bad_food_images = get_bad_food_images()
