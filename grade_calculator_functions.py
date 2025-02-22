def get_student_score() -> float:
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
    
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
