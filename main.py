import pygame
import sys
from game import Game

# Inizializza Pygame
pygame.init()

def main():
    """Funzione principale del gioco"""
    game = Game()
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # FPS a 60
        clock.tick(60)
        
        # Gestisci eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
        
        # Aggiorna logica di gioco
        game.update()
        
        # Disegna tutto
        game.draw()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
