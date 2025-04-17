from abc import ABC, abstractmethod

class GradedActivity:
    def __init__(self, score=0.0):
        self.score = score

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"Score: {self.score}, Grade: {self.get_grade()}"


class Essay(GradedActivity):
    def __init__(self, grammar_points, spelling_points, length_points, content_points):
        super().__init__()
        self.grammar_points = grammar_points
        self.spelling_points = spelling_points
        self.length_points = length_points
        self.content_points = content_points
        total_points = grammar_points + spelling_points + length_points + content_points
        self.set_score(total_points)

    def __str__(self):
        return f"Essay - {super().__str__()}"


class PassFailExam(GradedActivity):
    def __init__(self, total_questions, questions_missed, passing_score=70):
        super().__init__()
        self.total_questions = total_questions
        self.questions_missed = questions_missed
        self.passing_score = passing_score
        score_calculated = 100 - ((questions_missed / total_questions) * 100)
        self.set_score(score_calculated)

    def __str__(self):
        text = f"Pass/Fail Exam - {super().__str__()}"
        if self.get_score() >= self.passing_score:
            text += " (Passed)"
        else:
            text += " (Failed)"
        return text


class FinalExam(GradedActivity):
    def __init__(self, total_questions_in_exam, number_of_questions_missed):
        super().__init__()
        self.total_questions = total_questions_in_exam
        self.missed_questions = number_of_questions_missed
        final_score = 100 - ((number_of_questions_missed / total_questions_in_exam) * 100)
        self.set_score(final_score)

    def __str__(self):
        return f"Final Exam - {super().__str__()}"


class Analyzable(ABC):
    @abstractmethod
    def get_average(self):
        pass

    @abstractmethod
    def get_highest(self):
        pass

    @abstractmethod
    def get_lowest(self):
        pass


class CourseGrades(Analyzable):
    def __init__(self):
        self.all_grades = [None] * 4

    def set_lab(self, lab_grade_object):
        self.all_grades[0] = lab_grade_object

    def set_pass_fail_exam(self, pass_fail_exam_object):
        self.all_grades[1] = pass_fail_exam_object

    def set_essay(self, essay_grade_object):
        self.all_grades[2] = essay_grade_object

    def set_final_exam(self, final_exam_object):
        self.all_grades[3] = final_exam_object

    def __str__(self):
        names = ['Lab Work', 'Pass or Fail Exam', 'Essay Work', 'Final Exam']
        final_text = ""
        for i in range(len(self.all_grades)):
            final_text += f"{names[i]}: {self.all_grades[i]}\n"
        return final_text.strip()

    def get_average(self):
        total = 0
        for grade in self.all_grades:
            total += grade.get_score()
        return total / len(self.all_grades)

    def get_highest(self):
        return max(self.all_grades, key=lambda grade: grade.get_score())

    def get_lowest(self):
        return min(self.all_grades, key=lambda grade: grade.get_score())


if __name__ == "__main__":
    lab_assignment = GradedActivity()
    lab_assignment.set_score(90)

    exam1 = PassFailExam(10, 3)
    my_essay = Essay(27, 18, 19, 28)
    final_exam_grade = FinalExam(50, 4)

    my_course = CourseGrades()
    my_course.set_lab(lab_assignment)
    my_course.set_pass_fail_exam(exam1)
    my_course.set_essay(my_essay)
    my_course.set_final_exam(final_exam_grade)

    print("=== Student Report Card ===")
    print(my_course)
    print("\nAverage Score:", round(my_course.get_average(), 2))
    print("Best Score:", my_course.get_highest())
    print("Lowest Score:", my_course.get_lowest())



