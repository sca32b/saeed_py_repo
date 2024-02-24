name1 = input("Enter name1: \n")
name2 = input("Enter name2: \n")

combined_name = (name1 + name2).lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

combined_score = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

combined_score2 = l + o + v + e

love_score = int(str(combined_score) + str(combined_score2))
print(love_score)