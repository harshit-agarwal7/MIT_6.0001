annual_salary = float(raw_input("What is your starting annual salary? "))
portion_saved = float(raw_input("What portion of your salary do you plan to save? "))
total_cost = float(raw_input("What is the cost of your dream home? "))
semi_annual_raise = float(raw_input("What's your semi-annual raise?"))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

money_req = total_cost * portion_down_payment
months_to_save_money = 0
monthly_savings = (annual_salary * portion_saved)/12

while money_req > current_savings:
    current_savings = current_savings + monthly_savings + (current_savings * (r/12))
    months_to_save_money = months_to_save_money + 1
    if months_to_save_money % 6 == 0:       # To include semi-annual raise
        monthly_savings = monthly_savings + monthly_savings * semi_annual_raise
        
print months_to_save_money
