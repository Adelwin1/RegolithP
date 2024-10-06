# simulation.py
import pygame
import math
import sys
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600

# Create a 3D window with a black background
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("3D Simulation")

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Define the light source
light_x, light_y, light_z = 0, 0, 10
light_radius = 10

# Draw the light source
def draw_light():
    pygame.draw.circle(screen, white, (int(light_x), int(light_y)), light_radius)

# Define the regolith's position and size
regolith_x, regolith_y, regolith_z = 0, 0, 0
regolith_size = 100

# Draw the regolith on the screen
def draw_regolith():
    pygame.draw.rect(screen, gray, (int(regolith_x - regolith_size / 2), int(regolith_y - regolith_size / 2), regolith_size, regolith_size))

# Define the rocket's position and velocity
rocket_x, rocket_y, rocket_z = 0, 0, 0
rocket_vx, rocket_vy, rocket_vz = 0, 0, 0

# Define the rocket's size and shape
rocket_size = 10
rocket_shape = "cylinder"

# Draw the rocket on the screen
def draw_rocket():
    pygame.draw.circle(screen, white, (int(rocket_x), int(rocket_y)), rocket_size)

# Define the astronauts' positions and velocities
astronaut1_x, astronaut1_y, astronaut1_z = -10, 0, 0
astronaut1_vx, astronaut1_vy, astronaut1_vz = 0, 0, 0

astronaut2_x, astronaut2_y, astronaut2_z = 10, 0, 0
astronaut2_vx, astronaut2_vy, astronaut2_vz = 0, 0, 0

# Define the astronauts' size and shape
astronaut_size = 5
astronaut_shape = "circle"

# Draw the astronauts on the screen
def draw_astronaut1():
    pygame.draw.circle(screen, white, (int(astronaut1_x), int(astronaut1_y)), astronaut_size)

def draw_astronaut2():
    pygame.draw.circle(screen, white, (int(astronaut2_x), int(astronaut2_y)), astronaut_size)

# Define the asteroids' positions and velocities
asteroids = []
for _ in range(10):
    asteroid_x = random.randint(-100, 100)
    asteroid_y = random.randint(-100, 100)
    asteroid_z = random.randint(-100, 100)
    asteroid_vx = random.randint(-5, 5)
    asteroid_vy = random.randint(-5, 5)
    asteroid_vz = random.randint(-5, 5)
    asteroids.append((asteroid_x, asteroid_y, asteroid_z, asteroid_vx, asteroid_vy, asteroid_vz))

# Define the asteroids' size and shape
asteroid_size = 5
asteroid_shape = "circle"

# Draw the asteroids on the screen
def draw_asteroids():
    for asteroid in asteroids:
        pygame.draw.circle(screen, white, (int(asteroid[0]), int(asteroid[1])), asteroid_size)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Draw the light source
    draw_light()

    # Draw the regolith
    draw_regolith()

    # Draw the rocket
    draw_rocket()

    # Draw the astronauts
    draw_astronaut1()
    draw_astronaut2()

    # Draw the asteroids
    draw_asteroids()

    # Update the positions of the objects
    rocket_x += rocket_vx
    rocket_y += rocket_vy
    rocket_z += rocket_vz

    astronaut1_x += astronaut1_vx
    astronaut1_y += astronaut1_vy
    astronaut1_z += astronaut1_vz

    astronaut2_x += astronaut2_vx