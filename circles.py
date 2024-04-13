import pygame
import random
from neural_network import NeuralNetwork

class Circle:
    def __init__(self, color, age, position):
        self.color = color
        self.age = age
        self.position = position
        self.neural_network = NeuralNetwork(input_size=2, output_size=2)  # Create neural network for each circle

    def evolve(self):
        # Implement the evolution process for the neural network
        self.neural_network.evolve()

    def grow(self):
        # Implement the growth process for the neural network
        self.neural_network.grow()

    def move(self, output):
        # Implement circle movement based on neural network output
        # For simplicity, let's move the circle randomly for now
        dx = output[0]  # Scale output for x-axis movement
        dy = output[1]  # Scale output for y-axis movement
        self.position = (self.position[0] + dx, self.position[1] + dy)
    
    def check_collision(self, other_circle):
        # Check collision between two circles
        distance_sq = (self.position[0] - other_circle.position[0])**2 + \
                      (self.position[1] - other_circle.position[1])**2
        if distance_sq < (10 * 2)**2:  # Assuming radius of circles is 10
            return True
        return False

class CircleGenerator:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.circles = []
    
    def generate_circles(self, num_circles):
        # Generate random number of circles within screen boundaries
        for _ in range(num_circles):
            color = random.choice(["red", "green", "blue"])
            age = 0
            position = (random.randint(10, self.screen_width - 10), random.randint(10, self.screen_height - 10))
            self.circles.append(Circle(color, age, position))
    
    def handle_collisions(self):
        # Handle collisions between circles
        for i in range(len(self.circles)):
            for j in range(i + 1, len(self.circles)):
                if self.circles[i].check_collision(self.circles[j]):
                    if self.circles[i].color == self.circles[j].color:
                        # Merge circles or perform some other action
                        pass
                    else:
                        # Handle collision between circles of different colors
                        pass
    
    def handle_border_collision(self, circle):
        # Handle border collision for a circle
        x, y = circle.position
        if x < 10 or x > self.screen_width - 10 or y < 10 or y > self.screen_height - 10:
            # Remove circle from list
            self.circles.remove(circle)
