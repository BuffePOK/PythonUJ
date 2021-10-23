# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

# Na końcu nie jest potrzebny średnik (lines 5, 7, 9)

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# for i in "qwerty": if ord(i) < 100: print (i) # za dużo działań w 1. linii
# for i in "axby": print (ord(i) if ord(i) < 100 else i) # good

x = 2; y = 3 # line 3
print(x,y)

if (x > y):
    result = x
else:
    result = y

for i in "qwerty": 
    if ord(i) < 100: print(i)
for i in "axby": print (ord(i) if ord(i) < 100 else i)