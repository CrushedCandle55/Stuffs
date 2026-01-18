import pygame
import random

# Initialize the game
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plants vs Zombies")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load images
background_image = pygame.image.load("background.png")
plant_image = pygame.image.load("plant.png")
zombie_image = pygame.image.load("zombie.png")

# Set up game variables
plant_x = screen_width // 2 - plant_image.get_width() // 2
plant_y = screen_height - plant_image.get_height() - 20

zombies = []
zombie_speed = 1

clock = pygame.time.Clock()

running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the plant with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plant_x -= 5
    if keys[pygame.K_RIGHT]:
        plant_x += 5

    # Spawn zombies randomly
    if random.randint(0, 100) < 2:
        zombie_x = random.randint(0, screen_width - zombie_image.get_width())
        zombie_y = -zombie_image.get_height()
        zombies.append([zombie_x, zombie_y])

    # Move and draw zombies
    for zombie in zombies:
        zombie[1] += zombie_speed
        screen.blit(zombie_image, (zombie[0], zombie[1]))

    # Draw the plant
    screen.blit(plant_image, (plant_x, plant_y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()