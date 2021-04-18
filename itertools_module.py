import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for combination in it.permutations(notes, 4):
    print(combination)

result = (math.factorial(len(notes))/math.factorial(len(notes)-4))
print(result)

print(30*'#')
for combination in it.product(notes, repeat=4):
    print(combination)

result = pow(len(notes), 4)
print(result)
