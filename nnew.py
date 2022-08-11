import random

def randomnumber(N):
	minimum = pow(5, N-1)
	maximum = pow(5, N) - 1
	return random.randint(minimum, maximum)

print(randomnumber(10))