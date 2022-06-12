class Employee:
    count = 0

    def __init__(self, name, rate=0.0, eid=None):
        Employee.count += 1
        self.name = name
        self.rate = float(rate)
        self.eid = Employee.count
        self.num_of_hours_worked = float(0)

    def __str__(self):
        return f'Employee Name: {self.getName()}\nEmployee ID: {self.getEID()}\nHourly Rate: {self.getRate()}\nHours Worked: {self.getHours()}\nGross Pay: {self.getGrossPay()}\n'

    def __eq__(self, num):
        if self.getEID() == num:
            return True
        else:
            return False

    def getRate(self):
        return self.rate

    def getEID(self):
        return self.eid

    def getName(self):
        return self.name

    def getHours(self):
        return self.num_of_hours_worked

    def getGrossPay(self):
        return self.getRate() * self.getHours()

    def setRate(self, rate):
        self.rate = rate

    def setHours(self, hours):
        self.num_of_hours_worked = hours
