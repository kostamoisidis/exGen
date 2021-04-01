import random
import numpy as np
#
# a    c
# -- + --
# b    b
# 

a = np.empty( 15, int )
b = np.empty( 15, int )
c = np.empty( 15, int )
d = np.empty( 15, int )

for i in range(15):
    a[i]= random.randint( 0, 20 )
    b[i]= random.randint( 0, 50 )
    c[i]= random.randint( 0, 20 )
    d[i]= random.randint( 0, 50 )
    

for i in range(15):
    print( i, ",", sep="" )

    if a[i] < 10:
        print( " ", a[i], "    ", c[i], sep="" )
    else:
        print( " ", a[i], "   ", c[i], sep="" )

    print( " ", "--", " + ", "--", sep="" )

    if b[i] < 10:
        print( " ", b[i], "    ", d[i], sep="" )
    else:
        print( " ", b[i], "   ", d[i], sep="" )
    
    print("========")

def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

print()
print("========Vysledky=======")

for i in range(15):
    print( i, ",", sep="" )
    
    if b[i] == 0 or d[i] == 0:
        if a[i] < 10:
            print( " ", a[i], "    ", c[i], sep="" )
        else:
            print( " ", a[i], "   ", c[i], sep="" )

        print( " ", "--", " + ", "--", " = ", "NELZE", sep="" )

        if b[i] < 10 or d[i] < 10:
            print( " ", b[i], "    ", d[i], sep="" )
        else:
            print( " ", b[i], "   ", d[i], sep=""  )
        
        print("========")
    
    else:
        lcm = compute_lcm( b[i], d[i] )
        cit1 = ( lcm / b[i] ) * a[i]
        cit2 = ( lcm / d[i] ) * c[i]
        finCit = cit1 + cit2

        if a[i] < 10:
            print( " ", a[i], "    ", c[i], "   ", int(finCit),sep="" )
        else:
            print( " ", a[i], "   ", c[i], "    ", int(finCit),sep="" )

        print( " ", "--", " + ", "--", " = ", "--", sep="" )

        if b[i] < 10 or d[i] < 10:
            if b[i] < 10 and d[i] < 10:
                print( " ", b[i], "    ", d[i], "    ", lcm,sep="" )
            else:
                print( " ", b[i], "    ", d[i], "   ", lcm,sep="" )
        else:
            print( " ", b[i], "   ", d[i], "   ", lcm, sep=""  )
        
        print("========")