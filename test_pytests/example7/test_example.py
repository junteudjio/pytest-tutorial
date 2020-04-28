from example import get_and_upper_and_persist

import pytest 


def test_get_and_upper_and_persist(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda:'string-data')
    monkeypatch.setattr('example.db_persist', lambda x:None)
    
    data = get_and_upper_and_persist()
    
    assert data == 'STRING-DATA'
    

    
def test_get_non_string_and_error(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 1)
    
    with pytest.raises(ValueError):
        data = get_and_upper_and_persist()