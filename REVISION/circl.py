import pygame, sys
width, height = 1000,700
white, black = (255,255,255), (0,0,0)
pygame.init()
pygame.display.set_caption("circle")
screen = pygame.display.set_mode((width,height))

def circle(xc,yc,r):
    p = 1-r
    x,y = 0,r
    screen.set_at((x+xc, y+yc),white)

    while x<=y:
        if p < 0:
            x += 1
            p += 2*x +1
        else:
            x += 1
            y -= 1
            p += 2*x - 2*y + 1
        screen.set_at((x+xc, y+yc),white)
        screen.set_at((-x+xc, y+yc),white)
        screen.set_at((x+xc, -y+yc),white)
        screen.set_at((-x+xc, -y+yc),white)
        screen.set_at((y+xc, x+yc),white)
        screen.set_at((-y+xc, x+yc),white)
        screen.set_at((y+xc, -x+yc),white)
        screen.set_at((-y+xc, -x+yc),white)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        circle(300,400, 50)
        pygame.display.flip()
if __name__== "__main__":
    main()