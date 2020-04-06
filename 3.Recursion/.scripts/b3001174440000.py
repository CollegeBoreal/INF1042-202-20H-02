import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
   from b300117444 import fact
   return fact( 5 ) 
 
def test_answer(bypass):
   assert bypass == 120
