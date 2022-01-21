"""
Jessica Davis
Monthly Interest
The problem being solved is calculating the monthly interest charge for the billing cycle.
This is my work and no one elses - Jessica Davis
"""

def monthly_interest():
    annual_interest = eval(input("enter the annual interest rate: "))
    days_in_cycle = eval(input("enter the number of days in cycle: "))
    previous_balance = eval(input("enter the previous balance: "))
    payment_amount = eval(input("enter the payment amount: "))
    payment_made = eval(input("enter the day payment was made: "))
    step_one = previous_balance * days_in_cycle
    step_two = payment_amount * (days_in_cycle - payment_made)
    step_three = step_one - step_two
    avg_daily_balance = step_three / 31
    print ("average daily balance =", avg_daily_balance)
    monthly_interest = avg_daily_balance * (annual_interest / 12 /100)
    print ("monthly interest = $", monthly_interest)







