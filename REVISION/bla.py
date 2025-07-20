import pygame,sys
w,h = 1000,700
white,black = (255,255,255),(0,0,0)
pygame.init()
pygame.display.set_caption("bla")
screen = pygame.display.set_mode((w,h))

def bla(x1,y1,x2,y2):
    dx,dy = abs(x2-x1), abs(y2-y1)
    if x2>x1:
        lx = 1
    else:
        lx = -1
    if y2>y1:
        ly = 1
    else:
        ly = -1
    x,y = x1,y1
    screen.set_at((x,y),white)
    if dx>dy:
        p = 2*dy - dx
        while x != x2:
            if p<0:
                x += lx
                p += 2*dy
            else:
                x += lx
                y += ly
                p += 2*dy - 2*dx
            screen.set_at((x,y),white)
    else:
        p = 2*dx - dy
        while y != y2:
            if p<0:
                y += ly
                p += 2*dx
            else:
                x += lx
                y += ly
                p += 2*dx - 2*dy
            screen.set_at((x,y),white)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        bla(200,100, 400,500)
        pygame.display.flip()

if __name__ == "__main__":
    main()