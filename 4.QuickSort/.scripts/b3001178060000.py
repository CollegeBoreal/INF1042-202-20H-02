import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
   from b300117806 import quicksort
   return quicksort( [10,5,2,3] ) 
 
def test_answer(bypass):
   assert bypass == [2,3,5,10]
