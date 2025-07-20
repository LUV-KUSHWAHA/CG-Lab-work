import pygame, sys
WIDTH, HEIGHT = 1000,700
WHITE, BLACK = (255,255,255),(0,0,0)

pygame.init()
pygame.display.set_caption("dda")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def dda(x1,y1,x2,y2):
    dx,dy = abs(x2-x1), abs(y2-y1)
    step = max(dx,dy)
    xi, yi = dx/step, dy/step
    x,y = x1,y1
    while x != x2:
        screen.set_at((round(x),round(y)),WHITE)
        x += xi
        y += yi

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        dda(100,200,400,400)
        pygame.display.flip()

if __name__=="__main__":
    main()