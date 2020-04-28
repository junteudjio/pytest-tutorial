def test_one(tmpdir):
    (tmpdir / 'foo.txt').write('hello world!')
    assert 1 == len(tmpdir.listdir())
    
def test_two(tmpdir):
    assert 0 == len(tmpdir.listdir())