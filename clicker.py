import pygame

class Business:
    def __init__(self):
        self.credits = 0
        self.stone = 0

def text(string, font, color='white'):
    return font.render(string, True, color)

def main():
    WIDTH, HEIGHT = 512, 512
    FRAMERATE = 60
    
    # Initial tasks.
    pygame.init()
    
    W = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mine Clicker')
    
    FONT_S = pygame.font.SysFont('tahoma', 18)
    FONT_M = pygame.font.SysFont('tahoma', 20)
    FONT_L = pygame.font.SysFont('tahoma', 32)
    
    clock = pygame.time.Clock()
    b = Business()
    
    # Tasks ran every frame.
    run = True
    while run:
        # Keep steady framerate.
        clock.tick(FRAMERATE)
        
        # Handle events.
        event_mousebuttondown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                event_mousebuttondown = True
                
        # Logic
        fps = round(clock.get_fps())
        mouse_pos = pygame.mouse.get_pos()
        
        text_fps = text(f'{fps}', FONT_M)
        text_credits = text(f'Credits: {b.credits}', FONT_M)
        text_stone = text(f'Stone: {b.stone}', FONT_M)
        
        BUTTON_SELL_STONE = pygame.Rect(8, 64, 32, 32)
        BUTTON_TEST = pygame.Rect(18, 164, 32, 32)
        
        if event_mousebuttondown and pygame.mouse.get_pressed()[0] and BUTTON_SELL_STONE.collidepoint(mouse_pos):
            print(1)
        
        # Draw
        W.fill((16, 16, 16)) # Background
        W.fill('gray20', BUTTON_SELL_STONE)
        W.blits(((text_fps, (480, 8)),
                (text_credits, (16, 16)),
                (text_stone, (48, 64))))
        
        # Update screen.
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()