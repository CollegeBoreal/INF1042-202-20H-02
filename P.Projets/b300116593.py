# Définition 
dic = {'a': 20, 'b': 30} 
# ou élément après élément : 
 dic={} ; dic['a']=20 ; dic['b']=30
 # ou en utilisant le constructeur dict : 
 dic = dict(a=20, b=30) 
 dic = dict( (('a', 20), ('b', 30)) ) 
 dic = dict(zip(('a','b'), (20,30)))
 type(dic)  # => type builtins.dict (cf. %whos s/IPython) 
 len(dic)   # => 2 paires clé:valeur
 'a' in dic   # test existence clé => True
 20  in dic   # => False, car 20 n'est pas une clé !
 # Récupérer les valeurs
 dic['a']         # => 20 
 dic['c']         # retourne erreur KeyError
 dic.get('a')     # => 20
 dic.get('c','erreur blabla')  # => 'erreur blabla' 
