# coding=utf-8
import sys; sys.path.append('.') # Rajouter le repertoire courant
import pytest
 
@pytest.fixture
def bypass():
   from b300116685 import rightTriangle
   return rightTriangle(11) 
 
def test_answer(bypass):
   assert bypass  == [(8, 6, 10)] 
