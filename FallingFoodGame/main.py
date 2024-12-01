from parameters import *
from game import Game

pygame.init()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling food game")

FPS = 60
clock = pygame.time.Clock()

background = pygame.image.load("resources/background.jfif").convert_alpha()
background = pygame.transform.scale(background, (width, height))
background.set_alpha(128)


game = Game()

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        game.player.move_left()
    if pressed[pygame.K_RIGHT]:
        game.player.move_right()

    screen.fill("black")
    screen.blit(background, (0, 0))
    game.play(screen)
    pygame.display.update()

pygame.quit()
