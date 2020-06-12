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

    
#Setting up the gui and give it a name
root = tk.Tk()
root.title("Lock Box")

#Create a main frame widget, set its color and position
main_frame = tk.Frame(root, bg = 'grey75')
main_frame.grid(ipadx= 1, ipady = 1)

#Create a seperate frame widget that organizes the button widgets
tab_frame = tk.Frame(main_frame,bg = 'grey30')
tab_frame.grid(row = 1, column = 1)

# Stating that requriement of the lock box entry is a 4-digit-passcode
entry_requirement = tk.Label(main_frame,text = '4 Digit Pin#')
entry_requirement.grid(row = 0)


passcode_input = tk.StringVar()                 #Define an instance 
passcode_input.trace('w', entry_limit)          #Bind my function entry_limit to this instance


#Pass instance that carries the entry_limit function into the entry widget to trigger entry_limit() 
passcode_entry = tk.Entry(main_frame, width = 30, bd = 8, \
                textvariable = passcode_input, font = ("Arial",20))  

#Locate entry box at the top of the frame widget
passcode_entry.grid(row = 0, column = 1, columnspan = 1, ipadx = 30, ipady = 30 )


#Create integer buttons widgets, use lambda as a anonymous function inside the button_click function
Button_1 = tk.Button(tab_frame, text = '1', command = lambda : click_button(1)) 
Button_2 = tk.Button(tab_frame, text = '2', command = lambda : click_button(2))
Button_3 = tk.Button(tab_frame, text = '3', command = lambda : click_button(3))
Button_4 = tk.Button(tab_frame, text = '4', command = lambda : click_button(4))
Button_5 = tk.Button(tab_frame, text = '5', command = lambda : click_button(5))
Button_6 = tk.Button(tab_frame, text = '6', command = lambda : click_button(6))
Button_7 = tk.Button(tab_frame, text = '7', command = lambda : click_button(7))
Button_8 = tk.Button(tab_frame, text = '8', command = lambda : click_button(8))
Button_9 = tk.Button(tab_frame, text = '9', command = lambda : click_button(9))
Button_0 = tk.Button(tab_frame, text = '0', command = lambda : click_button(0))

# Create buttons widgets and assign funcitons to buttons when they are clicked
Button_clear = tk.Button(tab_frame, text = 'Clear', fg = 'orange', command = clear_button)
Button_lock = tk.Button(tab_frame, text = 'Lock', fg = 'red', command = lock_button)
Button_open = tk.Button(main_frame, text = 'Open', fg = 'green', command = open_box)

#Organizing button widgets in a table-like strucutre that is similar to tabs on real lock box
#Allow Button_open to appear on top of the frame widget and make it stick to the right
Button_open.grid(row = 0, column = 2, ipadx = 25, ipady = 40, sticky = 'e') 

#Organizing button widgets in the first row
Button_1.grid(row = 1, column = 0, ipadx = 40, ipady = 40, padx = 10, pady = 10)
Button_2.grid(row = 1, column = 1, ipadx = 40, ipady = 40, padx = 10, pady = 10)
Button_3.grid(row = 1, column = 2, ipadx = 40, ipady = 40, padx = 10, pady = 10)

#Organizing button widgets in the second row
Button_4.grid(row = 2, column = 0, ipadx = 40, ipady = 40, padx = 10, pady = 10)
Button_5.grid(row = 2, column = 1, ipadx = 40, ipady = 40, padx = 10, pady = 10)
Button_6.grid(row = 2, column = 2, ipadx = 40, ipady = 40, padx = 10, pady = 10)

#Organizing button widgets in the third row
Button_7.grid(row = 3, column = 0, ipadx = 40, ipady = 40, padx = 10, pady = 10)
Button_8.grid(row = 3, column = 1, ipadx = 40, ipady = 40, padx = 10, pady = 10)
Button_9.grid(row = 3, column = 2, ipadx = 40, ipady = 40, padx = 10, pady = 10)

#Organizing button widgets in the fourth row
Button_0.grid(row = 4, column = 0, ipadx = 40, ipady = 40, padx = 10, pady = 10)
Button_clear.grid(row = 4, column = 1, ipadx = 30, ipady = 40, padx = 10, pady = 10)
Button_lock.grid(row = 4, column = 2, ipadx = 30, ipady = 40, padx = 10, pady = 10)

#Execute tkinter and allow a GUI to show up
root.mainloop()