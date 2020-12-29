a = int(input("\nBanyaknya data : "))

b = []
d = 0

for x in range(1, a+1):
    c = int(input("Masukkan Data ke - %d: " % (x)))
    b.append(c)
    d = sum(b)
    e = d / a

print("Total : ", d)
print("Rata - rata : ", e)
