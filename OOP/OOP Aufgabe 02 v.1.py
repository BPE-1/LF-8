
# Variante 1

class Character:
    def __init__(self):
        self.name = None
        self.height = None
        self.weight = None
        self.sex = None
        self.lp = None

# Methoden         
    def run(self):
        print(self.name, "Rennt")
    def fight(self):
        print(self.name, "Kämpft")
    def defend(self):
        print(self.name, "verteidigt") 

# Ermöglicht bessere Objektausgabe aller Werte / Alternative zu __dict__       
    def __str__(self):
        return f"Character\nName = {self.name},\nGröße = {self.height}m,\nGewicht = {self.weight}kg,\nGeschlecht = {self.sex},\nLebenspunkte = {self.lp})"
        
# Erstellung eines Objects der Class Character        
char1 = Character()
char2 = Character()

# Den Attributen Werte zuweißen
char1.name = "Olaf"
char1.height = 1.80
char1.weight = 82
char1.sex = "M"
char1.lp = 100

char2.name = "Helene"
char2.height = 1.65
char2.weight = 58
char2.sex = "W"
char2.lp = 75

# Zeigt alle Attribute an 
print(char1.__dict__) 
print(char2.__dict__) 

# Zugriff auf einzelnes oder mehrere Attribute mit . Opperator
print(char1.name)
print(char2.name, char2.height)

# Funktionsaufruf
char1.run()
char2.fight()

# Ausgabe aller Werte durch oben benutzte __str__ Funktion
print(char1)
