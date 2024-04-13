import pygame
import sys
import numpy as np
from neural_network import NeuralNetwork
from circles import CircleGenerator
from display import Display

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_INITIAL_CIRCLES = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Neural Network Circles")

    circle_generator = CircleGenerator(SCREEN_WIDTH, SCREEN_HEIGHT)
    display = Display(SCREEN_WIDTH, SCREEN_HEIGHT)

    circle_generator.generate_circles(NUM_INITIAL_CIRCLES)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        circle_generator_output = []  # Store outputs for each circle
        for circle in circle_generator.circles:
            inputs = np.array([circle.position[0], circle.position[1]])
            output = circle.neural_network.forward(inputs)
            circle_generator_output.append(output)
        
        circle_generator.handle_collisions()
        
        for circle, output in zip(circle_generator.circles, circle_generator_output):
            circle.move(output)
            circle.evolve()  # Evolve the neural network for each circle
            circle.grow()  # Grow the neural network for each circle

        circle_generator.handle_collisions()

        screen.fill((0, 0, 0))
        display.display_circles(circle_generator.circles)

        # Print neural network output for debugging
        print("Neural Network Output:", circle_generator_output)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
