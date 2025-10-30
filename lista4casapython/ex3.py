ra= []
ram =[]

y = 8
z = 1
for x in range(9):
    ra.append(int(input(f"Insira o RA:")))

print(ra)

for x in range(9):
    if x < 7:
        ram.append(ra[x])    
    else:
        ram.append(ra[y])
        y-=1
ram [0] = ra [1]
ram [1] = ra[0]

print(ram)