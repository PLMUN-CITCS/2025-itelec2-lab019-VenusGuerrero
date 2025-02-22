def get_student_score():
    score = float(input("Enter your score: "))
    return score

def calculate_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'


final_score = get_student_score()
final_grade = calculate_grade(final_score)
print(f"Your Grade is: {final_grade}")



