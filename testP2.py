import pytest
from parcial2_prog1 import is_mutant

def test_non_mutant():
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    assert is_mutant(dna) == False

def test_mutant_diagonal():
    dna = ["ATGCGA", "CATGGC", "TTATGT", "AGAAGG", "CGCCTA", "TCACTG"]
    assert is_mutant(dna) == True

def test_mutant_inverse_diagonal():
    dna = ["ATGCGA", "CAGTAC", "TTGTGT", "AGAAGG", "CCCCTA", "TCACTG"]
    assert is_mutant(dna) == True

