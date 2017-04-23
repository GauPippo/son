l = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Hiep and these are my ship sizes\n", l)

n = max(l)
print("Now my biggest sheep has size", n, "let's shear it")

l[2] = 8
print("After shearing, here is my flock\n", l)

for m in l:
    m += 50
    print(m)
##print("One month has passed, now here is my flock", m)
