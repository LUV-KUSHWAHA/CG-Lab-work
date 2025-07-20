import pygame, sys
WIDTH, HEIGHT = 1000,700
WHITE, BLACK = (255,255,255),(0,0,0)

pygame.init()
pygame.display.set_caption("ellipse")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def ellipse(xc,yc,a,b):
    x,y = 0,b
    p = b**2 - a**2 *b + a**2 /4
    points = [(x,y),(-x,y),(x,-y),(-x,-y)]
    for px,py in points:
        screen.set_at((px+xc,py+yc),WHITE)

    while b**2 *x <= a**2 *y:
        if p<0:
            x += 1
            p += 2*b**2 *x + b**2
        else:
            x += 1
            y -= 1
            p += 2*b**2 *x - 2*a**2 *y + b**2
        points = [(x,y),(-x,y),(x,-y),(-x,-y)]
        for px,py in points:
            screen.set_at((px+xc,py+yc),WHITE)

    p = b**2 *(x+0.5)**2 + a**2 *(y-1)**2 - a**2 * b**2
    while y >= 0:
        if p>0:
            y -= 1
            p += -2*a**2 *y + a**2
        else:
            x += 1
            y -= 1
            p += 2*b**2 *x - 2*a**2 *y + a**2
        points = [(x,y),(-x,y),(x,-y),(-x,-y)]
        for px,py in points:
            screen.set_at((px+xc,py+yc),WHITE)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        ellipse(300,200,100,200)
        pygame.display.flip()

if __name__=="__main__":
    main()