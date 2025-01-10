
# Implementieren der Klasse mit den geforderten Eigenschaften.

class NetworkSettings:
    def __init__(self,ipv4=None, snm=None, mac=None):
        self._ipv4 = ipv4   #protected
        self._snm = snm     #protected
        self.__mac = mac    #private
    
# IP Setzfunktion mit Setter Methode
    def setIP(self,ipv4):
        if ipv4.count(".") == 3:
            octets = ipv4.rstrip(".").split(".")
            if len(octets) == 4:
                if "" in octets:
                    print("Fehler! Oktett leer!\nKeine Änderung vorgenommen.")
                    return
                if int(octets[0],) in range(0, 256) and int(octets[1],) in range(0, 256) and int(octets[2],) in range(0, 256) and int(octets[3],) in range(0, 256):
                    self._ipv4 = ipv4
                    print("Die neue Ip wurde erfolgreich gesetzt!\n")
                else:
                    print("Fehlerhafte Eingabe -> IP Range 0-255!\nKeine Änderung vorgenommen.")
            else: 
                print("Es müssen 4 Oktette sein!\nKeine Änderung vorgenommen.")
        else:
            print("Bitte mit Punkten (.) trennen!\nKeine Änderung vorgenommen.")

# SNM Setzfunktion mit Setter Methode        
    def setSubnetmask(self,snm):
        if snm.count(".") == 3:
            octets = snm.rstrip(".").split(".")
            if len(octets) == 4:
                if "" in octets:
                    print("Fehler! Oktett leer!\nKeine Änderung vorgenommen.")
                    return
                if int(octets[0],) in range(0, 256) and int(octets[1],) in range(0, 256) and int(octets[2],) in range(0, 256) and int(octets[3],) in range(0, 256):
                    self._snm = snm
                    print("Die neue Subnetzmaske wurde erfolgreich gesetzt!\n")
                else:
                    print("Fehlerhafte Eingabe -> IP Range 0-255!\nKeine Änderung vorgenommen.")
            else: 
                print("Es müssen 4 Oktette sein!\nKeine Änderung vorgenommen.")
        else:
            print("Bitte mit Punkten (.) trennen!\nKeine Änderung vorgenommen.")
        
# Zum Anzeigen der ganzen Attribute        
    def printSettings(self):
        print(f"\nNetzwerkeinstellungen\n--------------------------------\nIPV4-Adresse = {self._ipv4}\nSubnetzmaske = {self._snm}\nMac-Adresse = {self.__mac}\n")

# Instanziieren des Objekt und Ausgabe der Konfiguration über printSettings()
networksetting1 = NetworkSettings("192.168.0.1", "255.255.255.0", "ab:cd:ef:01:23:45")
networksetting1.printSettings()

# IP und SNM mit Setter neu setzen
networksetting1.setIP("172.16.188.0")
networksetting1.setSubnetmask("255.255.255.192")

# Konfiguration erneut anzeigen
networksetting1.printSettings()


# Direkte Änderung versuchen 
networksetting1._ipv4 = "0.0.0.0"  # Änderung möglich, nur protected :(
networksetting1._snm = "0.0.0.0"  # Änderung möglich, nur protected :(
networksetting1.__mac = "00:00:00:00:00:00"  # Private, Änderung nicht möglich :)

# Konfiguration erneut anzeigen
networksetting1.printSettings()
