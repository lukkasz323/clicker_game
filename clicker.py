import pygame

class Business:
    def __init__(self):
        self.credits = 0

def main():
    WIDTH, HEIGHT = 960, 540
    FRAMERATE = 60
    
    # Initial tasks.
    pygame.init()
    W = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mine Clicker')
    clock = pygame.time.Clock()
    
    # Tasks ran every frame.
    run = True
    while run:
        # Keep steady framerate.
        clock.tick(FRAMERATE)
        
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] is True:
                print('LMB down!')
        
        # Draw
        W.fill((16, 16, 16)) # Background
        
        # Update screen.
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()