l=[11,1,2,3,1,4]
print(l)
print(type(l))
li=[{"red"},{"blue"},{"green"}]
print(li)


li.append("sami")
for x in li:
    print(x)

if "sami" in li:
    print("yes")
l.sort()
print(l[:])
print(li[:len(li)])
print(li[2:len(li)])
print(li[0:4:2])

l.reverse()
print(l)


print(l.count(1))


m=l
m[0]=222
print(m)
s=m.copy()
s[0]=777
s.insert(1,555)
m.sort()
s.extend(m)
print(s)
print(s.count(1))
print(m)
s.sort()
m.sort()

k = s + m
print(k)