from collections import deque

# Create a new deque
d = deque([1, 2, 3, 4, 5])
print(d)
print(type(d))
print(d[0])

# Add an element to the right side of the deque
d.append(6)
print(d)

# Add an element to the left side of the deque
d.appendleft(0)
print(d)

# Remove an element from the right side of the deque
d.pop()
print(d)

# Remove an element from the left side of the deque
d.popleft()
print(d)

