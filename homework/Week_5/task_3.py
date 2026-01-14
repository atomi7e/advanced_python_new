class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def introduce(self):
        print(f"Hello, I am a person. My name is {self._name}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hello, I am a student {self._name}. My ID: {self.student_id}.")

person = Person("Oleg", 40)
student = Student("Artem", 20, "SE-2409")

people = [person, student]

print("--- Polymorphism ---")
for p in people:
    p.introduce()

print("\n--- Encapsulation ---")
print(f"Access to protected attribute (not recommended, but possible): {person._name}")