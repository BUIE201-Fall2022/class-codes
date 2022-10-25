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
    
    def print(self):
        print ("Movie: " + self.Name + " has IMDB score of " + str(self.IMDBScore))
        # Violates encapsulation principle
        #print ("It was released on {}/{}/{}".format(self.ReleaseDate.Day, self.ReleaseDate.Month, self.ReleaseDate.Year))
        print ("Release date") 
        self.ReleaseDate.print()

movie = Movie("Top Gun: Maverick", 8.4, 2022, 7, 1)
movie.print()

print (type(movie))
print (id(movie))
print (sys.getrefcount(movie))

print (type(movie.ReleaseDate))
print (id(movie.ReleaseDate))
print (sys.getrefcount(movie.ReleaseDate))

new_movie = movie
print (type(new_movie))
print (id(new_movie))
print (sys.getrefcount(new_movie))

print (type(new_movie.ReleaseDate))
print (id(new_movie.ReleaseDate))
print (sys.getrefcount(new_movie.ReleaseDate))

movie = None
print (type(new_movie))
print (id(new_movie))
print (sys.getrefcount(new_movie))

print (type(new_movie.ReleaseDate))
print (id(new_movie.ReleaseDate))
print (sys.getrefcount(new_movie.ReleaseDate))


# movie2 = Movie("Amsterdam", 6.2, 2022, 8, 15)
# movie2.print()
# print (type(movie2))
# print (id(movie2))

# print (type(movie2.ReleaseDate))
# print (id(movie2.ReleaseDate))

# movie3 = movie2
# print (type(movie3))
# print (id(movie3))

# print (type(movie3.ReleaseDate))
# print (id(movie3.ReleaseDate))
