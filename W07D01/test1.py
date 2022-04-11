# Way of selecting the filtering test case
# 1) Running the test cases with substring matching
# approach


def funct1(fruits):
    '''
    the parameter fruits would be a list
    '''
    if 'litchi' in fruits:
        return 'litchi'
    else:
        return None

def test_armaan_1(): #test case 1
    assert funct1(['litchi','mango','orange']) == 'litchi'
    
def test_armaan_2(): #test case 2
    assert funct1(['banana','mango','orange']) == 'mango'
 
def test_sayali_1(): #test case 3
    assert funct1(['banana','mango','orange']) == None
#cmd py.test test1.py -k test_a