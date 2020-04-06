import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
   from b300117314 import ajout
   return ajout(('ma_cle', [0,1,2,3,4]))['ma_cle'] 
 
def test_answer(bypass):
   assert bypass  == [0,1,2,3,4]  
