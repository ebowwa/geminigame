# object.py
from vec_ops.vector import engVector
from vec_ops.physics import apply_force

class Object:
    def __init__(self, x, y, width, height, mass):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mass = mass if mass > 0 else 1  # Ensure mass is positive, non-zero
        self.velocity = engVector.create_vector(0.0, 0.0)  # Use engVector for velocity
        self.acceleration = engVector.create_vector(0.0, 0.0)  # Use engVector for acceleration

    def update_position(self, dt):
        # Use engVector method for adding and multiplying vectors
        self.velocity = engVector.add_vectors(self.velocity, engVector.multiply_vector(self.acceleration, dt))
        # Access x and y components via indexing into the engVector object
        self.x += self.velocity.values[0] * dt
        self.y += self.velocity.values[1] * dt
        self.acceleration = engVector.create_vector(0.0, 0.0)  # Reset acceleration

    def apply_force(self, force):
        # Use engVector to represent force
        force_vector = engVector.create_vector(force[0], force[1])
        # Apply force to acceleration
        self.acceleration = engVector.add_vectors(self.acceleration, engVector.multiply_vector(force_vector, 1 / self.mass))

    def collide(self, other):
        pass
