#program to implement MIDPOINT CIRCLE ALGORITHM

import pygame, sys
pygame.init()
WHITE,BLACK,RED = (255,255,255),(0,0,0),(193,68,14)
YELLOW,BLUE = (255,255,150),(0,100,200)
GRAY = (150,150,150)
YELLOWISH_WHITE = (230,230,200)
JUP,GOLD = (200,160,130), (220,200,150)
CYAN, DEEP_BLUE = (150,220,230), (50,80,200)

WIDTH,HEIGHT = 700,700
pygame.display.set_caption("Midpoint Circle Algo Implementation")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_circle_bla(xc,yc,r,color = WHITE):
    d = 1-r
    x,y = 0,r
    screen.set_at((x+xc,y+yc),color)
    while x <= y:
        if d < 0:
            x += 1
            d += 2*x +1
        else:
            x += 1
            y -= 1
            d += 2*x - 2*y +1
        screen.set_at((x+xc,y+yc),color)
        screen.set_at((x+xc,-y+yc),color)
        screen.set_at((-x+xc,y+yc),color)
        screen.set_at((-x+xc,-y+yc),color)
        screen.set_at((y+xc,x+yc),color)
        screen.set_at((y+xc,-x+yc),color)
        screen.set_at((-y+xc,x+yc),color)
        screen.set_at((-y+xc,-x+yc),color)

def draw_sphere(x,y,radius,color):
    for r in range(0,radius):
        draw_circle_bla(x,y,r,color)
        
def main():
    x,y = 350,350
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        draw_sphere(x,y,30,YELLOW) #sun
        #planets_orbit
        draw_circle_bla(x,y,50)
        draw_circle_bla(x,y,80)
        draw_circle_bla(x,y,110)
        draw_circle_bla(x,y,140)
        draw_circle_bla(x,y,170)
        draw_circle_bla(x,y,200)
        draw_circle_bla(x,y,230)
        draw_circle_bla(x,y,260)
        # planets
        draw_sphere(x+50,y,5,GRAY) #Mercury
        draw_sphere(x,y+80,10,YELLOWISH_WHITE) #Venus
        draw_sphere(x+110,y,10,BLUE) #Earth
        draw_sphere(x-140,y,7,RED) #Mars
        draw_sphere(x,y-170,20,JUP) #Jupiter
        draw_sphere(x+200,y,18,GOLD) #Saturn
        draw_sphere(x,y-230,14,CYAN) # Uranus
        draw_sphere(x-260,y,14,DEEP_BLUE) #Neptune

        pygame.display.update()

if __name__ == "__main__":
    main()