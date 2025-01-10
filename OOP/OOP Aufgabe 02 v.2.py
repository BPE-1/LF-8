
# Variante 2 mit Pflichtparametern / Attribute werden direkt im Konstruktor gesetzt

class Character:
    def __init__(self, name, height, weight, sex, lp):
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
char1 = Character("Harald", 1.75, 77, "M", 105)
char2 = Character("Annika", 1.70, 60, "W", 70)


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
