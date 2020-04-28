import pytest

def add_one(x):
    return x + 1

@pytest.mark.parametrize('num, expected', 
                         [(1, 2), (2, 3), (5, 6)])
def test_add_one(num, expected):
    assert add_one(num) == expected