import pygame
import sys

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Display")

# Load the image
image = pygame.image.load("C:\\Users\\maqwi\\Desktop\\hack\\testing images\\2.png")
new_width = 200
new_height = 150

# Resize the image
resized_image = pygame.transform.scale(image, (new_width, new_height))
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display the image
    screen.blit(resized_image, (0, 0))
    pygame.display.flip()