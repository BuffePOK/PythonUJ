# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line. 

a = 'Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line'

a = a.split()

def sortByLength(inputStr):
        return len(inputStr)

a.sort(key=sortByLength)

B = list(a[-1])

print("Najdłuższy wyraz: ", a[-1], "Długość najdłuższego wyrazu: ", len(B))