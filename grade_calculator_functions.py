def get_student_score() -> float:
    """
    Handles user input to obtain the student's score.
    Ensures the input is a valid numerical value.
    
    Returns:
        float: The student's score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.
    
    Args:
        score (float): The student's numerical score.
    
    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

def main():
    """Main function to execute the grade calculation process."""
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
