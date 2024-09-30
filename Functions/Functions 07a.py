# Aufgabe 7a  // Hosts aus CIDR berechnen

def netmask_hosts(x):
    x = 2**(32 - x)
    x1 = x-2
    print("Maximal", x,"IP-Adressen.\nDavon sind",x1,"frei zu vergeben.\n2 IP´s sind immer fest vergeben (Netzadresse & Broadcastadresse).")

netmask_hosts(25)
netmask_hosts(int(input("Bitte CIDR eingeben: ")))
