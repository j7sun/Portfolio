import tkinter as tk

#I modified this function from http://stackoverflow.com/questions/33518978/python-how-to-limit-an-entry-box-to-2-characters-max
def entry_limit(*args): 
    """Check the length of entry and limit the number of input to 4.
    
    Parameters
    -----------
    *args: int 
        Integers correponding to their buttons
    
    Returns
    -----------
    output: set
        A set of 4-digit-code will be the entry ouput
    """
    my_input = passcode_input.get()
    
    if len(my_input) > 4:
        
        passcode_input.set(my_input[:4])


def click_button(tapped_code): 
    """Allow the corresponding number to appear in entry when its button is clicked.
    Clear the screen before the next code input so the integers appear in order
    
    current_entry = passcode_entry.get()  
    
    Parameters
    ----------
    tapped_code: integer
        Integers correponding to their buttons
    
    Returns
    ----------
    output: string
        String concatenation of the 4-digit-code after their
        corresponding button is clicked.
    """
   
    current_entry = passcode_entry.get()
    
    passcode_entry.delete(0, 4)   
    
    passcode_entered = passcode_entry.insert(0, current_entry + str(tapped_code))
    
    return passcode_entered


def lock_button():
    """Lock the box when 4-digit-passcode is typed in the entry
    
    Parameters
    ----------
    
    Returns
    ----------
    output: string
        String value is 'LOCK' if entry length is 4, otherwise the value is 'FAIL'.
   """
    
    global final_entry
    
    final_entry = passcode_entry.get()
    
    if len(final_entry) == 4:

        passcode_entry.insert(0, 'LOCK')
        
    else: 

        passcode_entry.insert(0, 'FAIL')
        

def open_box():
    """Open the box if new code matches with the 4-digit-passcode when box is locked.
    
    Parameters
    ----------
    
    Returns
    ----------
    output : string
        String value is 'OPEN' if code matches, otherwise the value is 'FAIL'.
    """
    
    new_code = passcode_entry.get()
    
    if new_code == final_entry:

        passcode_entry.insert(0, 'OPEN')

    elif new_code != final_entry:

        passcode_entry.insert(0, 'FAIL')
        

def clear_button():
    """Clear all the code input in entry box(up to 4 digits),
    Clear the input before typing new code to execute open_box().
    
    Parameters
    ----------
    
    Returns
    ----------
    """
    
    passcode_entry.delete(0, 4)

    