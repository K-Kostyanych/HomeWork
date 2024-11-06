list = [57, 48,101, 125, 36,110, 78, 85]
d = ''
for i in list:
    d = d + chr(i)
print(d)
s = 'Kostyanych'
list = []
for j in s:
    list.append(ord(j))

print(list)
print(hex(ord('k')))
kk = b'\x6b'
print(kk.decode())
