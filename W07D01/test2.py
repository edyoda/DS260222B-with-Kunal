# Another method of testing 
# 2) Marking the test case
import pytest
def funct1(fruits):
    '''
    the parameter fruits would be a list
    '''
    if 'litchi' in fruits:
        return 'litchi'
    else:
        return None
@pytest.mark.saikumar
def test_1(): #test case 1
    assert funct1(['litchi','mango','orange']) == 'litchi'
@pytest.mark.charulingah
def test_2(): #test case 2
    assert funct1(['banana','mango','orange']) == 'mango'
@pytest.mark.vinay
def test_3(): #test case 3
    assert funct1(['banana','mango','orange']) == None
@pytest.mark.mayank
def test_4():
    assert funct1(['banana','mango','orange']) == False

    
# py.test test2.py -m charulingah