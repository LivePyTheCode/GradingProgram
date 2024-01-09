student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# score 91-100 - "Outstanding"
# score 81-90 - "Exceeds expectations"
# score 71-80 - "Acceptable"
# score 70 or lower - "Fail

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding!"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations!"
    elif score > 70:
        student_grades[student] = "Acceptable."
    else:
        student_grades[student] = "Fail."

print(student_grades)