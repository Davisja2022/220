class SalesPerson:
    employee_id = 0
    name = ""
    sales = [0.0]

    def __init__(self, employee_id,name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        sales = self.sales
        sales.append(sale)

    def total_sales(self):
        total = 0
        for num in self.sales:
            total += float(num)
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if sum(self.sales) >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        val = other.total_sales()
        if val == self.total_sales():
            return 0
        elif val > self.total_sales():
            return -1
        else:
            return 1

    def __str__(self):
        return "{}-{}: {}".format(self.get_id(),self.get_name(),self.total_sales())