import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
   from b300117178 import search
   return search("Boris")
 
def test_answer(bypass):
   assert bypass == True