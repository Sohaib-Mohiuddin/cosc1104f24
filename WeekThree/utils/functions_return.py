student_registration_status = False # Boolean variable

# Create a function that takes 3 parameters and registers a student. If the information passed is satisfied, return True, else return False. 
def register_student(banner_id:int = 0, name:str = 'Default', age:int = 0):
    registration_status = False
    
    if (banner_id > 0):
        registration_status = True
    
    return registration_status

student_registration_status = register_student()