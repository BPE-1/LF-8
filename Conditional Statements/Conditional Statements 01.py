"""
Geben Sie die allgemeine Python Syntax einer einfachen Verzweigung (if-Anweisung), einer Verzweigung mit
Alternative (if-else Anweisung) und einer Verzweigung mit mehreren Bedingungen (elif-Anweisung) an. 
Erarbeiten Sie sich zusätzlich die allgemeine Python Syntax zur Fallunterscheidung (match-case) und geben Sie diese mit an.
"""


x = 10

# Einfache Verzweigung
if x > 9:
    print("Einfache Verzweigung")
    
    
# Verzweigung mit Alternative
if x > 10:
    print("Lorem Ipsum")
else:
    print("Verzweigung mit Alternative")
    

# Verzweigung mit mehreren Alternativen 
if x > 10:
    print("Lorem Ipsum")
elif x < 5:
    print("Lorem Ipsum")
else:
    print("Verzweigung mit mehreren Alternativen")
 
    
# Fallunterscheidung
match x:
    case 3:
        print("x ist 3")     
    case 6:
        print("x ist 6")
    case 9:
        print("x ist 9")
    case 10:
        print("Fallunterscheidung (x ist 10)")
    case other:
        print("x ist nicht 3,6,9 oder 10")
