import json


students_data = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 92]},
    {"name": "Bob", "age": 21, "grades": [78, 80, 70]},
    {"name": "Charlie", "age": 22, "grades": [95, 100, 98]}
]

with open("students.json", "w") as f:
    json.dump(students_data, f, indent=4)

print("File students.json created.")

with open("students.json", "r") as f:
    data = json.load(f)

updated_data = []

for student in data:
    grades = student["grades"]
    avg_grade = sum(grades) / len(grades)
    
    student_info = {
        "name": student["name"],
        "age": student["age"],
        "average_grade": round(avg_grade, 0)
    }
    updated_data.append(student_info)

with open("students_avg.json", "w") as f:
    json.dump(updated_data, f, indent=4)

print("Processing completed. Check the students_avg.json file")