import pygame

class Business:
    def __init__(self):
        self.credits = 0

def update_screen(b):
    print(f'[MINE]\n Credits: {b.credits}')      

def main():
    WIDTH, HEIGHT = 960, 540
    FRAMERATE = 60
    
    pygame.init()
    W = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mine Clicker')
    clock = pygame.time.Clock()
    
    run = True
    while run:
        # Keep steady framerate.
        clock.tick(FRAMERATE)
        
        # Handle 'quit' request.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Update screen.
        W.fill((16, 16, 16))
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()