from my_function import *

def test_entry_limit():
    
    #Write multiple asserts
    
    assert callable(entry_limit)
    assert isinstance(entry_limit([1, 2, 3, 4]), set)
    assert entry_limit([1, 2, 3, 4, 5]) == {1, 2, 3, 4}




def test_click_button(): 
    
    #Write multiple asserts
    
    assert callable(click_button)
    assert isinstance(click_button(1), str)
    assert click_button(1) == '1'



def test_lock_button():
    
    #Write multiple asserts
    assert callable(lock_button)
    assert isinstance(lock_button('mark'), str)
    assert lock_button('abc') == 'FAIL'
    




    



 



