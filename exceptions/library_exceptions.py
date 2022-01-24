class NoTitleProvided(Exception):
    def __init__(self, message="Must define a title for the book"):
        self.message = message
        super().__init__(self.message)

class NoGenreProvided(Exception):
    def __init__(self, message="Must define a genre for the book"):
        self.message = message
        super().__init__(self.message)

class NoPagesProvided(Exception):
    def __init__(self, message="Must define a page number for the book"):
        self.message = message
        super().__init__(self.message)
    
class NoAuthorProvided(Exception):
    def __init__(self, message="Must define an author for the book"):
        self.message = message
        super().__init__(self.message)

class NoYearProvided(Exception):
    def __init__(self, message="Must define a year for the book"):
        self.message = message
        super().__init__(self.message)

class NoIsbnProvided(Exception):
    def __init__(self, message="Must define an isbn for the book"):
        self.message = message
        super().__init__(self.message)