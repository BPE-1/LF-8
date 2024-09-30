def bin_conv(x,v):
    print("IP Dezimal:",x)
    print("SNM Dezimal:",v)
    x = x.split(".")
    v = v.split(".")

    x = [int(octet) for octet in x]
    v = [int(octet) for octet in v]
    
    ip0 = bin(x[0])[2:]
    ip1 = bin(x[1])[2:]
    ip2 = bin(x[2])[2:]
    ip3 = bin(x[3])[2:]
    ipbin = ip0+"."+ip1+"."+ip2+"."+ip3
    
    snm0 = bin(v[0])[2:]
    snm1 = bin(v[1])[2:]
    snm2 = bin(v[2])[2:]
    snm3 = bin(v[3])[2:]
    snmbin = snm0+"."+snm1+"."+snm2+"."+snm3
    
    print(ipbin)
    print(snmbin)
    

    ip00 = ip0.zfill(8)
    ip01 = ip1.zfill(8)
    ip02 = ip2.zfill(8)
    ip03 = ip3.zfill(8)
    ip8bin = ip00+"."+ip01+"."+ip02+"."+ip03
   
    snm00 = snm0.zfill(8)
    snm01 = snm1.zfill(8)
    snm02 = snm2.zfill(8)
    snm03 = snm3.zfill(8)
    snm8bin = snm00+"."+snm01+"."+snm02+"."+snm03
    
    print(ip8bin)
    print(snm8bin)
    
    
bin_conv("25.172.10.10","255.255.255.0")
bin_conv(input("Bitte IP-Adresse eingeben: "), input("Bitte Subnetzmaske eingeben: "))
