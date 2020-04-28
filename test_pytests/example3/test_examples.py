import pytest

@pytest.mark.slow
@pytest.mark.integration
def test_http_call():
    pass
    
    
@pytest.mark.slow
def test_http_call2():
    pass
    
    
@pytest.mark.fast
@pytest.mark.unit
def test_add():
    pass
    
@pytest.mark.unit
def test_add2():
    pass