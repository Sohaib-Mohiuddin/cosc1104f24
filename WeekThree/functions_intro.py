# Introduction to Functions

# Import Statements
import utils.functions_return

# Create a basic hello world function
def hello_world():
    # Code Block specific to function hello_world()
    print('Hello', 'World!')
    
# Create a parameterized hello world function
def hello_world1(name:str = 'Some_Student', age:int = 0):
    print(f'Hello { name }! Your current age is { age }.')

# Main Method that will be run
if __name__ == "__main__":
    # Call the function
    hello_world1('Sohaib', 21)

    # Call function from another file
    print(f'The student registration status from another class is { utils.functions_return.register_student(313) }')