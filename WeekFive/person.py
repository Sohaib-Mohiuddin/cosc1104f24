class Person:
    def __init__(self, first_name, last_name, age, gender, address, phone_number, email, occupation, nationality, marital_status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.occupation = occupation
        self.nationality = nationality
        self.marital_status = marital_status

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, lives at {self.address}, " \
               f"phone: {self.phone_number}, email: {self.email}, works as {self.occupation}, " \
               f"nationality: {self.nationality}, marital status: {self.marital_status}"
    
    def get_last_name(self):
        return f" The Last Name of { self.first_name } is : { self.last_name }"

if __name__ == '__main__':
    person = Person(
        first_name="John",
        last_name="Doe",
        age=30,
        gender="Male",
        address="123 Main St, Anytown, USA",
        phone_number="555-1234",
        email="john.doe@example.com",
        occupation="Software Engineer",
        nationality="American",
        marital_status="Single"
    )
    
    person2 = Person(
        first_name="Sohaib",
        last_name="Mohiuddin",
        age=30,
        gender="Male",
        address="123 Main St, Anytown, USA",
        phone_number="555-1234",
        email="sohaib.mohiuddin@durhamcollege.ca",
        occupation="Software Engineer",
        nationality="American",
        marital_status="Single"
    )
    
    print(person.get_last_name())