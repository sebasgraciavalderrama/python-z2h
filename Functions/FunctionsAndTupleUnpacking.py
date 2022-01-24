stock_prices = [('APPLE', 200), ('MS', 400), ('GOOGLE', 15000)]
for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(ticker)

for ticker, price in stock_prices:
    print(price+(0.1*price))


work_hours = [('Abby', 200), ('Billy', 4000), ('Cassie', 800)]

def employee_check (work_hours):
    current_max = 0
    employee_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_month = employee
        else:
            pass
    return (employee_month, current_max)

name, hours = employee_check(work_hours)
print(name)
print(hours)

item = employee_check(work_hours)

print(employee_check(work_hours))