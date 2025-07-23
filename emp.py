
import random

# Creating the constants so Readablity and maintainablity of the code increases
WAGE_PER_HR = 20
PART_TIME_HRS = 4
FULL_TIME_HRS = 8
MAX_WORKING_DAYS = 20
MAX_WORKING_HRS = 100


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


def calc_daily_wage(WAGE_PER_HR, hr_per_day)->int:
    """
        Description:
        This function is used to calculate daily wage of an employee

        Parameter:
        wage_per_hr : It is employee's per hour wage
        hr_per_day : It is employee's per day working hours        

        Return:
        It returns daily wage of employee as integer value
    """   
    daily_wage = hr_per_day * WAGE_PER_HR
    return daily_wage

def part_or_full() ->int :
    """
        Description:
        This function is know whether the employee is part time or full time

        Parameter:
        None

        Return:
        It returns an Integer value 1 or 2, for part time or full time
    """
    return random.randint(1,2)   


#initializing monthly wage
monthly_wage = 0
emp_present = 0
total_hrs = 0

try:
    while True:
        #loop till this condition become true
        if total_hrs < MAX_WORKING_HRS and emp_present < MAX_WORKING_HRS:
            if is_present() :
                #employee is present
                emp_present += 1
                match part_or_full():
                    case 1:
                        #When employee is part time
                        hr_per_day = PART_TIME_HRS
                        
                    case 2:
                        hr_per_day = FULL_TIME_HRS
                        
                daily_wage = calc_daily_wage(WAGE_PER_HR,hr_per_day)
                total_hrs += hr_per_day
                monthly_wage += daily_wage
            else:
                #employee is absent
                total_hrs += 0
                monthly_wage += 0
        else:
            
            break
            
except Exception as e:
    print(f"Exception occured {e} please try again")

print(f"Employee's monthly wage is ₹{monthly_wage} for a month of {MAX_WORKING_DAYS} working days",
      f"Employee was present for {emp_present} days with total working hours of {total_hrs} hrs" ,sep='\n')
    