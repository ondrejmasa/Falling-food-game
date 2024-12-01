from player import Player
from food import *
from text import Text
from hearth import Hearth


class Game:
    def __init__(self):
        self.player = Player()
        self.hearth = Hearth()
        self.current_food = []
        self.lives = 3
        self.delta = 500
        self.upper_border = 600 + self.delta
        self.lower_border = 200 + self.delta
        self.next_step_time = pygame.time.get_ticks()
        self.game_over = False
        self.score = 0
        self.vomit_sound = pygame.mixer.Sound("resources/vomit.mp3")
        self.bite_sound = pygame.mixer.Sound("resources/bite.mp3")

    def get_random_food(self):
        random_number = random.randint(0, 11)
        self.current_food.append(GoodFood() if random_number < 8 else BadFood())

    def eat_food(self):
        for food in self.current_food:
            if height-self.player.size <= food.y+food.size//2 < height-food.size//2:
                if (self.player.x <= food.x <= self.player.x + self.player.size
                        or self.player.x <= food.x + food.size <= self.player.x + self.player.size):
                    if not food.poisonous:
                        self.score += 1
                        self.bite_sound.play()
                        self.current_food.remove(food)
                    else:
                        self.vomit_sound.play()
                        self.game_over = True
            if not food.poisonous and food.y >= height:
                self.lives -= 1
                self.current_food.remove(food)
                if self.lives <= 0:
                    self.game_over = True

    def spawn_food(self):
        time = pygame.time.get_ticks()
        if time > self.next_step_time:
            self.get_random_food()
            self.delta *= 0.99
            self.upper_border = 600 + int(self.delta)
            self.lower_border = 200 + int(self.delta)
            self.next_step_time += random.randint(self.lower_border, self.upper_border)

    def play(self, screen):
        self.vomit_sound.set_volume(0.1)
        self.bite_sound.set_volume(0.1)
        if not self.game_over:
            self.spawn_food()
            self.eat_food()
            self.draw(screen)
        else:
            self.draw_game_over(screen)

    def reset(self):
        self.current_food = []
        self.lives = 3
        self.delta = 500
        self.score = 0
        self.next_step_time = pygame.time.get_ticks()
        self.game_over = False

    def draw(self, screen):
        self.player.draw(screen)
        for food in self.current_food:
            food.draw(screen)
        score_text = Text(50, f"{self.score}", "white", (width-30, 30))
        score_text.draw(screen)
        for i in range(self.lives):
            self.hearth.draw(screen, (20 + i*self.hearth.size, 10))

    def draw_game_over(self, screen):
        game_over_text = Text(80, "GAME OVER!", "white", (width//2, height//2))
        game_over_text.draw(screen)
        score_text = Text(40, f"score: {self.score}", "white", (width//2, height//2 + 40))
        score_text.draw(screen)
