# A simple grade calculator for CS101
def calculate_average(grades):
    # BUG: This will crash if the list is empty (DivisionByZero)
    total = sum(grades)
    return total / len(grades)

def get_student_status(average):
    # LOGIC ERROR: What if the grade is exactly 70? 
    # CS Students love finding these edge cases.
    if average > 70:
        return "Passing"
    elif average < 70:
        return "Failing"

# SMULLY CODE: Hardcoded list instead of a database or file
students = {"Alice": [85, 90, 78], "Bob": [60, 55, 65], "Charlie": []}

for student, grades in students.items():
    avg = calculate_average(grades)
    status = get_student_status(avg)
    print(f"Student: {student}, Average: {avg}, Status: {status}")

# SECURITY/PRACTICE ISSUE: Using input() without sanitization
bonus_points = input("Enter bonus points to add: ")
final_score = 90 + bonus_points # This will crash because bonus_points is a string