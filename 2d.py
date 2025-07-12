#Program to implement 2D transformation
import pygame, sys, math
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

WIDTH, HEIGHT = 1000, 700
pygame.display.set_caption("2D Transformations: Translation, Scaling, Rotation")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def translate(x, y, tx, ty):
    return x + tx, y + ty

def scale(x, y, sx, sy):
    return x * sx, y * sy

def rotate(x, y, angle_deg):
    angle_rad = math.radians(angle_deg)
    x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return x_new, y_new

def main():
    x1, y1 = 100, 100
    x2, y2 = 100, 400

    tx, ty = 200, 150         
    sx, sy = 1.5, 1.5         
    angle = -45                

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)

       #Translation
        xt1, yt1 = translate(x1, y1, tx, ty)
        xt2, yt2 = translate(x2, y2, tx, ty)
        pygame.draw.line(screen, RED, (xt1, yt1), (xt2, yt2), 2)

        #Scaling
        xs1, ys1 = scale(x1, y1, sx, sy)
        xs2, ys2 = scale(x2, y2, sx, sy)
        pygame.draw.line(screen, GREEN, (xs1, ys1), (xs2, ys2), 2)

        #Rotation
        xr1, yr1 = rotate(x1, y1, angle)
        xr2, yr2 = rotate(x2, y2, angle)
        pygame.draw.line(screen, BLUE, (xr1, yr1), (xr2, yr2), 2)

        pygame.display.flip()

if __name__ == "__main__":
    main()