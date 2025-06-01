#Program to implement DDA Line Algorithm
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soccer Game Playground")
white = (255,255,255)
green = (0,100,0)

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
                p += 2*dx
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
        screen.fill(green)
        #co-ordinates
        draw_line_bla(10,350,590,350) #center line
        draw_line_bla(10,10,590,10) #top
        draw_line_bla(10,10,10,690) #left
        draw_line_bla(10,690,590,690) #bottom
        draw_line_bla(590,10,590,690) #right
        #centeral box
        draw_line_bla(290,340,290,360)
        draw_line_bla(290,340,310,340)
        draw_line_bla(290,360,310,360)
        draw_line_bla(310,340,310,360)
        #top inner lines
        draw_line_bla(150,10,150,160)
        draw_line_bla(450,10,450,160)
        draw_line_bla(150,160,450,160)
        draw_line_bla(270,30,330,30) #top post
        draw_line_bla(270,10,270,30)
        draw_line_bla(330,10,330,30)
        #bottom inner lines
        draw_line_bla(150,690,150,540)
        draw_line_bla(450,540,450,690)
        draw_line_bla(150,540,450,540)
        draw_line_bla(270,670,330,670) #bottom post
        draw_line_bla(270,690,270,670)
        draw_line_bla(330,690,330,670)

        pygame.display.flip()

if __name__ == "__main__":
    main()
        