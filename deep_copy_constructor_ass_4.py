import copy

class Student:
    def __init__(self, name, cources=[]):
        self.name = name
        self.cources = cources

    def clone(self, name):
        deep_copy =  copy.deepcopy(self)
        deep_copy.name = name
        return deep_copy

    def add_cource(self, cource):
        self.cources.append(cource)

    def desplay(self):
        return f"{self.name} has taken {self.cources}"

student1 = Student("John", ["Math", "Science"])
strudent2 = student1.clone("Doe")
strudent2.add_cource("History")

print(student1.desplay())
print(strudent2.desplay())
