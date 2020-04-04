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
   echo "   from b${id} import search" >> .scripts/b${id}0000.py
   echo "   return search(\"Boris\")" >> .scripts/b${id}0000.py
   echo " " >> .scripts/b${id}0000.py
   echo "def test_answer(bypass):" >> .scripts/b${id}0000.py
   echo "   assert bypass == True" >> .scripts/b${id}0000.py
}

