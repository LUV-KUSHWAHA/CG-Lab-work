import pygame, sys, math
WIDTH, HEIGHT = 1000, 700
WHITE, BLACK = (255,255,255),(0,0,0)

pygame.init()
pygame.display.set_caption("trans 2d")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def translate(x1,y1,x2,y2, tx,ty):
    return x1+tx,y1+ty, x2+tx,y2+ty

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        pygame.draw.line(screen,WHITE,(200,300),(300,100),5)
        x1,y1,x2,y2 = translate(200,300,300,100,200, 200)
        pygame.draw.line(screen,WHITE,(x1,y1),(x2,y2),3)
        pygame.display.flip()

if __name__ == "__main__":
    main()