def bin_conv(x,v):
    print("IP Dezimal:",x)
    print("SNM Dezimal:",v)
# Parameter x auf "." splitten, X ist nun eine Liste mit str Elementen
    x = x.split(".")
    v = v.split(".")
    
# Listenelemte in integer umwandeln mit for schleife 
    x = [int(octet) for octet in x]
    v = [int(octet) for octet in v]
    
# Listen für die Binär-Ergebnisse der einzelnen Oktete
    safelist0 = []
    safelist1 = []
    safelist2 = []
    safelist3 = []

    safelistv0 = []
    safelistv1 = []
    safelistv2 = []
    safelistv3 = []


# Ausrechnung der einzelnen Oktette / Rest wird der Liste hinzugefügt und am Ende wird die Liste reversed
    while x[0] != 0:
        y = x[0] % 2
        safelist0.append(y)
        x[0] = x[0] // 2
    safelist0.reverse()
    
    while x[1] != 0:
        y = x[1] % 2
        safelist1.append(y)
        x[1] = x[1] // 2
    safelist1.reverse()
        
    while x[2] != 0:
        y = x[2] % 2
        safelist2.append(y)
        x[2] = x[2] // 2
    safelist2.reverse()  
               
    while x[3] != 0:
        y = x[3] % 2
        safelist3.append(y)
        x[3] = x[3] // 2
    safelist3.reverse()

    #SNM Rechnung  
    while v[0] != 0:
        c = v[0] % 2
        safelistv0.append(c)
        v[0] = v[0] // 2
    safelistv0.reverse()
    
    while v[1] != 0:
        c = v[1] % 2
        safelistv1.append(c)
        v[1] = v[1] // 2
    safelistv1.reverse()
        
    while v[2] != 0:
        c = v[2] % 2
        safelistv2.append(c)
        v[2] = v[2] // 2
    safelistv2.reverse()  
               
    while v[3] != 0:
        c = v[3] % 2
        safelistv3.append(c)
        v[3] = v[3] // 2
    safelistv3.reverse()
   
# Listenelemente zusammenfügen und in str umwandeln mit anschließender Ausgabe    
    s0 = "".join(map(str, safelist0))
    s1 = "".join(map(str, safelist1))
    s2 = "".join(map(str, safelist2))
    s3 = "".join(map(str, safelist3))
    print("IP Binär: "+s0+"."+s1+"."+s2+"."+s3)
    
    sv0 = "".join(map(str, safelistv0))
    sv1 = "".join(map(str, safelistv1))
    sv2 = "".join(map(str, safelistv2))
    sv3 = "".join(map(str, safelistv3))
    print("SNM Binär: "+sv0+"."+sv1+"."+sv2+"."+sv3)
    
# Listenelemte mit 0 auffüllen für 8 Bit Darstellung
    s80 = s0.rjust(8,"0")
    s81 = s1.rjust(8,"0")
    s82 = s2.rjust(8,"0")
    s83 = s3.rjust(8,"0")
    print("IP Binär (8 Bit): "+s80+"."+s81+"."+s82+"."+s83)
    
    sv80 = sv0.rjust(8,"0")
    sv81 = sv1.rjust(8,"0")
    sv82 = sv2.rjust(8,"0")
    sv83 = sv3.rjust(8,"0")
    print("SNM Binär (8 Bit): "+sv80+"."+sv81+"."+sv82+"."+sv83)


bin_conv("25.172.10.10","255.255.255.0")
bin_conv(input("Bitte IP-Adresse eingeben: "), input("Bitte Subnetzmaske eingeben: "))
