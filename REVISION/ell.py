import pygame, sys

w, h = 1000, 700
white, black = (255, 255, 255), (0, 0, 0)
pygame.init()
pygame.display.set_caption("Ellipse")
screen = pygame.display.set_mode((w, h))

def ellipse(xc, yc, a, b):
    x, y = 0, b
    p = b**2 - a**2 * b + a**2 / 4
    
    # Plot initial point and its reflections
    points = [(x, y), (-x, y), (x, -y), (-x, -y)]
    for px, py in points:
        screen.set_at((px + xc, py + yc), white)

    # Region 1
    while 2 * b**2 * x <= 2 * a**2 * y:
        if p < 0:
            x += 1
            p += 2 * b**2 * x + b**2
        else:
            x += 1
            y -= 1
            p += 2 * b**2 * x - 2 * a**2 * y + b**2
        
        # Plot all 4 symmetric points
        points = [(x, y), (-x, y), (x, -y), (-x, -y)]
        for px, py in points:
            screen.set_at((px + xc, py + yc), white)
    
    # Region 2
    p2 = b**2 * (x + 0.5)**2 + a**2 * (y - 1)**2 - a**2 * b**2
    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 += -2 * a**2 * y + a**2
        else:
            x += 1
            y -= 1
            p2 += 2 * b**2 * x - 2 * a**2 * y + a**2
        
        points = [(x, y), (-x, y), (x, -y), (-x, -y)]
        for px, py in points:
            screen.set_at((px + xc, py + yc), white)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fixed typo here
                pygame.quit()
                sys.exit()
        screen.fill(black)
        ellipse(300, 300, 200, 100)
        pygame.display.update()

if __name__ == "__main__":
    main()