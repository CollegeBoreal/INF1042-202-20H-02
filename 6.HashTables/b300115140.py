#Mon code HashTable


recetteskabyles = {}
recetteskabyles ['hasbana'] = ['huile', 'tomtes', 'semoule', 'boeuf', 'razelhanout', 'menthe']
recetteskabyles ['brickaloeuf'] = ['feuilledebrick', 'oeufs', 'fromage', 'epices', 'huile']

def ajout(tuple):
    mousaoui, aitzetoun = tuple
    recetteskabyles [mousaoui] = aitzetoun
    return recetteskabyles

[ x for x in recetteskabyles.keys() ]
[ x for x in recetteskabyles.values() ]

print (ajout(('ma_cle',[0,1,2,3,4])))
