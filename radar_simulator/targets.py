import numpy as np

class Target:
    def __init__(self, position, velocity, reflectivity=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.reflectivity = reflectivity

    def update_position(self, dt):
        self.position += self.velocity * dt
