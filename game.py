import pygame
from config import *
from player import Player
from enemy import Asteroid
from explosion import Explosion
from background import ScrollingBackground
import random

class Game:
    def __init__(self):
        """Inizializza il gioco"""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids Escape - Schiva gli Asteroidi!")
        
        # Grup di sprite
        self.all_sprites = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()
        
        # Sfondo scrollante
        self.background = ScrollingBackground(self.background_group)

        # Esplosione
        self.explosions = pygame.sprite.Group()
        
        # Giocatore
        self.player = Player(self.all_sprites)
        
        # Spawn asteroidi iniziali
        self.spawn_asteroids()
        
        # Punteggio e stato
        self.score = 0
        self.time_survived = 0
        self.asteroid_spawn_timer = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.game_over_time = 0
        self.player_hit = False  # Flag per sapere se la navicella è stata colpita
    
    def spawn_asteroids(self, count=3):
        """Genera asteroidi"""
        for _ in range(count):
            asteroid = Asteroid(self.all_sprites, self.asteroids, size="big")
            self.all_sprites.add(asteroid)
    
    def handle_event(self, event):
        """Gestisce gli eventi"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and self.game_over:
                self.restart()
    
    def update(self):
        """Aggiorna la logica del gioco"""
        # Aggiorna sfondo
        self.background.update()
        
        # Aggiorna tutti gli sprite (incluse esplosioni)
        self.all_sprites.update()
        self.explosions.update()
        
        # Se la navicella è stata colpita, aspetta che l'esplosione finisca
        if self.player_hit:
            self.game_over_time += 1
            if self.game_over_time > 60:  # Aspetta 1 secondo
                self.game_over = True
            return
        
        if self.game_over:
            self.game_over_time += 1
            return
        
        # Aggiorna tempo sopravvissuto
        self.time_survived += 1
        self.score = self.time_survived // 60  # Punteggio in secondi
        
        # Controllo collisioni: asteroidi vs giocatore
        if pygame.sprite.spritecollide(self.player, self.asteroids, False):
            explosion = Explosion(self.player.rect.centerx, self.player.rect.centery, self.all_sprites, self.explosions)
            self.player.kill()
            self.player_hit = True
            self.game_over_time = 0
        
        # Spawn asteroidi periodici (aumenta con il tempo)
        self.asteroid_spawn_timer += 1
        spawn_rate = max(40, 120 - (self.score // 5) * 5)  # Più veloce col tempo
        if self.asteroid_spawn_timer > spawn_rate:
            self.spawn_asteroids(random.randint(1, 2))
            self.asteroid_spawn_timer = 0
    
    def draw(self):
        """Disegna tutto sullo schermo"""
        # Disegna sfondo
        self.background_group.draw(self.screen)
        self.screen.fill(BACKGROUND_COLOR)
        self.background_group.draw(self.screen)
        
        # Disegna sprite
        self.all_sprites.draw(self.screen)
        self.explosions.draw(self.screen)
        
        # UI
        score_text = self.font.render(f"Tempo: {self.score}s", True, WHITE)
        asteroids_text = self.font.render(f"Asteroidi: {len(self.asteroids)}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(asteroids_text, (10, 50))
        
        # Game Over
        if self.game_over:
            game_over_font = pygame.font.Font(None, 72)
            game_over_text = game_over_font.render("GAME OVER", True, RED)
            score_text_big = pygame.font.Font(None, 48).render(f"Tempo: {self.score}s", True, YELLOW)
            restart_text = self.font.render("Premi R per ricominciare", True, WHITE)
            
            self.screen.blit(
                game_over_text,
                (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 150)
            )
            self.screen.blit(
                score_text_big,
                (SCREEN_WIDTH // 2 - score_text_big.get_width() // 2, SCREEN_HEIGHT // 2 - 50)
            )
            self.screen.blit(
                restart_text,
                (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 80)
            )
        
        pygame.display.flip()
    
    def restart(self):
        """Riavvia il gioco"""
        self.__init__()
