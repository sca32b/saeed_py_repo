import math

def calc_paint(height, width, coverage):
    return math.ceil(int(height) * int(width) / coverage)

height = input ("get me the heinght : ")
width = input ("get me the width : ")
coverage = 5

print(f"you will need {calc_paint(height, width, coverage)} cans of paint for your job")