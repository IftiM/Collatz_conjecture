# 3n+1
# Collatz Conjecture
# Added matplolib graph for visualizing

import matplotlib.pyplot as plt

i = int(input())
starting_number = i
# r is a counter, to calculate the number of steps needed to reach to number 1
r = 0

# Finding the max value the conjecture reached,
# initially used input value as the maximum
max = i

x = []
y = []

while i != 1:
    r+=1
    x.append(r)
    y.append(i)
    if i % 2 == 0:
        i = int(i/2)
        if i > max:
            max = i
    else:
        i = int(3*i+1)
        if i > max:
            max = i
    
x.append(r+1)
y.append(1)
plt.plot(x,y)
plt.show()

print(f'Starting number: {starting_number:,}')
print(f'Total number of steps = {r+1}')
print(f'Maximum value reached {max:,}')
