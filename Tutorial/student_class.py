class Student:

    def __init__(self, name, num_scores):
        self.name = name
        self.test_scores = [0] * num_scores

    def getName(self):
        return self.name

    def getScore(self, position):
        if position < 1 or position > len(self.test_scores):
            raise IndexError(f"Position {position} is out of range. Valid range: 1 to {len(self.test_scores)}.")
        return self.test_scores[position - 1]

    def setScore(self, position, value):
        if position < 1 or position > len(self.test_scores):
            raise IndexError(f"Position {position} is out of range. Valid range: 1 to {len(self.test_scores)}.")
        if value < 0 or value > 100:
            raise ValueError(f"Score value {value} is invalid. Scores must be between 0 and 100.")
        self.test_scores[position - 1] = value

    def getHighestScore(self):
        return max(self.test_scores)

    def getAverageScore(self):
        return round(sum(self.test_scores) / len(self.test_scores), 2)

    def __str__(self):
        scores_display = ", ".join(str(score) for score in self.test_scores)
        return (
            f"Student Name  : {self.name}\n"
            f"Test Scores   : [{scores_display}]\n"
            f"Highest Score : {self.getHighestScore()}\n"
            f"Average Score : {self.getAverageScore()}"
        )


if __name__ == "__main__":
    print("=" * 45)
    print("       Student Class Implementation")
    print("=" * 45)

    student = Student("Alice Johnson", 5)

    student.setScore(1, 88)
    student.setScore(2, 95)
    student.setScore(3, 76)
    student.setScore(4, 91)
    student.setScore(5, 83)

    print(student)
    print("-" * 45)

    print(f"Name          : {student.getName()}")
    print(f"Score at pos 2: {student.getScore(2)}")
    print(f"Highest Score : {student.getHighestScore()}")
    print(f"Average Score : {student.getAverageScore()}")
    print("=" * 45)

    print("\nUpdating Score at position 3 to 99...\n")
    student.setScore(3, 99)
    print(student)
    print("=" * 45)

    print("\nError Handling Demo:")
    try:
        student.getScore(10)
    except IndexError as e:
        print(f"  IndexError  → {e}")

    try:
        student.setScore(1, 150)
    except ValueError as e:
        print(f"  ValueError  → {e}")

    print("=" * 45)
