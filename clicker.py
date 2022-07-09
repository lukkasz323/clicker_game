import pygame

class Business:
    def __init__(self):
        self.credits = 0
        self.stone = {'value': 1, 'amount': 0, 'miners': 0, 'miner_cost': 10}
        
    def sell(self, material):
        self.credits += material['amount'] * material['value']
        material['amount'] = 0
        
    def buy_miner(self, material):
        if self.credits >= material['miner_cost']:
            self.credits -= material['miner_cost']
            material['miners'] += 1

def text(string, font, color='white'):
    return font.render(string, True, color)

def main():
    WIDTH, HEIGHT = 512, 512
    FRAMERATE = 60
    
    pygame.init()
    
    clock = pygame.time.Clock()
    b = Business()
    
    W = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mine Clicker')
    
    FONT_S = pygame.font.SysFont('tahoma', 18)
    FONT_M = pygame.font.SysFont('tahoma', 20)
    FONT_L = pygame.font.SysFont('tahoma', 32)
    
    TIMER_1000 = pygame.event.custom_type()
    pygame.time.set_timer(TIMER_1000, 1000)
    
    # Tasks ran every frame.
    run = True
    while run:
        # Keep steady framerate.
        clock.tick(FRAMERATE)
        
        # Handle events.
        event_timer_1000 = False
        event_mousebuttondown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == TIMER_1000:
                event_timer_1000 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                event_mousebuttondown = True
                
        # Logic
        fps = round(clock.get_fps())
        mouse_pos = pygame.mouse.get_pos()
        
        BUTTON_MINE = pygame.Rect(240, 16, 32, 32)
        BUTTON_BUY_MINER_STONE = pygame.Rect(240, 64, 32, 32)
        BUTTON_SELL_STONE = pygame.Rect(8, 64, 32, 32)
        
        if event_timer_1000:
            b.stone['amount'] += b.stone['miners']
        
        if event_mousebuttondown and pygame.mouse.get_pressed()[0]:
            if BUTTON_MINE.collidepoint(mouse_pos):
                b.stone['amount'] += 1
            if BUTTON_BUY_MINER_STONE.collidepoint(mouse_pos):
                b.buy_miner(b.stone)
            if BUTTON_SELL_STONE.collidepoint(mouse_pos):
                b.sell(b.stone)
        
        # Draw
        text_fps = text(f'{fps}', FONT_M)
        text_credits = text(f'Credits: {b.credits}', FONT_M)
        text_stone = text(f"Stone: {b.stone['amount']} [+{b.stone['miners']}/s]", FONT_M)
        text_miner_stone = text(f"{b.stone['miner_cost']}", FONT_M)
        
        W.fill((16, 16, 16)) # Background
        W.fill('yellow', BUTTON_MINE)
        W.fill('gray', BUTTON_BUY_MINER_STONE)
        W.fill('gray30', BUTTON_SELL_STONE)
        W.blits(((text_fps, (480, 8)),
                (text_credits, (16, 16)),
                (text_stone, (48, 64)),
                (text_miner_stone, (288, 64))))
        
        # Update screen.
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()