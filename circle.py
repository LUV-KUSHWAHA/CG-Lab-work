#program to implement MIDPOINT CIRCLE ALGORITHM

import pygame, sys
pygame.init()
WHITE,BLACK = (255,255,255),(0,0,0)
WIDTH,HEIGHT = 1000,600
pygame.display.set_caption("Midpoint Circle Algo Implementation")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_circle_bla(xc,yc,r):
    d = 1-r
    x,y = 0,r
    screen.set_at((x+xc,y+yc),WHITE)
    while x <= y:
        if d < 0:
            x += 1
            d += 2*x +1
        else:
            x += 1
            y -= 1
            d += 2*x - 2*y +1
        screen.set_at((x+xc,y+yc),WHITE)
        screen.set_at((x+xc,-y+yc),WHITE)
        screen.set_at((-x+xc,y+yc),WHITE)
        screen.set_at((-x+xc,-y+yc),WHITE)
        screen.set_at((y+xc,x+yc),WHITE)
        screen.set_at((y+xc,-x+yc),WHITE)
        screen.set_at((-y+xc,x+yc),WHITE)
        screen.set_at((-y+xc,-x+yc),WHITE)
        
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        draw_circle_bla(300,300,200)
        pygame.display.update()

if __name__ == "__main__":
    main()