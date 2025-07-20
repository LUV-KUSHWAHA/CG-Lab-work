import pygame, sys
w,h = 1000,700
white,black = (255,255,255), (0,0,0,)
pygame.init()
pygame.display.set_caption("circle")
screen = pygame.display.set_mode((w,h))

def circle(xc,yc,r):
    x,y = 0,r
    p = 1-r
    screen.set_at((x+xc,y+yc),white)

    while x<=y:
        if p < 0:
            x += 1
            p += 2*x +1
        else:
            x += 1
            y -= 1
            p += 2*x - 2*y +1
        screen.set_at((x + xc ,y + yc),white)
        screen.set_at((-x + xc ,y + yc),white)
        screen.set_at((x + xc ,-y + yc),white)
        screen.set_at((-x + xc ,-y + yc),white)
        screen.set_at((y + xc ,x + yc),white)
        screen.set_at((-y + xc ,x + yc),white)
        screen.set_at((y + xc ,-x + yc),white)
        screen.set_at((-y + xc ,-x + yc),white)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        circle(300,300,200)
        pygame.display.update()

if __name__ == "__main__":
    main()