#!/bin/sh

# --------------------------------------
# Spec (test) specific file
# Use this to customize the testing files
# code: Binary Search 
# --------------------------------------

generate_spec () {
   echo "import sys; sys.path.append('.') # Rajouter le repertoire courant" > .scripts/b${id}0000.py
   echo "import pytest" >> .scripts/b${id}0000.py
   echo " " >> .scripts/b${id}0000.py
   echo "@pytest.fixture" >> .scripts/b${id}0000.py
   echo "def bypass():" >> .scripts/b${id}0000.py
   echo "   from b${id} import quicksort" >> .scripts/b${id}0000.py
   echo "   return quicksort( [10,5,2,3] ) " >> .scripts/b${id}0000.py
   echo " " >> .scripts/b${id}0000.py
   echo "def test_answer(bypass):" >> .scripts/b${id}0000.py
   echo "   assert bypass == [2,3,5,10]" >> .scripts/b${id}0000.py
}

