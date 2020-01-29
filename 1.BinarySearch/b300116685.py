"""cher amis ce programmer consiste a calculer
le somme d'un liste des numero"""

def list_sum(num_list) :
    if len (num_list) ==1 :
        return num_list [0]
    else:
        return  num_list [0]+ list_sum(num_list[1:])

print(list_sum([2,4,5,6,7]))