import datetime

class User:
    """
    A class for storing user information.

        name: stores the full name of the user
        first_name: stores the first name of the user
        last_name: stores the last name of the user
        dob: stores the date of birth of the user
    """
    def __init__(self, full_name, date_of_birth):
        self.name = full_name
        self.dob = date_of_birth

        # Extract first name and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """ Returns the user's age. """
        current_date = datetime.date.today()
        year = int(self.dob[0:4])
        month = int(self.dob[4:6])
        day = int(self.dob[6:8])
        dob_converted = datetime.date(year, month, day)
        age_in_days = (current_date - dob_converted).days
        
        return int(age_in_days / 365)

user = User("Albert Crosswodd", "19990101") # user_1 is an "Instance" of class User 
                # user_1 is an "object"


print(user.first_name)
print(user.last_name)
print(user.dob)
print("Age: ", user.age())
# help(user)
