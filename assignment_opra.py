a = 10
print(id(a)) 

a += 5  # a = a + 5
print(id(a))
print(a) # the memory address of both a = 10 and a = 15 are different 

b = 11
b -= 1 # b = b - 1
print(b)

c = 12
c *= 5 # it is similar to  c = c * 5
print(c)

d = 20
d /= 10   #d = d / 10
print(d)

e = 100
e //= 10  # e = e // 10
print(e)

f = 50
f %= 4  # f = f % 4
print(f)

g = 10
g **= 2  # g = g ** 2
print(g)