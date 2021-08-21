# 3n+1
# Collatz Conjecture
# Visualizing multiple (25) graphs. Taking a single input from user, then creating 25 consecutive graphs.

import matplotlib.pyplot as plt

i = int(input())
# q = int(input())
q = i + 25
starting_number = i

while starting_number < q:
    i = starting_number
    r = 0
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

    print(f'Starting number: {starting_number:,}')
    print(f'Total number of steps = {r+1}')
    print(f'Maximum value reached {max:,}')
    starting_number += 1
    
plt.show()
