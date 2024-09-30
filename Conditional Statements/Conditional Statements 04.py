x = int(input("Bitte Zahl eingeben:"))
modulo = (x % 2)

if x == 0:
    print("nice try...")
elif modulo > 0:
    print("Ungerade Zahl")
else:
    print("Gerade Zahl")
