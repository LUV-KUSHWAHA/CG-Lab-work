import pygame, sys, math
WIDTH, HEIGHT = 1000, 700
WHITE, BLACK = (255,255,255), (0,0,0)
pygame.init()
pygame.display.set_caption("2D Transformation")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def translate(x,y,tx,ty):
    return x+tx, y+ty

def scale(x,y,sx,sy):
    return x*sx,y*sy

def rotate(x,y,angle_deg):
    angle_rad = math.radians(angle_deg)
    xn = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    yn = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return xn,yn

def main():
    x1,y1 = 100, 100
    x2,y2 = 100, 400
    tx,ty = 100,100
    sx,sy = 1.25,1.25
    angle_deg = -45
    while True:
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE,(x1,y1),(x2,y2),5)

        x1n,y1n = translate(x1,y1,tx,ty)
        x2n,y2n = translate(x2,y2,tx,ty)
        pygame.draw.line(screen, WHITE,(x1n,y1n),(x2n,y2n),5)

        x1n,y1n = scale(x1,y1,sx,sy)
        x2n,y2n = scale(x2,y2,sx,sy)
        pygame.draw.line(screen, WHITE,(x1n,y1n),(x2n,y2n),1)

        x1n,y1n = rotate(x1,y1,angle_deg)
        x2n,y2n = rotate(x2,y2,angle_deg)
        pygame.draw.line(screen, WHITE,(x1n,y1n),(x2n,y2n),3)

        pygame.display.flip()

if __name__ == "__main__":
    main()