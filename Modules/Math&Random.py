import math
import random

help(math)

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))

print(math.pi)

print(math.e)
print(math.inf)
print(math.nan)
print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(897))
print(math.degrees(math.sin(9783)))
print(math.radians(math.sin(9783)))

print(random.randint(0,10))
print(random.randint(0,1000000))

# Seed
print(random.seed(101))
print(random.randint(0,100))
print(random.randint(0,100))

mylist = list(range(0, 20))
print(mylist)
print(random.choice(mylist))

# Sampple with replacement
print(random.choices(population=mylist, k=10))
# Sampple without replacement
print(random.sample(population=mylist, k=10))

print(random.shuffle(mylist))
print(mylist)

# Probability - continuous distribution
print(random.uniform(a=0, b=100))
# Gaussian distribution
print(random.gauss(mu=0, sigma=1))

