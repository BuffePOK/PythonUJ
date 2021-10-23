line = "W tekście znajdującym się w zmiennej line zamienić ciąg znaków GvR na Guido van Rossum"
line = line.split()

for i in line:
    if i == "GvR":
        id = line.index(i)
        line[id] = "Guido van Rossum"

print(line)