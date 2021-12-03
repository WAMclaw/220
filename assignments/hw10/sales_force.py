"""
William McClain
sales_force.py
Problem: Create a class for the Sales Force of an organization
Affirmation: I affirm that this is all my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    """
    The class for creating an organizations sales employees
    """

    def __init__(self):
        """
        initializes SalesForce class
        """
        self.sales_people = []

    def add_data(self, file_name):
        """
        reads data from a file of all of the sales employees and creates a list of
        SalesPerson objects [sales_people]
        """
        personnel_file = open(file_name, 'r')
        count = 0
        for line_info in personnel_file:
            line_in = str(line_info.strip('\n'))
            # self.sales_people.append(line_in)
            line_in_l = line_in.split(", ")
            self.sales_people.append(SalesPerson(int(line_in_l[0]), str(line_in_l[1])))
            for sal_item in line_in_l[2].split():
                self.sales_people[count].enter_sale(float(sal_item))
            count += 1
        personnel_file.close()

    def get_list(self):
        """
        returns the list of sales_people
        """
        return self.sales_people

    def quota_report(self, quota):
        """
        returns a list of quotas of all employees
        """
        list_quota = []
        for person in range(len(self.sales_people)):
            pl_l = [self.sales_people[person].get_id(), self.sales_people[person].get_name(),
                    self.sales_people[person].total_sales(),
                    self.sales_people[person].met_quota(quota)]
            list_quota.append(pl_l)
        return list_quota

    def top_seller(self):
        """
        returns a list of the top sellers in the organization
        """
        sales = []
        obj_high = []
        for person in range(len(self.sales_people)):
            sales.append(self.sales_people[person].total_sales())
        for person in range(len(self.sales_people)):
            if max(sales) == self.sales_people[person].total_sales():
                obj_high.append(self.sales_people[person])
        return obj_high

    def individual_sales(self, employee_id):
        """
        gives the object related to an employee id
        """
        for person in self.sales_people:
            if employee_id == person.get_id():
                return person
        return None
