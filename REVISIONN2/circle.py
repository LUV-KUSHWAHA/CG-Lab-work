import pygame, sys
WIDTH, HEIGHT = 1000,700
WHITE, BLACK = (255,255,255),(0,0,0)

pygame.init()
pygame.display.set_caption("circle")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def circle(xc,yc,r):
    x,y = 0,r
    d = 1-r
    points = [(x,y),(-x,y),(x,-y),(-x,-y),(y,x),(-y,x),(y,-x),(-y,-x)]
    for px,py in points:
        screen.set_at((px+xc,py+yc),WHITE)

    while x<=y:
        if d<0:
            x += 1
            d += 2*x + 1
        else:
            x += 1
            y -= 1
            d += 2*x - 2*y + 1
        points = [(x,y),(-x,y),(x,-y),(-x,-y),(y,x),(-y,x),(y,-x),(-y,-x)]
        for px,py in points:
            screen.set_at((px+xc,py+yc),WHITE)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        circle(300,200,100)
        pygame.display.flip()

if __name__=="__main__":
    main()