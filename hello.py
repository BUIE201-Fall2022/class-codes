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
    print("before set_date date id:", id(date))
    date.set_date(2022, 11, 15)
    print("after set_date date id:", id(date))
    date.print()
    print("f - end")

today = Date(2022, 10, 20)
print("Today type:", type(today))
print("Today id:", id(today))

tomorrow = Date(2022, 10, 21)
print("Tomorrow type:", type(tomorrow))
print("Tomorrow id:", id(tomorrow))

print("Before f")
print("today id:", id(today))
today.print()
f(today)
today.print()
print("today id:", id(today))
today.print()
print("After f")

def g(i):
    print("g - start")
    print("i id:", id(i), " value: ", i)
    i += 5
    print("i id:", id(i), " value: ", i)
    print("g - end")

my_int = 5
print("Before g")
print("my_int id:", id(my_int), " value: ", my_int)
g(my_int)
print("my_int id:", id(my_int), " value: ", my_int)
print("After g")

print(type(my_int))
print(id(my_int))