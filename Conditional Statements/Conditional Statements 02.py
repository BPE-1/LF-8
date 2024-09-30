"""
betrag = int(input("Warenkorbwert:"))
if betrag >= 100:
    print("Keine Versandkosten")
versandkosten = 0
"""

#Schönere Lösung
betrag = int(input("Warenkorbwert: "))
versandkosten1 = 0
versandkosten2 = "3,99"

if betrag >= 100:
    print("Keine Versandkosten für Sie")
    print("Ihre Versandkosten betragen:",versandkosten1,"€")
elif betrag < 100 and betrag > 0:
    print("Ihre Versandkosten betragen:",versandkosten2,"€")
else:
    print("Der Mindestbestellwert von 1€ wurde nicht erreicht !")

