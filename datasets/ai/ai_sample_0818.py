import math

class BouncingBall():
    def __init__(self):
        self.x = 0.0   # horizontal position 
        self.y = 5.0   # vertical position 
        self.vy = 0.2  # vertical velocity 
        self.g = 9.81  # gravitational acceleration 

    def update(self, dt):
        self.y -= self.vy * dt
        self.vy -= self.g * dt

        if self.y <= 0:
            self.y = 0
            self.vy *= -0.9