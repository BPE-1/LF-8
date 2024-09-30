def cidr_conv(x):
    x = int(x)
    host_bits = x % 8
    oct_number = x // 8
    
    if host_bits == 0:
        host_bits = "0"
    if host_bits == 1:
        host_bits = "128"
    elif host_bits == 2:
        host_bits = "192"
    elif host_bits == 3:
        host_bits = "224"
    elif host_bits == 4:
        host_bits = "240"
    elif host_bits == 5:
        host_bits = "248"
    elif host_bits == 6:
        host_bits = "252"
    elif host_bits == 7:
        host_bits = "254"
    
    if oct_number == 0:
        oct_number = host_bits+".0.0.0"
    elif oct_number == 1:
        oct_number = "255."+host_bits+".0.0"
    elif oct_number == 2:
        oct_number = "255.255."+host_bits+".0"
    elif oct_number == 3:
        oct_number = "255.255.255."+host_bits
    elif oct_number == 4:
        oct_number = "255.255.255.255"
            
    print("Die Subnetzmaske lautet:", oct_number)
    
    
cidr_conv(32)
cidr_conv(int(input("Bitte CIDR Wert eingeben: ")))
