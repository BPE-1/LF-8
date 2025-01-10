
# (1) Implementieren Sie die Klasse mit den geforderten Eigenschaften.
class NetworkSettings:
    def __init__(self,ipv4=None, snm=None, mac=None):
        self.ipv4 = ipv4
        self.snm = snm
        self.mac = mac
    
    def printSettings(self):
        print(f"\nNetzwerkeinstellungen\nIPV4-Adresse = {self.ipv4}\nSubnetzmaske = {self.snm}\nMac-Adresse = {self.mac}\n")

# (2) Instanziieren Sie Ihre Klasse und lassen Sie sich die Konfiguration über printSettings() ausgeben.

networksetting1 = NetworkSettings("192.168.0.1", "255.255.255.0", "ab:cd:ef:01:23:45")
networksetting1.printSettings()


# (3) Weisen Sie dem erzeugten Objekt im Nachhinein eine neue IPv4 Adresse zu und geben Sie diese nochmal aus.

networksetting1.ipv4 = "10.0.0.1"
print(networksetting1.ipv4)
 
