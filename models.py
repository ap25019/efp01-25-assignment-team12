#models.py

# The file Creates the Classes that represent the data of the application.


import datetime as Date


# 1  
class Work:    #Represents a Movie
    def __init__(self, work_id:int, title: str, release_date: Date, storyline: str,work_type: list, avr_rating: float):
        self.work_id = work_id
        self.title = title
        self.release_dates = release_date
        self.storyline = storyline
        self.work_type = work_type
        self.avr_rating = avr_rating

        self.cast = [] # List of actors Many actors can be in a movie
        self.directors = None #one director can be in a movie
        self.reviews = [] # List of reviews Many reviews can be in a movie


#Making a string more beautiful for the user to read when we print a Work object
    def __str__(self) -> str: 
        return f"{self.work_id},{self.title},{self.release_dates},{self.avr_rating},{self.work_type},{self.storyline}"
    


 # 2
class Person:   #Represents a Person (Actor, Director)
    def __init__(self, person_id:int, full_name: str, birth_date: Date, birth_place: str, website: str, bio: str, filmography: list):
        self.person_id = person_id
        self.full_name = full_name
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.website = website
        self.bio = bio
        self.filmography = filmography

    def __str__(self) -> str: # String representation of Person
        return f"{self.person_id},{self.full_name},{self.birth_date},{self.birth_place},{self.website},{self.bio},{self.filmography}"
    



 # 3
class Review: #Represents Review of a User!!
    def __init__(self, review_username: str, rating: int, review_text: str, review_date: Date):
        self.review_username = review_username
        self.rating = rating
        self.review_text = review_text
        self.review_date = review_date

        self.user = None #one user can write one review for a movie


    def __str__(self):
        return f"{self.review_username},{self.rating},{self.review_text},{self.review_date}"


 # 4
class User: #Represents a User
    def __init__(self, username: str, password: str, email: str, favorite_list: list):
        self.username = username
        self.password = password
        self.email = email
        self.favorite_list = favorite_list

    def __str__(self) -> str:
        return f"{self.username},{self.password},{self.email},{self.favorite_list}"
    


 # 5
class Series(Work): #Represents a TV Series, inherits from Work class
    def __init__(self, work_id:int, title: str, release_date: Date, storyline: str, work_type: list, 
                 avg_rating: float, last_air_date: Date, season_count: int, episodes_count: int):
        
        super().__init__(work_id, title, release_date, storyline, work_type, avg_rating)
        
       
        self.last_air_date = last_air_date
        self.season_count = season_count
        self.episodes_count = episodes_count

    def __str__(self) -> str:
        return f"{super().__str__()},{self.last_air_date},{self.season_count},{self.episodes_count}"





        
        