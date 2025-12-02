import pygame
from config import *

class StarField(pygame.sprite.Sprite):
    """Sfondo con stelle che si muovono per dare l'effetto di movimento"""
    def __init__(self, group, layer=0):
        """Inizializza lo starfield"""
        super().__init__(group)
        
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = layer * SCREEN_HEIGHT
        
        # Disegna le stelle
        self.image.fill(BACKGROUND_COLOR)
        pygame.draw.circle(self.image, WHITE, (100, 50), 1)
        pygame.draw.circle(self.image, WHITE, (200, 150), 1)
        pygame.draw.circle(self.image, WHITE, (300, 80), 1)
        pygame.draw.circle(self.image, WHITE, (400, 200), 1)
        pygame.draw.circle(self.image, WHITE, (500, 120), 1)
        pygame.draw.circle(self.image, WHITE, (600, 180), 1)
        pygame.draw.circle(self.image, WHITE, (700, 70), 1)
        pygame.draw.circle(self.image, WHITE, (150, 300), 1)
        pygame.draw.circle(self.image, WHITE, (350, 250), 1)
        pygame.draw.circle(self.image, WHITE, (550, 350), 1)
        pygame.draw.circle(self.image, WHITE, (750, 400), 1)
        pygame.draw.circle(self.image, WHITE, (250, 450), 1)
        
        self.speed = STAR_SPEED
    
    def update(self):
        """Aggiorna la posizione dello starfield"""
        self.rect.y += self.speed
        
        # Se esce dallo schermo, riposiziona
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = -SCREEN_HEIGHT


class ScrollingBackground:
    """Gestisce lo sfondo che scorre"""
    def __init__(self, group):
        """Inizializza lo sfondo scrollante"""
        self.group = group
        self.star_fields = []
        
        # Crea due strati di starfield per effetto continuo
        for i in range(2):
            star = StarField(group, i)
            self.star_fields.append(star)
    
    def update(self):
        """Aggiorna lo sfondo"""
        for star in self.star_fields:
            star.update()
    
    def draw(self, screen):
        """Disegna lo sfondo"""
        self.group.draw(screen)
