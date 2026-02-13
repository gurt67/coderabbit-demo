# Student Grade Management System
# Created for CS101 Project 2

def calculate_average(grades):
    """Calculates the mean score from the provided list of grades."""
    total = sum(grades)
    return total / len(grades)

def get_student_status(average):
    """Determines if a student is passing based on their average score."""
    if average > 70:
        return "Passing"
    elif average < 70:
        return "Failing"

# Dictionary to store student names and their respective grade lists
student_data = {
    "Alice": [85, 90, 78],
    "Bob": [60, 55, 65],
    "Charlie": []  # Enrollment pending - no grades yet
}

# Process and display results for each student
for student, grades in student_data.items():
    avg = calculate_average(grades)
    status = get_student_status(avg)
    print(f"Student: {student} | Average: {avg} | Status: {status}")

# Add manual bonus points to final project grade
bonus_points = input("Enter project bonus points: ")
final_project_score = 90 + bonus_points
print(f"Final Adjusted Score: {final_project_score}")