import pygame

class Business:
    def __init__(self):
        self.credits = 0

def main():
    WIDTH, HEIGHT = 512, 512
    FRAMERATE = 60
    
    # Initial tasks.
    pygame.init()
    
    W = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mine Clicker')
    
    FONT_SMALL = pygame.font.SysFont('tahoma', 16)
    FONT_MEDIUM = pygame.font.SysFont('tahoma', 24)
    FONT_LARGE = pygame.font.SysFont('tahoma', 32)
    logo = FONT_LARGE.render('Mine Clicker', True, 'yellow')
    
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
                
        # Logic
        fps = round(clock.get_fps())
        text_fps = FONT_SMALL.render(f'{fps}', True, 'white')
        
        # Draw
        W.fill((16, 16, 16)) # Background
        W.blit(logo, (16, 8))
        W.blit(text_fps, (480, 8))
        
        # Update screen.
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()