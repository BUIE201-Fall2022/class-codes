class Date:
    def __init__(self) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1

today = Date()
today.Year = 2022
today.Month = 10
today.Day = 18
print(today)

tomorrow = Date()
tomorrow.Year = 2022
tomorrow.Month = 10
tomorrow.Day = 19
print(tomorrow)



