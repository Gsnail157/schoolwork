class Birthday:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __str__(self):
        return f'Day: {self.day}, Month: {self.month}, Year: {self.year}'

    def __hash__(self):
        return (self.day + self.month + self.year) % 12

    def __eq__(self, other):
        if self.day == self.other and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
