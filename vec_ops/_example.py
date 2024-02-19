from vector import Vector
from physics import apply_force

# Create vectors
v1 = Vector(values=[1, 2])
v2 = Vector(values=[3, 4])

# Add vectors
v_sum = v1 + v2

# Apply force
result = apply_force(acceleration=1, force=10, mass=5)

print(v_sum)
print(result)