import random

def is_present()->int:
    """
        Description:
        This function is used to tell whether the employee is present or not

        Parameter:
        None
        Return:
        It returns a int value 0 or 1 based on random.randint(0,1)
        If the return value is 1 than it is considered as present else absent.
    """
    
    return random.randint(0,1)

try:
    if is_present() == 1 :
        print("Employee is present today")
    else:
        print("Employee is absent today")
        
except Exception as e:
    print(f"Exception occured {e} please try again")