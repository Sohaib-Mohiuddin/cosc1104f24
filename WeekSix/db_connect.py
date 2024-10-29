from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://mongo:27017')
db = client['school']
students_collection = db['students']

# 2. Retrieve and print all students
print("All Students:")
for student in students_collection.find():
    print(student)

# 3. Update the grade of one student
students_collection.update_one({"name": "Bob"}, {"$set": {"grade": "B+"}})

# 4. Retrieve and print the updated student record
print("\nUpdated Record for Bob:")
print(students_collection.find_one({"name": "Bob"}))

# 5. Delete one student
# students_collection.delete_one({"name": "Alice"})

# 6. Retrieve and print all records after deletion
print("\nAll Students After Deletion:")
for student in students_collection.find():
    print(student)

# Close the connection
client.close()
