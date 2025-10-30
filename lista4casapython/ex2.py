ra= []
ram =[]
y = 8
for x in range(9):
    ra.append(int(input(f"Insira o RA:")))
print(ra)
for x in range(9):
    if x < 5:
        ram.append(ra[x])    
    else:
        ram.append(ra[y])
        y-=1
print(ram)