#hallo 
a = int(input("Wert_ fuer a: "))
b = int(input("Wert fuer b: "))
c = int(input("Wert fuer c: "))
d = int(input("Wert fuer d: ")) 
v = int(input("Wert fuer v: "))

ergebnis_1 = bool(not a and not b)
ergebnis_2 = bool((a and (b or c)) or (b and not c))
ergebnis_3 = bool(0)
ergebnis_4 = bool(a or not (b or c))
ergebnis_5 = bool(a and not b)
ergebnis_6 = bool(c or d)
ergebnis_7 = bool((not a or not c) or (not b and v))
ergebnis_8 = bool(a and (b or c))

print("Ergebnis 1:", ergebnis_1)
print("Ergebnis 2:", ergebnis_2)
print("Ergebnis 3:", ergebnis_3)
print("Ergebnis 4:", ergebnis_4)
print("Ergebnis 5:", ergebnis_5)
print("Ergebnis 6:", ergebnis_6)
print("Ergebnis 7:", ergebnis_7)
print("Ergebnis 8:", ergebnis_8)

