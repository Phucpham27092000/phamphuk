

class Employee:
    count = {}

    def __init__(self, role):
        self.role = role
        self.id = self.generate_id()

    def generate_id(self):
        if self.role not in Employee.count:
            Employee.count[self.role] = 1
        else:
            Employee.count[self.role] += 1

        id_number = Employee.count[self.role]
        id_string = self.role + str(id_number)
        return id_string

while True:
    chucvu = Employee(input("Nhap chuc vu: "))
    print(chucvu.id)
