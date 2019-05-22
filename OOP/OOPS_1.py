class Employee:
    def __init__(self, firstName, lastName, age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary

    def sum(self):
        if self.age > 28:
            print("You can take hooneymoon package")
        else:
            print("you cannot take honeymoon package")

    def empDetails(self):
        print("FIRST NAME: {}".format(self.firstName))
        print("LAST NAME: {}".format(self.lastName))
        print("AGE: {}".format(self.age))
        print("SALARY: {}".format(self.salary))


if __name__ == " __main__ ":
    employee = Employee("Ankit", "Kharel", 23, "100k")
    employee.empDetails()
    employee.sum()



