#Program to implement DDA Line Algorithm
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Algorithm")
white = (255,255,255)
black = (0,0,0)

def draw_line_bla(x1,y1,x2,y2):
    dx,dy = abs(x2 - x1), abs(y2 - y1)
    x,y = x1,y1
    if x2 > x1:
        lx = 1
    else:
        lx = -1
    if y2 > y1:
        ly = 1
    else:
        ly = -1
    screen.set_at((x,y),white)

    if dx > dy:
        p = 2*dy - dx
        while x != x2:
            x += lx
            if p < 0:
                p += 2*dy
            else:
                y += ly
                p += 2*dy - 2*dx
            screen.set_at((x,y),white)
    else:
        p = 2*dx - dy
        while y != y2:
            y += ly
            if p < 0:
                p += 2*dy
            else:
                x += lx
                p += 2*dx - 2*dy
            screen.set_at((x,y),white)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        draw_line_bla(10,10,500,500)
        pygame.display.flip()

if __name__ == "__main__":
    main()
        