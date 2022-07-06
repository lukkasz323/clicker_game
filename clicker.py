import pygame

class Business:
    def __init__(self):
        self.credits = 0

def update_screen(b):
    print(f'[MINE]\n Credits: {b.credits}')      

def main():
    WIDTH, HEIGHT = 960, 540
    
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
            
    pygame.quit()

if __name__ == '__main__':
    main()