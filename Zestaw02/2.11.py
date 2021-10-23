# Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia. 

a = 'word'
a = list(a)
b = ""
for i in a:

    b += i + '_'

print(b)