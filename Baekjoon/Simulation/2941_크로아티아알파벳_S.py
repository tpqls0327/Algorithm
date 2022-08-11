# 2941 크로아티아 알파벳

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
data = input()

for i in cro:
    data = data.replace(i, '*')
print(len(data))
