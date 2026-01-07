import random  # random module is imported to generate random numbers


random_integer = random.randint(1,10) # Generate a random integer between 1 and 100 (inclusive)

print(random_integer)

random_number_0_to_1 = random.random() * 10  # random.random() generates a float between 0.0 to 1.0
print (random_number_0_to_1)

random_float = random.uniform(1,10)  # random.uniform(a, b) generates a float between a and b (inclusive)
print(random_float)