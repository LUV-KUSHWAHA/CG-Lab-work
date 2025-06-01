#Program to implement DDA Line Algorithm
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Algorithm")
white = (255,255,255)
black = (0,0,0)

def draw_line_dda(x1,y1,x2,y2):
    dx,dy = x2-x1, y2-y1
    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)
    Xinc = dx/step
    Yinc = dy/step
    x,y = x1,y1
    screen.set_at((round(x),round(y)),white)
    while x != x2 or y != y2:
        x += Xinc
        y += Yinc
        screen.set_at((round(x), round(y)),white)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        draw_line_dda(10,10,500,500)
        pygame.display.flip()

if __name__ == "__main__":
    main()
        