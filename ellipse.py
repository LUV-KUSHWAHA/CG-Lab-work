#program to implement MIDPOINT ELLIPSE ALGORITHM

import pygame, sys, math
pygame.init()
WHITE,BLACK = (255,255,255),(0,0,0)
WIDTH,HEIGHT = 1000,700
pygame.display.set_caption("Midpoint Ellipse Algo Implementation")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_ellipse_bla(xc,yc,rx,ry):
    x,y = 0,ry
    p1 = ry**2 - rx**2 *ry + 0.25*rx**2
    screen.set_at((x+xc,y+yc),WHITE)
    while 2*ry**2 *x <= 2*rx**2 *y:
        if p1 < 0:
            x += 1
            p1 += 2*ry**2 *x +ry**2
        else:
            x += 1
            y -= 1
            p1 += 2*ry**2 *x -2*rx**2 * y +ry**2
        screen.set_at((x+xc,y+yc),WHITE)
        screen.set_at((x+xc,-y+yc),WHITE)
        screen.set_at((-x+xc,y+yc),WHITE)
        screen.set_at((-x+xc,-y+yc),WHITE)
        
    p2 = ry**2 *(x+0.5)**2 + rx**2 *(y-1)**2 - rx**2 *ry**2
    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 += -2*rx**2 *y + rx**2
        else:
            x += 1
            y -= 1
            p2 += 2*ry**2 *x - 2*rx**2 *y + rx**2
        screen.set_at((x+xc,y+yc),WHITE)
        screen.set_at((x+xc,-y+yc),WHITE)
        screen.set_at((-x+xc,y+yc),WHITE)
        screen.set_at((-x+xc,-y+yc),WHITE)

def main():
    x,y = 400,300
    rx,ry = 300,200
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        draw_ellipse_bla(x,y,rx,ry)
        pygame.display.update()

if __name__ == "__main__":
    main()