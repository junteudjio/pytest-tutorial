import os 

def test_one(monkeypatch):
    monkeypatch.setenv('FOO', 'BAR')
    assert 'FOO' in os.environ
    
def test_two():
    assert 'FOO' not in os.environ