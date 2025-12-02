import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, all_sprites, explosions_group):
        """Inizializza un'esplosione"""
        super().__init__(all_sprites, explosions_group)
        
        # Crea l'immagine (un cerchio che si espande)
        self.max_radius = 80  # Più grande
        self.current_radius = 5
        self.image = pygame.Surface((self.max_radius * 2, self.max_radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.growth_rate = 1.5  # Più lento

    def update(self):
        """Aggiorna l'esplosione"""
        if self.current_radius < self.max_radius:
            self.current_radius += self.growth_rate
            self.image.fill((0, 0, 0, 0))  # Pulisce l'immagine
            
            # Cerchio principale arancione
            pygame.draw.circle(self.image, (255, 150, 0), (self.max_radius, self.max_radius), int(self.current_radius))
            
            # Cerchio interno giallo (nucleo)
            inner_radius = max(1, int(self.current_radius * 0.6))
            pygame.draw.circle(self.image, (255, 255, 0), (self.max_radius, self.max_radius), inner_radius)
            
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.kill()  # Rimuovi l'esplosione quando raggiunge la dimensione massima

