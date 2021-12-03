"""
William McClain
test_org.py
Problem: Testing the classes of sales_force and sales_person
Affirmation: I affirm that this code is all my own work.
"""
from sales_person import SalesPerson
from sales_force import SalesForce


stan = SalesPerson(123, "Stan")
stan.enter_sale(1234)
stan.enter_sale(2341)
stan.enter_sale(3412)
stan.enter_sale(4123)
print(stan.get_id())
print(stan.get_name())
print(stan.get_sales())
print(stan.total_sales())
print(stan.met_quota(10000))


print()

mark = SalesPerson(321, "Mark")
mark.enter_sale(1234)
mark.enter_sale(2341)
mark.enter_sale(3412)
mark.enter_sale(4123)
print(mark.get_id())
print(mark.get_name())
print(mark.get_sales())
print(mark.total_sales())
print(mark.met_quota(10000))


print()

stan.set_name('Kimberly')

print()

print(stan.personnel_info())
print(mark.personnel_info())
print(stan.compare_to(mark))

all_per = SalesForce()
all_per.add_data('salesData.txt')
print(all_per.get_list())
print(all_per.quota_report(1000))

print(all_per.top_seller())
print(all_per.individual_sales(345))
