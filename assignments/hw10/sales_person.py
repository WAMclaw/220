"""
William McClain
sales_person.py
Problem: Create a class for a sales person
Affirmation: I affirm that this is all my own work.
"""


class SalesPerson:
    """
    class for an individual sales employee
    """

    def __init__(self, employee_id, name):
        """
        initializes the class SalesPerson
        """
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """
        returns the id number of the employee
        """
        return self.employee_id

    def get_name(self):
        """
        returns the name of the employee
        """
        return self.name

    def set_name(self, name):
        """
        resets the name of an employee
        """
        self.name = name

    def enter_sale(self, sale):
        """
        enters a single sale of an employee
        """
        self.sales.append(sale)

    def total_sales(self):
        """
        returns the total sales of an employee
        """
        return float(sum(self.sales))

    def get_sales(self):
        """
        returns the list of all sales of an employee
        """
        return self.sales

    def met_quota(self, quota):
        """
        checks to see if an employees sales meets an entered quota and return True of False
        """
        return float(sum(self.sales)) >= quota

    def compare_to(self, other):
        """
        compares two employees sales and returns -1 if they sold less 0 if equal sales and 1 if they sold higher
        """
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        return 0

    def personnel_info(self):
        """
        returns a string of the employee <ID-Name: sales>
        """
        return str(self.employee_id)+"-"+str(self.name)+": "+str(self.total_sales())