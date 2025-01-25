
# Erstellung der Oberklasse
class Character:
    def __init__(self, name:str=None, gender:str=None, race:str=None, hp:int=None, max_hp:int=None, ep:int=None, lvl_ep:int=None, lvl:int=None):
        self._name = name
        self._gender = gender
        self._race = race
        self._hp = hp
        self._max_hp = max_hp
        self._ep = ep
        self._lvl_ep = lvl_ep
        self._lvl = lvl
        
# Werte der Klasse ausgeben        
    def print_Stats(self):
        print(
            f"\nCharacter Stats\n"
            f"-----------------------------------\n"
            f"{'Name':<18} =  {self._name}\n"
            f"{'Geschlecht':<18} =  {self._gender}\n"
            f"{'Rasse':<18} =  {self._race}\n"
            f"{'Lebenspunkte':<18} =  {self._hp}\n"
            f"{'Lebenspunkte max.':<18} =  {self._max_hp}\n"
            f"{'EXP':<18} =  {self._ep}\n"
            f"{'EXP -> LVL UP':<18} =  {self._lvl_ep}\n"
            f"{'Level':<18} =  {self._lvl}"
            )
# Level Up Funktion / erhöht Level, max_HP und Level-UP_EP
    def levelup(self):
        self._lvl += 1
        self._lvl_ep = int(self._lvl_ep * 1.5)
        self._max_hp = int(self._max_hp * 1.075)
        print("\n",self._name, "ist ein Level aufgestiegen!")

# EP erhalten Funktion <-- schlechter Name, Verwechslungsgefahr >GETTER/SETTER< /  setzt einen Wert >>> gain_exp   
    def get_ep(self,epn):
        self._ep += epn       
        while self._ep >= self._lvl_ep:  # Prüfen auf Level UP
            self.levelup()
 
# HP erhöhen oder reduzieren         
    def set_hp(self, operator:str, value:int):
        if str(operator) == "+":
            self._hp += value
            if self._hp > self._max_hp:
                self._hp = self._max_hp
        elif operator == "-":
            self._hp -= value
            if self._hp < 1:
                self._hp = 1
        else: 
            print("Fehlerhafte Eingbe")
            
# Zweite Setter Methode / Optional 
    def set_name(self, new_name:str):
        self._name = new_name 
        

# Unterklasse Magier  (max. Mana ebenfalls ergänzt)   
class Mage(Character):
    def __init__(self, name, gender, race, hp, max_hp, ep, lvl_ep, lvl, mana:int=None, max_mana:int=None):     
        super().__init__(name, gender, race, hp, max_hp, ep, lvl_ep, lvl) # super() für Zugriff auf Basisklasse 
        self.__mana = mana              # neues Attribut
        self.__max_mana = max_mana      # neues Attribut
        
    def print_Stats(self):
        super().print_Stats()
        print(f"{'Mana':<18} =  {self.__mana}\n"
            f"{'Mana max.':<18} =  {self.__max_mana}\n")
        
# Mana erhöhen oder reduzieren         
    def set_mana(self, operator:str, value:int):
        if str(operator) == "+":
            self.__mana += value
            if self.__mana > self.__max_mana:
                self.__mana = self.__max_mana
        elif operator == "-":
            self.__mana -= value
            if self.__mana < 0:
                self.__mana = 0
        else: 
            print("Fehlerhafte Eingbe")
    
    
# Unterklasse Warrior (max. Fury ebenfalls ergänzt)   
class Warrior(Character):
    def __init__(self, name, gender, race, hp, max_hp, ep, lvl_ep, lvl, fury:int=None, max_fury:int=None):     
        super().__init__(name, gender, race, hp, max_hp, ep, lvl_ep, lvl) # super() für Zugriff auf Basisklasse 
        self.__fury = fury              # neues Attribut
        self.__max_fury = max_fury      # neues Attribut
        
    def print_Stats(self):
        super().print_Stats()
        print(f"{'Wut':<18} =  {self.__fury}\n"
            f"{'Wut max.':<18} =  {self.__max_fury}\n")
         
# Wut erhöhen oder reduzieren         
    def set_fury(self, operator:str, value:int):
        if str(operator) == "+":
            self.__fury += value
            if self.__fury > self.__max_fury:
                self.__fury = self.__max_fury
        elif operator == "-":
            self.__fury -= value
            if self.__fury < 0:
                self.__fury = 0
        else: 
            print("Fehlerhafte Eingbe")


# Character wird initialisiert
char1 = Character("Rambo", "Männlich", "Mensch", 375, 875, 1000, 5000, 5)
char1.print_Stats()   

# Magier wird initialisiert     
mage1 = Mage("Voldemort", "Männlich", "Schlammblut", 7085, 10500, 10000, 50000, 50, 500, 2000)
mage1.print_Stats()

# Warrior wird initialisiert
war1 = Warrior("Blade", "Männlich", "Daywalker", 4000, 9000, 8000, 4000, 35, 1000, 5000)
mage1.print_Stats()

# Charakter, Magier & Warrior bekommen EP hinzu 
char1.get_ep(15000) 
mage1.get_ep(7500)
war1.get_ep(1000)

# Charakter erhält oder verliert HP
char1.set_hp("+", 25) 
char1.print_Stats()       

# Magier erhält oder verliert Mana <-- max. Mana wurde ergänzt
mage1.set_mana("+", 300)   
mage1.print_Stats()

# Warrior erhält oder verliert Wut <-- max. Wut wurde ergänzt
war1.set_fury("+", 600)   
war1.print_Stats()

""" optionale zweite Setter Methode <- gefordert in Aufgabenstellung 
char1.set_name("Leonidas")
char1.print_Stats()   
"""
