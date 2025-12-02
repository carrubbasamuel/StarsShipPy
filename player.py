import pygame
import os
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        """Inizializza il giocatore (navicella)"""
        super().__init__(group)
        
        # Carica l'immagine della navicella
        image_path = os.path.join(os.path.dirname(__file__), 'spaceship.png')
        if os.path.exists(image_path):
            self.image = pygame.image.load(image_path).convert_alpha()
            # Ridimensiona se necessario
            self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        else:
            # Fallback: disegna la navicella se l'immagine non c'è
            self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
            self.draw_spaceship(self.image)
        
        # Rettangolo per collisioni
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
    
    def draw_spaceship(self, surface):
        """Disegna una navicella triangolare (fallback)"""
        # Punti del triangolo
        points = [
            (PLAYER_SIZE // 2, 0),           # punta su
            (PLAYER_SIZE, PLAYER_SIZE),      # angolo basso destra
            (PLAYER_SIZE // 2, PLAYER_SIZE * 0.7),  # mezzo
            (0, PLAYER_SIZE)                 # angolo basso sinistra
        ]
        pygame.draw.polygon(surface, CYAN, points)
        # Aggiungi una finestra
        pygame.draw.circle(surface, YELLOW, (PLAYER_SIZE // 2, PLAYER_SIZE // 3), 3)
        
        # Velocità
        self.speed_x = 0
        self.speed_y = 0
        
        # Input
        self.update_input()
    
    def update_input(self):
        """Aggiorna l'input da tastiera"""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed_x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed_x = PLAYER_SPEED
        else:
            self.speed_x = 0
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed_y = -PLAYER_SPEED
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed_y = PLAYER_SPEED
        else:
            self.speed_y = 0
    
    def update(self):
        """Aggiorna la posizione del giocatore"""
        self.update_input()
        
        # Aggiorna posizione
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Limiti dello schermo
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    

