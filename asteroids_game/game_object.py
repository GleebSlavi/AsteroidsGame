from two_dimensional_vector import Vector2D

class GameObject:
    def __init__(self, position, image, velocity):
        self.image = image
        self.radius = image.get_width() / 2
        self.velocity = Vector2D(velocity[0], velocity[1])
        self.position = Vector2D(position[0], position[1])

    def draw(self, surface) -> None:
        blit_position = self.position - Vector2D(self.radius, self.radius)
        surface.blit(self.image, blit_position.to_tuple())

    def move(self) -> None:
        self.position = self.position + self.velocity

    def collision(self, other) -> bool:
        distance = self.position.euclidean_distance(other.position)
        return distance < self.radius + other.radius
