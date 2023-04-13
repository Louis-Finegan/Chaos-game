
# Libaries used.
import numpy as np
import pygame



def generate_verts(num_verts, size, radius):
    # Calculates the vertices and outputs them as an array.           
    return np.array([[np.cos(2*np.pi/num_verts*i)*radius + size[0]/2, 
                   np.sin(2*np.pi/num_verts*i)*radius + size[1]/2] 
                  for i in range(num_verts)])

def radius_finder(verts):
    # Will calculate the mid-point of an edge on the polygon. Since the polygon is a regular
    # polygon, this calculation only has to be done once and is a point on the circle in which
    # the initial point will be randomly chosen inside the circle.
    midpt = np.array([(verts[0][0] + verts[1][0])/2, (verts[0][1] + verts[1][1])/2])
    radius = np.sqrt(midpt[0]**2 + midpt[1]**2)
    
    return radius

def init_point(size, verts):
    # gets an initial point within the circle inscribed in the regular polygon
    while True:
        randpt = np.random.rand(2) * np.array(list(size))
        if randpt[0]**2 + randpt[1]**2 <= radius_finder(verts):
            return randpt
        else:
            continue

def main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chaos Game")
    color = (255, 255, 255) # Color is white
    clock = pygame.time.Clock()

    running = True
    pressed_s = False

    # Initializes the pygame
    num_verts = 3 # Number of vertices on the polygon
    verts = generate_verts(num_verts, size=size, radius=150)
    current_point = init_point(size, verts)
    
    font = pygame.font.Font("fonts/arial.ttf", 16)
    text = font.render(f"Number of vertices: {num_verts}", True, color)
    screen.blit(text, (50, 50))

    # Displays polygon vertices on the display (in blue).
    for iargs in range(0, num_verts):
        pygame.draw.circle(screen, (255, 0, 0), (int(verts[iargs][0]), int(verts[iargs][1])), 1)
        pygame.display.flip()

    # While loop that generates each of the points on the pygame display. Will continuously generate point until
    # `q` or `r` is pressed.
    while running:
        clock.tick(60)
            
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Press to start
                if event.key == pygame.K_s:
                    pressed_s = True        
                
                # Press q to Quit Game
                if event.key == pygame.K_q:
                    running = False

                # Press r to reset game
                if event.key == pygame.K_r:
                    running = False
                    main()       

        if pressed_s:
            try:
                # Picks a vertex at random
                next_point = verts[np.random.randint(0, num_verts)]

                # Calculates midpoint
                current_point = (current_point + next_point)/2

                # Draw the current point on the display
                pygame.draw.circle(screen, color, (int(current_point[0]), int(current_point[1])), 1)
                pygame.display.flip()

            except:
                running = False 
    
    pygame.quit()

if __name__ == '__main__':
    main()