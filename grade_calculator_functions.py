def get_student_score() -> float:
    """
    Handles user input to obtain the student's score.
    Ensures valid numeric input within the range 0-100.
    
    Returns:
        float: The validated student score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                print("Valid score entered.")  # Confirmation message
                return score
            else:
                print("Error: Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score using standard grading criteria.
    
    Args:
        score (float): The student's score (0-100).
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main() -> None:
    """
    Main program flow.
    Calls get_student_score() to obtain input, calculates the grade,
    and displays the result to the user.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
