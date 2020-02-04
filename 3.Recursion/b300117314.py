
"" Morti"

a=int(input("entrer un chiffre\n") )
x =a
def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)
print("Le resultat est :")
print(fact(x))
