def funct1(fruits):
    '''
    the parameter fruits would be a list
    '''
    if 'litchi' in fruits:
        return 'litchi'
    else:
        return None

def test_method(): #test case 1
    assert funct1(['litchi','mango','orange']) == 'litchi'
    
def test_method_1(): #test case 2
    assert funct1(['banana','mango','orange']) == 'mango'
