import pygame

class Business:
    def __init__(self):
        self.credits = 0
        self.stone = {'value': 1, 'amount': 0, 'miners': 0}
        
    def sell(self, material):
        material['amount'] = 0
        self.credits += material['amount'] * material['value']

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
        text_stone = text(f"Stone: {b.stone['amount']} [+{b.stone['miners']}/s]", FONT_M)
        
        BUTTON_MINE = pygame.Rect(240, 16, 32, 32)
        BUTTON_BUY_MINER_STONE = pygame.Rect(240, 64, 32, 32)
        BUTTON_SELL_STONE = pygame.Rect(8, 64, 32, 32)
        
        if event_mousebuttondown and pygame.mouse.get_pressed()[0]:
            if BUTTON_MINE.collidepoint(mouse_pos):
                b.stone['amount'] += 1
            if BUTTON_BUY_MINER_STONE.collidepoint(mouse_pos):
                b.stone['miners'] += 1
            if BUTTON_SELL_STONE.collidepoint(mouse_pos):
                b.sell(b.stone)
        
        # Draw
        W.fill((16, 16, 16)) # Background
        W.fill('yellow', BUTTON_MINE)
        W.fill('gray', BUTTON_BUY_MINER_STONE)
        W.fill('gray30', BUTTON_SELL_STONE)
        W.blits(((text_fps, (480, 8)),
                (text_credits, (16, 16)),
                (text_stone, (48, 64))))
        
        # Update screen.
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()