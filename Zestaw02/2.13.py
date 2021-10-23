# Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum(). 

a = "Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum()."
a = a.split()

accum = 0

for i in a:
    i = list(i)
    accum += len(i)

print(accum)