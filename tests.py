from functions import *

def test_1():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(10) == 'buzz'
    assert fizzbuzz(15) == 'fizzbuzz'
    assert fizzbuzz(0) == None
    assert fizzbuzz(-5) == None
    assert fizzbuzz('Mama') == None
    assert fizzbuzz(1.7) == None
    assert fizzbuzz('0') == None