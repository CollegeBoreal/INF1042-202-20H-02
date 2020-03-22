import sys; sys.path.append('.') # Rajouter le repertoire courant
from b300115065 import search
test = search('Boris') == 'Zoureni'  
if  test:
     print('--------------------')
     print(':tada: :tada: :tada:')
else:
     print('--------------------')
     print(':no_entry: :no_entry: :interrobang:')
