import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
   from b300118196 import selectionSort
   return selectionSort( [5, 3, 6, 2, 10])
def test_answer(bypass):
   assert bypass == [2, 3, 5, 6, 10]
