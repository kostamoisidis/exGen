import random
import numpy as np

a = np.empty( 15, int )
b = np.empty( 15, int )

for i in range(15):
    a[i]= random.randint( 0, 999999 )
    b[i]= random.randint( 0, 999 )


for i in range(15):
    print( i, ",", " ", a[i], ":", b[i], sep="" )

for i in range(15):
    print( a[i], ":", b[i], "=", a[i]//b[i], "(", a[i]%b[i],")" )