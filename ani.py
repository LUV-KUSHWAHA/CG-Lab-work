import pygame, sys, math
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1000, 700
FPS = 60

# Pygame setup
pygame.display.set_caption("Shaded Sphere Moving on Ellipse")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_ellipse_bla(xc, yc, rx, ry):
    x, y = 0, ry
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    plot_points(xc, yc, x, y)
    
    while 2 * ry**2 * x <= 2 * rx**2 * y:
        if p1 < 0:
            x += 1
            p1 += 2 * ry**2 * x + ry**2
        else:
            x += 1
            y -= 1
            p1 += 2 * ry**2 * x - 2 * rx**2 * y + ry**2
        plot_points(xc, yc, x, y)

    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2
    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 += -2 * rx**2 * y + rx**2
        else:
            x += 1
            y -= 1
            p2 += 2 * ry**2 * x - 2 * rx**2 * y + rx**2
        plot_points(xc, yc, x, y)

def plot_points(xc, yc, x, y):
    screen.set_at((int(xc + x), int(yc + y)), WHITE)
    screen.set_at((int(xc - x), int(yc + y)), WHITE)
    screen.set_at((int(xc + x), int(yc - y)), WHITE)
    screen.set_at((int(xc - x), int(yc - y)), WHITE)

def draw_sphere_with_concentric_circles(xc, yc, max_radius):
    """
    Simulates a shaded 3D sphere by drawing concentric circles
    with increasing radius and changing brightness (from dark to white).
    """
    for r in range(max_radius, 0, -1):
        # Create a smooth shading from dark grey to white
        shade = int(255 * (r / max_radius))  # fade from dark to light
        color = (shade, shade, shade)
        pygame.draw.circle(screen, color, (int(xc), int(yc)), r)

def main():
    x, y = 500, 350  # center of ellipse
    rx, ry = 300, 150  # ellipse radii
    theta = 0  # initial angle

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Draw the main elliptical path
        draw_ellipse_bla(x, y, rx, ry)

        # Calculate position of the moving sphere on the ellipse
        rad = math.radians(theta)
        xc = x + rx * math.cos(rad)
        yc = y + ry * math.sin(rad)

        # Draw the rotating shaded sphere
        draw_sphere_with_concentric_circles(xc, yc, 25)

        # Update angle for rotation
        theta = (theta + 1) % 360

        pygame.display.update()

if __name__ == "__main__":
    main()
