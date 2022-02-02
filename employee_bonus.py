import csv

employee = open("EmployeePay.csv", 'r')
employee_file = csv.reader(employee, delimiter=',')
next(employee_file)

for record in employee_file:
    bonus_pay = float(record[4]) * int(record[3])
    total_pay = bonus_pay + int(record[3])
    print("First Name:", record[1]) 
    print("Last Name:", record[2])
    print("Salary:",'$', format(float(record[3]),',.2f'))
    print("Bonus:",'$', format(bonus_pay, ',.2f'))
    print("Total pay:",'$', format(total_pay,',.2f'))
    input()


employee.close()

