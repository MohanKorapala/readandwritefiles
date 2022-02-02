import csv

counter = 0

customers = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

customer_file = csv.reader(customers, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)

outfile.write("First Name, " + "Last Name," + " Country" + '\n')

for record in customer_file:
    first = record[1]
    last = record[2]
    country = record[4]
    counter += 1
    outfile.write(first + ', ' + last + ', '+ country + '\n')

print("Total number of customers:",counter)
outfile.close()

   