import pygame

class Display:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Neural Network Circles")

    def display_circles(self, circles):
        # Display circles on the screen
        self.screen.fill((0, 0, 0))  # Clear the screen
        for circle in circles:
            pygame.draw.circle(self.screen, self._get_color(circle.color), circle.position, 10)  # Assuming radius is 10
        pygame.display.flip()  # Update the display

    def _get_color(self, color):
        if color == "red":
            return (255, 0, 0)
        elif color == "green":
            return (0, 255, 0)
        elif color == "blue":
            return (0, 0, 255)
        else:
            return (255, 255, 255)  # Default to white if color is not recognized
