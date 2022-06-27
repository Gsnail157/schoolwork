from linkedList import LinkedList
from employee import *


def menu():
    print('''
a. Add New Employee
b. Enter Employee Hours
c. Update Employee Hourly Rate
d. Display Payroll
e. Remove Employee from Payroll
f. Exit the program
    ''')


def main():
    print(" *** CS 172 Payroll Simulator ***")
    linkedlist = LinkedList()

    while True:
        # try:
        menu()
        option = input("Enter your choice:")
        if option == "a":
            name = input("Enter the new employee name:")
            rate = float(input("Enter their hourly rate:"))
            new_employee = Employee(name, rate)
            linkedlist.append(new_employee)
            print(f'Employee {new_employee.getEID()} added to payroll')

        elif option == "b":
            for item in range(len(linkedlist)):
                hours = float(
                    input(f"Enter hours worked for employee {linkedlist[item].getEID()}:"))
                linkedlist[item].setHours(hours)

        elif option == "c":
            iD = int(input("Enter employee ID:"))
            if iD > Employee.count:
                print("Employee doesn't exist.")
            for item in range(0, len(linkedlist)):
                if linkedlist[item].getEID() == iD:
                    new_wage = float(
                        input(f"Enter new wage for employee:"))
                    linkedlist[item].setRate(new_wage)

        elif option == "d":
            print("*** Payroll***")
            print(linkedlist)

        elif option == "e":
            iD = int(input("Enter employee ID:"))
            if iD > Employee.count:
                print("Employee doesn't exist.")
            for item in range(0, len(linkedlist)):
                if linkedlist[item].getEID() == iD:
                    linkedlist.remove(linkedlist[item])
                    print(f"Employee removed.")

        elif option == "f":
            print("Goodbye.")
            return

        #     else:
        #         raise Exception

        # except Exception as e:
        #     print("Invalid entry")


if __name__ == '__main__':
    main()
