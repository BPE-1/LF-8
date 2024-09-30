# Erfüllt die Anforderung
"""
ip = input("Bitte IP eingeben: ")
x = ip.split(".")
r = range(256)
if int(x[0]) in r and int(x[1]) in r and int(x[2]) in r and int(x[3]) in r and len(x) == 4:
    print("Die IP Adresse ist korrekt !")  
else:
    print("Die IP Adresse ist nicht korrekt !")
"""

# Detailierter
ip = input("Bitte IP eingeben: ")
x = ip.split(".")
if len(x) < 4:
    print("Fehler! Eine IP muss 4 Oktete haben.\nDie IP Adresse ist nicht korrekt !")  
elif len(x) > 4:
    print("Fehler! Eine IP darf nur 4 Oktete haben.\nDie IP Adresse ist nicht korrekt !")  
elif int(x[0]) < 0 or int(x[0]) > 255:
    print("Fehler in Oktett 1.\nWert muss zwischen 0-255 liegen.\nDie IP Adresse ist nicht korrekt !")  
elif int(x[1]) < 0 or int(x[1]) > 255:
    print("Fehler in Oktett 2.\nWert muss zwischen 0-255 liegen.\nDie IP Adresse ist nicht korrekt !") 
elif int(x[2]) < 0 or int(x[2]) > 255:
    print("Fehler in Oktett 3.\nWert muss zwischen 0-255 liegen.\nDie IP Adresse ist nicht korrekt !") 
elif int(x[3]) < 0 or int(x[3]) > 255:
    print("Fehler in Oktett 4.\nWert muss zwischen 0-255 liegen.\nDie IP Adresse ist nicht korrekt !") 
else:
    print("Die IP Adresse ist korrekt !")
    
