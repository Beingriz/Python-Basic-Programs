# program to generate randome numbers
import  random
s=random.randint(0,500)
l = list()
for i in range(s):
    l.append(i*2)
    su = sum(l)

print(l)
print(su)