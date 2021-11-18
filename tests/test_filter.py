from src.filter import Filter


def func(x):
    return x+1

def test_answer():
    assert func(3)==4

def test_filter():
    f = Filter('request.method.GET')
    assert f.comparator=='GET'
    assert f.fields==['request','method']
