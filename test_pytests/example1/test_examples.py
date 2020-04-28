def add_one(x):
    return x + 1

def test_add_one():
    assert add_one(3) == 5
    
def test_dicts_equality():
    assert {'a':1, 'b':2, 'c': 3} == {'a':0, 'd':2, 'c': 3}