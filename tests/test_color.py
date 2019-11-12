import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_find_black():
    blacks = playground.color.find_black([(255,255,255),(0,0,0),(20,20,20)])
    assert blacks == [(0,0,0)]  
    
def test_find_black_empty():
    blacks = playground.color.find_black([])
    assert blacks == []  

def test_find_black_same_vals():
    blacks = playground.color.find_black([(2,0,0),(0,1,0),(0,0,3)])
    assert blacks == [(0,1,0)]  
