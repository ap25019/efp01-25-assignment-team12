#models.py

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

        self.cast = [] 
        self.directors = [] 


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

    def __str__(self) -> str: 
        return f"{self.person_id},{self.full_name},{self.birth_date},{self.birth_place},{self.website},{self.bio},{self.filmography}"


 # 3
class Series(Work): #Represents a TV Series, inherits from Work class
    def __init__(self, work_id:int, title: str, release_date: Date, storyline: str, work_type: list, 
                 avg_rating: float, last_air_date: Date, season_count: int, episodes_count: int):
        
        super().__init__(work_id, title, release_date, storyline, work_type, avg_rating)
        
       
        self.last_air_date = last_air_date
        self.season_count = season_count
        self.episodes_count = episodes_count

    def __str__(self) -> str:
        return f"{super().__str__()},{self.last_air_date},{self.season_count},{self.episodes_count}"





        
        