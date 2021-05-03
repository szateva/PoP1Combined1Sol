import pytest
from question3_implementation import *

# simple case
def test1():
    assert swap_min_max([3, 4, 5, 2, 1]) == [3,4,1,2,5]

# duplicate max
def test2():
    assert swap_min_max([3, 5, 5, 2, 1]) == [3,5,1,2,5]

# duplicate min
def test3():
    assert swap_min_max([3, 1, 5, 2, 1]) == [3,1,1,2,5]

# duplicate min and max
def test4():
    assert swap_min_max([3, 1, 5, 1, 5]) == [3,1,5,5,1]

# 3 minimums
def test5():
    assert swap_min_max([1, 1, 5, 1, 5]) == [1,1,5,5,1]

# negative values
def test6():
    assert swap_min_max([3, 4, 5, 2, -1]) == [3,4,-1,2,5]
