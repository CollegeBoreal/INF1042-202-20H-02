import sys; sys.path.append('.') # Rajouter le repertoire courant
from b300115140 import search
test = search('Boris') == True  
if  test:
     print('--------------------')
     print(':tada: :tada: :tada:')
else:
     print('--------------------')
     print(':no_entry: :no_entry: :interrobang:')
