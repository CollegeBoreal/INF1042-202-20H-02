import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
from b300117782 import binary_search
   return binary_search( [5,7,11,14,19,20,25], 11) 
 
def test_answer(bypass):
   assert bypass == 2
