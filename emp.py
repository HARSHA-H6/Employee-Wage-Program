
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


def calc_daily_wage(wage_per_hr, hr_per_day):
    """
        Description:
        This function is used to calculate daily wage of an employee

        Parameter:
        wage_per_hr : It is employee's per hour wage
        hr_per_day : It is employee's per day working hours        

        Return:
        It returns daily wage of employee as integer value
    """   
    daily_wage = hr_per_day * wage_per_hr
    return daily_wage

def part_or_full():
    """
        Description:
        This function is know whether the employee is part time or full time

        Parameter:
        None

        Return:
        It returns an Integer value 1 or 2, for part time or full time
    """
    return random.randint(1,2)   

try:
    if is_present() :
        print("Employee is present today")
        """
        We are using the match since instead of  switch
        Since there is switch case in python
        """
        match part_or_full():
            case 1:
                #When employee is part time
                daily_wage = calc_daily_wage(wage_per_hr=20, hr_per_day=4)
                wage_type = "Part time"
            case 2:
                #When employee is full time
                daily_wage = calc_daily_wage(wage_per_hr=20, hr_per_day=8)
                wage_type = "Full time"
        print(f"Employee's daily wage is {daily_wage} as employee is {wage_type}")
    else:
        print("Employee is absent today")
        
except Exception as e:
    print(f"Exception occured {e} please try again")
     