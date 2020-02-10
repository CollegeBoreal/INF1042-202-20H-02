#-*- coding : utf-8 -*-

import math

def fact(x):                        # declaration de la fonction
        if x == 1:
            return 1
        else :
            return x*fact(x-1)

print(fact(5))              #appelle de la fonction

        
        
