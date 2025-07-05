import pygame, sys, math
pygame.init()

# Constants
WHITE, BLACK, GREY = (255, 255, 255), (0, 0, 0), (180, 180, 180)
WIDTH, HEIGHT = 1000, 700
FPS = 60

# Pygame setup
pygame.display.set_caption("Midpoint Ellipse Algorithm - Sphere Rotation")
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

def draw_sphere(xc, yc, ry, base_radius=20, depth_scale=10):
    """
    Draws a circle that simulates a sphere by adjusting its radius based on vertical position.
    The more to the front (lower y on screen), the larger the radius.
    """
    # Normalize vertical position to [0, 1]
    # Frontmost point on ellipse = y + ry, backmost = y - ry
    # We'll use this to scale radius
    relative_depth = (yc - (y - ry)) / (2 * ry)
    radius = int(base_radius + relative_depth * depth_scale)
    
    pygame.draw.circle(screen, WHITE, (int(xc), int(yc)), radius)

def main():
    global y, ry  # needed to compute depth inside draw_sphere
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

        # Draw the rotating sphere (size adjusted for depth)
        draw_sphere(xc, yc, ry)

        # Update angle for rotation
        theta = (theta + 1) % 360

        pygame.display.update()

if __name__ == "__main__":
    main()
