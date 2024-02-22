class Student:
    def __init__(self,name,num_tests):
        self.name = name
        self.scores =[0]* num_tests
    def getName(self):
        return self.name
    def getScore(self,position):
        return self.scores[position - 1]
    
    def set_score(self, position, score):
        self.scores[position - 1] = score
    def get_highest_score(self):
        return max(self.scores)
    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"Name: {self.name}\nTest Scores: {', '.join(map(str, self.scores))}"
student1 = Student("Alice", 3)
print(student1)
student1.set_score(1, 85)
student1.set_score(2, 90)
student1.set_score(3, 95)
print("Name:", student1.getName())
print("Test score at position 2:", student1.getScore(2))
print("Highest test score:", student1.get_highest_score())
print("Average test score:", student1.get_average_score())
print(help(student1))
