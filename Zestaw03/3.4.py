# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) 
# i wypisujący x oraz trzecią potęgę x. 
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop. 
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
from math import pow as cube

while True:
    try:
        x = input("podaj liczbe: ")
        if x == "stop":
            break
        x = float(x)
        print(x, "x^3 = ", cube(x,3))
    except ValueError:
        print("To nie jest liczba")