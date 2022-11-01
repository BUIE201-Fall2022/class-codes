import sys
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

class Movie:
    def __init__(self, Name, IMDBScore, Year, Month, Day) -> None:
        self.Name = Name
        self.IMDBScore = IMDBScore
        self.ReleaseDate = Date(Year, Month, Day)
        self.Viewers = []
    
    def print(self):
        print ("Movie: " + self.Name + " has IMDB score of " + str(self.IMDBScore))
        print ("Release date") 
        self.ReleaseDate.print()
        if len(self.Viewers) > 0:
            print("List of viewers: ")
            for viewer in self.Viewers:
                viewer.print() 
    
    def add_viewer(self, viewer):
        self.Viewers.append(viewer)
class Viewer:
    def __init__(self, Name) -> None:
        self.Name = Name
    
    def print(self):
        print(self.Name)

top_gun = Movie("Top Gun: Maverick", 8.4, 2022, 7, 1)
top_gun.print()
amsterdam = Movie("Amsterdam", 6.2, 2022, 8, 15)
amsterdam.print()

caner = Viewer("caner")
tinaz = Viewer("tinaz")

top_gun.add_viewer(caner)
amsterdam.add_viewer(caner)

amsterdam.add_viewer(tinaz)

top_gun.print()
amsterdam.print()