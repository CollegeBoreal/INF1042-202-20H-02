import sys; sys.path.append('.') # Rajouter le repertoire courant
from b300117782 import ajout
test = ajout(('ma_cle', [0,1,2,3,4]))['ma_cle'] == [0,1,2,3,4]  
if  test:
     print('--------------------')
     print(':tada: :tada: :tada:')
else:
     print('--------------------')
     print(':no_entry: :no_entry: :interrobang:')
