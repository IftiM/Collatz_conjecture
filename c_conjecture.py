""" 3n+1 Collatz Conjecture
Start with any positive integer n
If the n even, divide by 2
If the n is odd, the next term is 3n+1 Keep going until it eventually reaches 1 """


i = int(input())
starting_number = i
# r is a counter, to calculate the number of steps needed to reach down to number 1
r = 0

# Finding the max value the conjecture reached, initially used input value as maximum
max = i

while i != 1:
    r+=1
    print(f'Current step: {r}, current value {i}')
    if i % 2 == 0:
        i = int(i/2)
        if i > max:
            max = i
    else:
        i = int(3*i+1)
        if i > max:
            max = i

print(f'Starting number: {starting_number:,}')
print(f'Total number of steps = {r+1}')
print(f'Maximum value reached {max:,}')
