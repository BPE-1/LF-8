temps = []

temp1 = float(input("Bitte Temperatur 1 eintragen: "))
temp2 = float(input("Bitte Temperatur 2 eintragen: "))
temp3 = float(input("Bitte Temperatur 3 eintragen: "))
temps.extend([temp1, temp2, temp3])
average = round(sum(temps)/len(temps), 2)

if average <= 30:
    print(average, "°C: Temperature is normal")
elif average >= 30 and average <= 40:
    print(average, "°C: Temperature is higher than normal")
else:
    print(average, "°C: Temperature is too high")

