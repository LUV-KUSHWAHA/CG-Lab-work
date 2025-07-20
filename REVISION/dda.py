import pygame,sys
WIDTH,HEIGHT = 1000,700
WHITE,BLACK = (255,255,255),(0,0,0)
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DDA Implementation")

def dda(x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    if dx > dy:
        step = dx
    else:
        step = dy
    xi = dx/step
    yi = dy/step
    x,y = x1,y1
    while x != x2 or y != y2:
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
        dda(100,100,400,500)
        pygame.display.flip()
if __name__ == "__main__":
    main()