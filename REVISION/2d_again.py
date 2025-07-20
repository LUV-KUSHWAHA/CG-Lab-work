import pygame, sys, math
W,H = 1000,700
WT,BK = (255,255,255),(0,0,0)
pygame.init()
pygame.display.set_caption("2d Transform")
screen = pygame.display.set_mode((W,H))

def trns(x,y,tx,ty):
    return x+tx, y+ty
def scale(x,y,sx,sy):
    return x*sx, y*sy
def rotate(x,y,ang_deg):
    ang_rad = math.radians(ang_deg)
    xn = x * math.cos(ang_rad) - y* math.sin(ang_rad)
    yn = x * math.sin(ang_rad) + y* math. cos(ang_rad)
    return xn,yn

def main():
    x1,y1 = 100,100
    x2,y2 = 100,400
    tx,ty = 200,200
    sx,sy = 1.2,1.2
    ang_deg = -45

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BK)
        pygame.draw.line(screen,WT,(x1,y1),(x2,y2),5)

        x1n,y1n = trns(x1,y1,tx,ty)
        x2n,y2n = trns(x2,y2,tx,ty)
        pygame.draw.line(screen,WT,(x1n,y1n),(x2n,y2n), 5)

        x1n,y1n = scale(x1,y1,sx,sy)
        x2n,y2n = scale(x2,y2,sx,sy)
        pygame.draw.line(screen,WT,(x1n,y1n),(x2n,y2n), 3)

        x1n,y1n = rotate(x1,y1,ang_deg)
        x2n,y2n = rotate(x2,y2,ang_deg)
        pygame.draw.line(screen,WT,(x1n,y1n),(x2n,y2n), 1)

        pygame.display.flip()
if __name__ == "__main__":
    main()