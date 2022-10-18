class Date:
    def __init__(self) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
    
    def print(self):
        print("The date is: {}/{}/{}".format(self.Day, self.Month, self.Year))

today = Date()
today.Year = 2022
today.Month = 10
today.Day = 18
print(today)
today.print()

tomorrow = Date()
tomorrow.Year = 2022
tomorrow.Month = 10
tomorrow.Day = 19
print(tomorrow)
tomorrow.print()



