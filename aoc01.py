#ez a második részre a megoldás, ha az elsőre kell akkor afaik csak a 20. sorba nem kell a fuelfuel()

adatok = [] #ebbe vannak beolvasva az adatok
eredmeny = 0 #ez lesz a kimenet

def muvelet(kcs):
    return (kcs//3)-2

def fuelfuel(o_mass):
    #o_mass = adatok[i]
    #nem akartam rekurziót használni, mert bucsi már megcsinálta azzal
    ez = o_mass
    while ez > 8:
        ez = muvelet(ez)
        o_mass += ez
    return o_mass

with open("aoc201901.txt","r") as f:
    adatok=f.read().split("\n")
for i in range(0,len(adatok)):
    adatok[i] = fuelfuel(muvelet(int(adatok[i])))
    eredmeny += adatok[i]
    
print(eredmeny)
