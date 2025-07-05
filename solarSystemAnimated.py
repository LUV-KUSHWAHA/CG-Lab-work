#program to implement ANIMATED SOLAR SYSTEM

import pygame, sys, math
pygame.init()

WHITE,BLACK,RED = (255,255,255),(0,0,0),(193,68,14)
YELLOW,BLUE = (255,255,150),(0,100,200)
GRAY = (150,150,150)
YELLOWISH_WHITE = (230,230,200)
JUP,GOLD = (200,160,130), (220,200,150)
CYAN, DEEP_BLUE = (150,220,230), (50,80,200)

WIDTH,HEIGHT = 1000,700
FPS = 60
pygame.display.set_caption("Animated Solar System Implementation")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

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

def draw_ellipse_bla(xc,yc,rx,ry):
    x,y = 0,ry
    p1 = ry**2 - rx**2 *ry + 0.25*rx**2
    screen.set_at((x+xc,y+yc),WHITE)
    while 2*ry**2 *x <= 2*rx**2 *y:
        if p1 < 0:
            x += 1
            p1 += 2*ry**2 *x +ry**2
        else:
            x += 1
            y -= 1
            p1 += 2*ry**2 *x -2*rx**2 * y +ry**2
        screen.set_at((x+xc,y+yc),WHITE)
        screen.set_at((x+xc,-y+yc),WHITE)
        screen.set_at((-x+xc,y+yc),WHITE)
        screen.set_at((-x+xc,-y+yc),WHITE)
    p2 = ry**2 *(x+0.5)**2 + rx**2 *(y-1)**2 - rx**2 *ry**2
    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 += -2*rx**2 *y + rx**2
        else:
            x += 1
            y -= 1
            p2 += 2*ry**2 *x - 2*rx**2 *y + rx**2
        screen.set_at((x+xc,y+yc),WHITE)
        screen.set_at((x+xc,-y+yc),WHITE)
        screen.set_at((-x+xc,y+yc),WHITE)
        screen.set_at((-x+xc,-y+yc),WHITE)

def draw_sphere(x,y,radius,color):
    for r in range(0,radius):
        draw_circle_bla(x,y,r,color)

def animation(x,y,rx,ry,theta):
    draw_ellipse_bla(x,y,rx,ry)
    rad = math.radians(theta)
    xc = x + rx * math.cos(rad)
    yc = y + ry * math.sin(rad)
    return xc,yc
        
def main():
    global theta
    x,y = 500,350
    theta = 0
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        draw_sphere(x,y,30,YELLOW) #sun
        #planets_orbit
        xc,yc = animation(x,y,90,60,theta*2.75)
        draw_sphere(int(xc),int(yc),5,GRAY) #Mercury
        xc,yc = animation(x,y,130,90,theta*2.5)
        draw_sphere(int(xc),int(yc),10,YELLOWISH_WHITE) #Venus
        xc,yc = animation(x,y,170,120,theta*2.25)
        draw_sphere(int(xc),int(yc),10,BLUE) #Earth
        xc,yc = animation(x,y,210,150,theta*2)
        draw_sphere(int(xc),int(yc),7,RED) #Mars
        xc,yc = animation(x,y,250,180,theta*1.75)
        draw_sphere(int(xc),int(yc),20,JUP) #Jupiter
        xc,yc = animation(x,y,320,210,theta*1.5)
        draw_sphere(int(xc),int(yc),18,GOLD) #Saturn
        xc,yc = animation(x,y,390,240,theta*1.25)
        draw_sphere(int(xc),int(yc),14,CYAN) # Uranus
        xc,yc = animation(x,y,450,270,theta)
        draw_sphere(int(xc),int(yc),14,DEEP_BLUE) #Neptune

        theta = (theta + 2) # theta = (theta+2) % 36o

        pygame.display.update()

if __name__ == "__main__":
    main()