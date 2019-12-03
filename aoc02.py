print("hello world, this is my solution for Advent of Code 2019 day 2")
print("this is not the correct solution! help :(")
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
    for i in range(len(lista)):
        if lista[i] == 1:
            lista[lista[i+3]] = lista[lista[i+1]] + lista[lista[i+2]]
            i += 4
        elif lista[i] == 2:
            lista[lista[i+3]] = lista[lista[i+1]] * lista[lista[i+2]]
            i += 4
        else:
            break
        return(lista)

#-----()-----
# itt nincs olyan hogy int main() de ha lenne akkor ez lenne az
#-----()-----
print(darabolo(o_lista))
