import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
   from b300117178 import rightTriangle
   return rightTriangle(11) 
 
def test_answer(bypass):
   assert bypass  == [(8, 6, 10)] 
