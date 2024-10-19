import pygame
from trex import Trex
from obstacle import Obstacle
from constants import *
from score_manager import ScoreManager

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Multiplayer Trex Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.trex1 = Trex(1)
        self.trex2 = Trex(2)
        self.obstacle = Obstacle()
        self.score = 0
        self.game_over = False
        self.score_manager = ScoreManager()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and self.game_over:
                if event.key == pygame.K_r:
                    self.reset_game()
        return True

    def reset_game(self):
        self.trex1 = Trex(1)
        self.trex2 = Trex(2)
        self.obstacle.reset()
        self.score = 0
        self.game_over = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.trex1.update(keys)
        self.trex2.update(keys)
        self.obstacle.update()
        if self.obstacle.rect.right < 0:
            self.obstacle.reset()
            self.score += 1
        if self.check_collision(self.trex1) or self.check_collision(self.trex2):
            self.game_over = True
            self.score_manager.add_score(self.score)
        return not self.game_over

    def draw(self):
        self.screen.fill(WHITE)
        self.trex1.draw(self.screen)
        self.trex2.draw(self.screen)
        self.obstacle.draw(self.screen)
        pygame.draw.line(self.screen, BLACK, (0, GROUND_HEIGHT), (SCREEN_WIDTH, GROUND_HEIGHT), 3)
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = self.font.render("Game Over - Press R to Restart", True, BLACK)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))
            
            top_scores = self.score_manager.get_top_scores()
            for i, score in enumerate(top_scores[:5]):
                score_text = self.font.render(f"Top {i+1}: {score}", True, BLACK)
                self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 40 + i * 30))
        
        pygame.display.flip()

    def check_collision(self, trex):
        return trex.rect.colliderect(self.obstacle.rect)

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            if running and not self.game_over:
                running = self.update()
            self.draw()
            self.clock.tick(30)