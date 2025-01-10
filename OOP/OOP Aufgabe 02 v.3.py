
# Variante 3 / Kombination der Varianten / Objekte können entweder direkt mit allen Werten oder auch ohne erstellt werden

class Character:
    def __init__(self, name=None, height=None, weight=None, sex=None, lp=None):
        self.name = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.lp = lp

# Methoden         
    def run(self):
        print(self.name, "Rennt")
    def fight(self):
        print(self.name, "Kämpft")
    def defend(self):
        print(self.name, "verteidigt") 
              
# Ermöglicht bessere Objektausgabe aller Werte / Alternative zu __dict__       
    def __str__(self):
        return f"\nCharacter\nName = {self.name}\nGröße = {self.height}m\nGewicht = {self.weight}kg\nGeschlecht = {self.sex}\nLebenspunkte = {self.lp}\n"
        
# Erstellung eines Objects der Class Character        
char1 = Character("Tom", 1.77, 95, "M", 110)
char2 = Character()
char2.name = "Erika"
char2.height = 1.60
char2.weight = 53
char2.sex = "W"
char2.lp = 50


# Zeigt alle Attribute an 
print("\n",char1.__dict__,"\n") 
print("\n",char2.__dict__,"\n") 

# Zugriff auf einzelnes oder mehrere Attribute mit . Opperator
print(char1.name)
print(char2.name, char2.height)

# Funktionsaufruf
char1.run()
char2.fight()

# Ausgabe aller Werte durch oben benutzte __str__ Funktion
print(char1)
print(char2)
