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

today = Date(2022, 10, 18)
#today.set_date(2022, 10, 18)
# today.Year = 2022
# today.Month = 10
# today.Day = 18
print(today)
today.print()

tomorrow = Date(2022, 10, 19)
#tomorrow.set_date(2022, 10, 19)
# tomorrow.Year = 2022
# tomorrow.Month = 10
# tomorrow.Day = 19
print(tomorrow)
tomorrow.print()

wrongday = Date(2022, 25, -4)
# wrongday.set_date(2022, 25, -4)
# wrongday.Year = 2022
# wrongday.Month = 25
# wrongday.Day = -4
print(tomorrow)
wrongday.print()

