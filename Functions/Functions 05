
#unschön
def listcalc1():
    list1 = [5,10,30]
    list2 = [15,20,10]
    print("[",list1[0]+list2[0],",",list1[1]+list2[1],",",list1[2]+list2[2],"]")
listcalc1()


#besser mit zip und append
def listcalc2():
    lista = [5,10,30]
    listb = [15,20,10]
    listc = []
    for a, b in zip(lista, listb):
            listc.append(a+b)
    print(listc)
listcalc2()


#noch besser mit return
def listcalc3():
    lista = [5,10,30]
    listb = [15,20,10]
    listc = []
    for a, b in zip(lista, listb):
            listc.append(a+b)
    return listc
new_list = listcalc3()
print(new_list)
