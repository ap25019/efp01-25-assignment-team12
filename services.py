#service.py


from models import Work, Person, Review, User, Series
from datetime import date as Date


class MovieManager: #The class that manages attributes and methods
    def __init__(self):
        self.works: list[Work] = [] # List to store movies and series
        self.users: list[User] = [] # List to store users
        self.persons: list[Person] = [] # List to store actors and directors
        
        self._next_work_id = 1 # Internal counter for work IDs        
        self._next_user_id = 1 # Internal counter for user IDs
        self._next_person_id = 1 # Internal counter for person IDs


        self._seed_demo_data()

    def _seed_demo_data(self) -> None:
        """Creates 3-4 ready-made movies and series for testing."""
        self.add_work("Inception", Date(2010, 7, 16), "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.", ["Action", "Sci-Fi"], 8.8)
        self.add_work("The Matrix", Date(1999, 3, 31), "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", ["Action", "Sci-Fi"], 8.7)
        self.add_serie("Breaking Bad", Date(2008, 1, 20), "A high school chemistry teacher turned methamphetamine producer navigates the dangers of the drug trade while trying to secure his family's future.", ["Crime", "Drama"], 9.5, Date(2013, 9, 29), 5, 62)
        self.add_serie("Stranger Things", Date(2016, 7, 15), "When a young boy vanishes, a small town uncovers a mystery of government experiments, terrifying supernatural forces and an alias that affects the lives of those involved.", ["Drama", "Fantasy"], 8.7, Date(2025, 7, 15), 4, 34)


    # ------- works ---------

    def add_work(self, title: str, release_date: Date, storyline: str, work_type: list, avr_rating: float, ) -> Work:
        new_work = Work(self._next_work_id, title, release_date, storyline, work_type, avr_rating)
        self.works.append(new_work) # Add work to the list
        self._next_work_id += 1 # Increment the work ID counter
        return new_work
    

    def add_serie(self, title: str, release_date: Date, storyline: str, work_type: list, avr_rating: float, 
                   last_air_date: Date, season_count: int, episodes_count: int) -> Series:
        
        new_series = Series(self._next_work_id, title, release_date, storyline, work_type, avr_rating, last_air_date, season_count, episodes_count)
        self.works.append(new_series) # Add series to the list
        self._next_work_id +=1 # Increment the work ID counter
        return new_series
    
    