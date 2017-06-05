semi_annual_raise = 0.07
annual_return = 0.04
down_payment = 0.25
cost_of_house = 1000000

money_req = down_payment * cost_of_house

annual_salary = float(raw_input("What is your annual salary? "))

months_to_save = 36
curr_savings = 0
portion_saved = float(5000)/10000
steps = 0
low = float(0)
high = float(10000)/10000


while abs( curr_savings - money_req) >= 100:
    monthly_savings = (annual_salary * portion_saved)/12
    for i in range (1,37):
        curr_savings = curr_savings + monthly_savings + (curr_savings * (annual_return/12))
        if i%6 == 0:
            monthly_savings = monthly_savings + (monthly_savings * semi_annual_raise)
            
    steps = steps + 1
    
    if curr_savings > money_req:
        high = portion_saved
    elif curr_savings < money_req:
        low = portion_saved
    portion_saved = (high+low)/2
    
print ("Best savings rate: %s") %portion_saved
print ("Steps in bisection search: %s") %steps
