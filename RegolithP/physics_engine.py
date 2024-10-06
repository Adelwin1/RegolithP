# physics_engine.py
import pymunk
import pymunk.pygame_util
import numpy as np

class PhysicsEngine:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, -1.62)  # Set the gravity to 1.62 m/s² (Moon's gravity)
        self.object_position = [0, 0, 0]
        self.object_velocity = [0, 0, 0]

    def add_object(self, mass, radius, x, y):
        # Create a new object in the physics engine
        body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius, (0, 0)))
        body.position = x, y
        shape = pymunk.Circle(body, radius)
        self.space.add(body, shape)

    def simulate(self, dt):
        # Simulate the physics for a given time step
        self.space.step(dt)
        self.object_position = [self.space.shapes[0].body.position.x, self.space.shapes[0].body.position.y, 0]
        self.object_velocity = [self.space.shapes[0].body.velocity.x, self.space.shapes[0].body.velocity.y, 0]

    def get_object_position(self):
        return self.object_position

    def get_object_velocity(self):
        return self.object_velocity
    
# simulation_3d.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from physics_engine import PhysicsEngine
from material_model import MaterialModel
from regolith_properties import RegolithProperties
from simulation_parameters import SimulationParameters

# Create instances of the classes
regolith_properties = RegolithProperties()
material_model = MaterialModel(regolith_properties)
physics_engine = PhysicsEngine()
simulation_parameters = SimulationParameters()

# Add an object to the physics engine
physics_engine.add_object(10, 1, 0, 0)  # Add an object with mass 10, radius 1, at position (0, 0)

# Simulate the physics
dt = 0.01
t = 0
x = []
y = []
z = []
while t < simulation_parameters.simulation_time:
    physics_engine.simulate(dt)
    t += dt
    x.append(physics_engine.get_object_position()[0])
    y.append(physics_engine.get_object_position()[1])
    z.append(physics_engine.get_object_position()[2])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the object's trajectory
ax.plot(x, y, z, 'b-')

# Plot the object's position at the final time step
ax.scatter(x[-1], y[-1], z[-1], c='r', marker='o')

# Set the plot limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Set the plot labels
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

# Show the plot
plt.show(block=True)