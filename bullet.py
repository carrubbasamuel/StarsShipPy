import pygame
from config import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, all_sprites, bullets_group):
        """Inizializza un proiettile"""
        super().__init__(all_sprites, bullets_group)
        
        # Crea l'immagine (un piccolo cerchio giallo)
        self.image = pygame.Surface((BULLET_SIZE, BULLET_SIZE))
        self.image.fill(YELLOW)
        
        # Rettangolo per collisioni
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        
        # Velocità
        self.speed_y = -BULLET_SPEED
    
    def update(self):
        """Aggiorna la posizione del proiettile"""
        self.rect.y += self.speed_y
        
        # Rimuovi proiettile se esce dallo schermo
        if self.rect.bottom < 0:
            self.kill()
