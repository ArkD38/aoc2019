print("hello world, this is my solution for Advent of Code 2019 day 2")
o_lista = [] #Ebbe megy a bemenet


#-----()-----
# Beolvasás
#-----()-----

with open("in.txt", "r") as f:
    o_lista = f.read().split(",")
for i in range(len(o_lista)):
    o_lista[i] = int(o_lista[i])
print(o_lista)



#-----()-----
# Függvények
#-----()-----

def darabolo(lista):
    #lista <- o_lista
    i = 0
    while i+3 < len(lista) and (lista[i] == 1 or lista[i] == 2):
        if lista[i] == 1:
            lista[lista[i+3]] = lista[lista[i+1]] + lista[lista[i+2]]
        elif lista[i] == 2:
            lista[lista[i+3]] = lista[lista[i+1]] * lista[lista[i+2]]
        i += 4
    return(lista)



print(darabolo(o_lista))
