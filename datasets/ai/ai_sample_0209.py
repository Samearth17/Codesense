import random

def generate_snowflake():
  # Generate random numbers between 0 and 1
  a = random.random()
  b = random.random()
  c = random.random()

  # Generate the snowflake
  snowflake = [] 
  snowflake.append((a**2 + b**2 + c**2)**0.5 * math.cos(a * math.pi * 2))
  snowflake.append((a**2 + b**2 + c**2)**0.5 * math.sin(b * math.pi * 2))
  snowflake.append((a**2 + b**2 + c**2)**0.5 * math.sin(c * math.pi * 2))

  return snowflake