class Date:
    def __init__(self, Year, Month, Day) -> None:
        is_valid = self.set_date(Year, Month, Day)
        if is_valid == False:
            self.Year = 1970
            self.Month = 1
            self.Day = 1
    
    def set_date(self, Year, Month, Day):
        # add validation
        if Month >= 1 and Month <= 12 and Day >= 1 and Day <= 31:
            self.Year = Year
            self.Month = Month
            self.Day = Day
            return True
        else:
            print("Invalid date! {}/{}/{}".format(Year, Month, Day))
            return False
    
    def print(self):
        print("The date is: {}/{}/{}".format(self.Day, self.Month, self.Year))

def f(date):
    print("f - start")
    date.print()
    print("f - end")

today = Date(2022, 10, 20)
print("Today type:", type(today))
print("Today id:", id(today))

tomorrow = Date(2022, 10, 21)
print("Tomorrow type:", type(tomorrow))
print("Tomorrow id:", id(tomorrow))

print("Before f")
f(today)
today.print()
print("After f")
