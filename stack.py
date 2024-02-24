# use list to implement a stack

from random import randint
def push(stack, data):
    stack.append(data)
    return stack

def pop (stack):
    if len(stack) == 0:
        return "The stack is empty"
    else:
        return stack.pop()


stack = []

for i in range(10):
    push(stack, randint(1,100))

print(f"The length of the stack is {len(stack)}")
print(stack)

for i in range(len(stack)):
    print(pop(stack))

print(f"The length of the stack is {len(stack)}")

