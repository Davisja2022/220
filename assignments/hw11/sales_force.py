from sales_person import SalesPerson

class SalesForce:
    sales_people = []

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, "r") as infile:
            lines = infile.readlines()
            for line in lines:
                self.sales_people.append(line)

    def quota_report(self, quota):
        list_of_persons= []
        for line in self.sales_people:
            person = []
            sum_of_vals = 0.0
            attrs = line.split(",")
            person.append(attrs[0])
            person.append(attrs[1])

            vals = attrs[2].lstrip().rstrip("\n").split(" ")
            for val in vals:
                sum_of_vals += float(val)
                person.append(float(val))
            if sum_of_vals >= quota:
                person.append(True)
            else:
                person.append(False)

            list_of_persons.append(person)
        return list_of_persons

    def top_seller(self):
        list_of_persons = []
        new_list = []
        for line in self.sales_people:
            person = []
            sum_of_vals = 0.0
            attrs = line.split(",")
            person.append(attrs[0])
            person.append(attrs[1])

            vals = attrs[2].lstrip().rstrip("\n").split(" ")
            for val in vals:
                sum_of_vals += float(val)
                person.append(float(val))
            list_of_persons.append(person)

        new_list.append(list_of_persons[0])
        for persons in list_of_persons[1:]:
            if sum(persons[2:]) > sum(new_list[0][2:]):
                new_list[0] = persons
            elif sum(persons[2:]) == sum(new_list[0][2:]):
                new_list.append(persons)
        return new_list

    def individual_sales(self, employee_id):
        list_of_persons = []
        for line in self.sales_people:
            person = []
            sum_of_vals = 0.0
            attrs = line.split(",")
            person.append(attrs[0])
            person.append(attrs[1])

            vals = attrs[2].lstrip().rstrip("\n").split(" ")
            for val in vals:
                sum_of_vals += float(val)
                person.append(float(val))
            list_of_persons.append(person)

        for persons in list_of_persons:
            if employee_id == int(persons[0]):
                obj = SalesPerson(int(persons[0]), persons[1])
                for attr in persons[2:]:
                    obj.enter_sale(attr)
                return obj
        return None

    def get_sale_frequencies(self):
        dict = {}
        list_of_persons = []
        for line in self.sales_people:
            person = []
            sum_of_vals = 0.0
            attrs = line.split(",")
            person.append(attrs[0])
            person.append(attrs[1])

            vals = attrs[2].lstrip().rstrip("\n").split(" ")
            for val in vals:
                sum_of_vals += float(val)
                person.append(float(val))
            list_of_persons.append(person)

        for persons in list_of_persons:
            for values in persons[2:]:
                if values not in dict.keys():
                    dict.update({values:1})
                else:
                    x = dict.get(values)
                    x += 1
                    dict[values] = x
        return dict