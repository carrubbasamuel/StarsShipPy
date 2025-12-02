import pygame
import random
import math
from config import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, all_sprites, enemies_group, x=None, y=None, size="big"):
        """Inizializza un asteroide"""
        super().__init__(all_sprites, enemies_group)
        
        self.size = size
        self.size_pixels = {"big": 40, "medium": 25, "small": 15}[size]
        
        # Crea l'immagine (cerchio grigio irregolare)
        self.image = pygame.Surface((self.size_pixels, self.size_pixels), pygame.SRCALPHA)
        self.draw_asteroid(self.image)
        
        # Rettangolo per collisioni
        self.rect = self.image.get_rect()
        
        if x is None:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.size_pixels)
        else:
            self.rect.x = x
        
        if y is None:
            self.rect.y = random.randint(-150, -self.size_pixels)
        else:
            self.rect.y = y
        
        # Velocità
        self.speed_x = random.uniform(-1.5, 1.5)
        self.speed_y = random.uniform(1, 3)
        self.rotation_speed = random.uniform(-5, 5)
        self.angle = 0
    
    def draw_asteroid(self, surface):
        """Disegna un asteroide irregolare"""
        # Disegna un cerchio grigio
        pygame.draw.circle(surface, (150, 150, 150), (self.size_pixels // 2, self.size_pixels // 2), self.size_pixels // 2)
        # Aggiungi delle ombre
        pygame.draw.circle(surface, (100, 100, 100), (self.size_pixels // 3, self.size_pixels // 3), self.size_pixels // 4)
    
    def update(self):
        """Aggiorna la posizione dell'asteroide"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.angle += self.rotation_speed
        
        # Rimbalza sui lati
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        
        # Rimuovi asteroide se esce dal basso
        if self.rect.top > SCREEN_HEIGHT + 100:
            self.kill()
