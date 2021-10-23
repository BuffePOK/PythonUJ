line = "posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. wskazówka: funkcja wbudowana sorted()."
line = line.split()

def sortByAlphabet(inputStr):
        return inputStr[0]

def sortByLength(inputStr):
        return len(inputStr)

print(sorted(line, key=sortByAlphabet))
print(sorted(line, key=sortByLength))