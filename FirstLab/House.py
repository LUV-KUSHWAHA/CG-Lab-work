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
    a,b,c,d = 100,500,900,00
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        #Co-ordinates 
        draw_line_dda(a,a,a,b)
        draw_line_dda(a,a,c,a)
        draw_line_dda(a,b,c,b)
        draw_line_dda(c,a,c,b)
        draw_line_dda(a,a,(a+c)/2,d)
        draw_line_dda((a+c)/2,d,c,a)
        draw_line_dda(a+300,b,a+300,b-300)
        draw_line_dda(c-300,b,c-300,b-300)
        draw_line_dda(a+300,b-300,c-300,b-300)

        pygame.display.flip()


if __name__ == "__main__":
    main()
        