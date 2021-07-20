import copy

a = [5] * 6
b = list(a)

a.append(7)

print(a)
print(b)

c = copy.deepcopy(a)
c.append(100)

print(a)
print(b)
print(c)
