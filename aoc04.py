print("Advent of Code day 4")

#FIGYELEM: nagyon csúnya a megoldás,
#és nagyon hosszú is, és a változónevek is retardáltak.


range1 = "246515"
range2 = "739105"

#   It is a six-digit number.
#   The value is within the range given in your puzzle input.

#   Two adjacent digits are the same (like 22 in 122345).

em = False #ennek igaznak kell lennie

#   Going from left to right, the digits never decrease
#       they only ever increase or stay the same (like 111123 or 135679).

incr = True #ez legyen igaz

solutions = []

#-----()-----
#  megoldás
#-----()-----

for i in range(int(range1),int(range2)+1):
    j=0
    k=0
    em = False
    incr = True
    while j < 5 and em == False:
        if str(i)[j] == str(i)[j+1]:
            em = True
        j+=1
    while k < 5 and incr == True:
        if int(str(i)[k]) > int(str(i)[k+1]):
            incr = False
        k+=1
    if em and incr:
        solutions.append(str(i))
print("első feladat megoldása: ", len(solutions))


#második feladat
sol2 = 0
for i in solutions:
    l = 0
    vane2 = False
    while vane2 == False and l < 6:
        if i.count(i[l])==2:
            sol2 += 1
            vane2 = True
        l += 1
print(sol2)
