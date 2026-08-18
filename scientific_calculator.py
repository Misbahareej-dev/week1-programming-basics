import math

history = []


# ---------- HISTORY ----------

def add_history(value):
    history.append(value)


def show_history():
    print("\n========== HISTORY ==========")
    if len(history) == 0:
        print("No history available")
    else:
        for item in history:
            print(item)


# ---------- INPUT VALIDATION HELPERS ----------

def get_float(prompt):
    """Safely gets a float input from user to prevent program crashing."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_int(prompt):
    """Safely gets an integer input from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def get_number(prompt="Enter first number: ", previous_answer=None):
    """Handles previous answer reuse and safe float input."""
    if previous_answer is not None:
        use = input("Use previous answer? (yes/no): ").strip().lower()
        if use == "yes":
            return previous_answer
    return get_float(prompt)


# ---------- BASIC OPERATIONS ----------

def addition(previous_answer=None):
    print("\n----- Addition -----")
    num1 = get_number("Enter first number: ", previous_answer)
    num2 = get_float("Enter second number: ")

    answer = num1 + num2
    print("Answer =", answer)
    add_history(f"{num1} + {num2} = {answer}")
    return answer


def subtraction(previous_answer=None):
    print("\n----- Subtraction -----")
    num1 = get_number("Enter first number: ", previous_answer)
    num2 = get_float("Enter second number: ")

    answer = num1 - num2
    print("Answer =", answer)
    add_history(f"{num1} - {num2} = {answer}")
    return answer


def multiplication(previous_answer=None):
    print("\n----- Multiplication -----")
    num1 = get_number("Enter first number: ", previous_answer)
    num2 = get_float("Enter second number: ")

    answer = num1 * num2
    print("Answer =", answer)
    add_history(f"{num1} * {num2} = {answer}")
    return answer


def division(previous_answer=None):
    print("\n----- Division -----")
    num1 = get_number("Enter first number: ", previous_answer)
    num2 = get_float("Enter second number: ")

    if num2 == 0:
        print("Error! Division by zero is not allowed.")
        return None

    answer = num1 / num2
    print("Answer =", answer)
    add_history(f"{num1} / {num2} = {answer}")
    return answer


# ---------- ADVANCED FEATURES ----------

def square(previous_answer=None):
    print("\n----- Square -----")
    num = get_number("Enter number: ", previous_answer)

    answer = num ** 2
    print("Answer =", answer)
    add_history(f"Square of {num} = {answer}")
    return answer


def square_root(previous_answer=None):
    print("\n----- Square Root -----")
    num = get_number("Enter number: ", previous_answer)

    if num < 0:
        print("Error! Cannot calculate square root of a negative number.")
        return None

    answer = math.sqrt(num)
    print("Answer =", answer)
    add_history(f"Square root of {num} = {answer}")
    return answer


def power(previous_answer=None):
    print("\n----- Power -----")
    num = get_number("Enter base number: ", previous_answer)
    p = get_float("Enter exponent (power): ")

    try:
        answer = math.pow(num, p)
        print("Answer =", answer)
        add_history(f"{num}^{p} = {answer}")
        return answer
    except ValueError:
        print("Error! Invalid power operation.")
        return None


def factorial():
    print("\n----- Factorial -----")
    num = get_int("Enter positive integer: ")

    if num < 0:
        print("Error! Factorial is not defined for negative numbers.")
        return None

    answer = math.factorial(num)
    print("Answer =", answer)
    add_history(f"{num}! = {answer}")
    return answer


def trigonometry():
    print("\n----- Trigonometry -----")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")

    choice = input("Enter choice: ").strip()
    angle = get_float("Enter angle (in degrees): ")

    if choice == "1":
        answer = math.sin(math.radians(angle))
    elif choice == "2":
        answer = math.cos(math.radians(angle))
    elif choice == "3":
        # Tan angle of 90, 270, etc. is undefined
        if angle % 180 == 90:
            print("Error! Tangent of 90°/270° is undefined.")
            return None
        answer = math.tan(math.radians(angle))
    else:
        print("Invalid Choice")
        return None

    print("Answer =", answer)
    add_history(f"Trigonometry choice ({choice}) for angle {angle}° = {answer}")
    return answer


def logarithm(previous_answer=None):
    print("\n----- Logarithm -----")
    print("1. Log Base 10")
    print("2. Natural Log (ln)")

    choice = input("Enter choice: ").strip()
    num = get_number("Enter positive number: ", previous_answer)

    if num <= 0:
        print("Error! Logarithm is only defined for positive numbers.")
        return None

    if choice == "1":
        answer = math.log10(num)
    elif choice == "2":
        answer = math.log(num)
    else:
        print("Invalid Choice")
        return None

    print("Answer =", answer)
    add_history(f"Log choice ({choice}) of {num} = {answer}")
    return answer


# ---------- MENUS ----------

def basic_menu(previous_answer=None):
    while True:
        print("\n========== BASIC OPERATIONS ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            previous_answer = addition(previous_answer)
        elif choice == "2":
            previous_answer = subtraction(previous_answer)
        elif choice == "3":
            previous_answer = multiplication(previous_answer)
        elif choice == "4":
            previous_answer = division(previous_answer)
        elif choice == "5":
            break
        else:
            print("Invalid Choice")

        if previous_answer is not None:
            again = input("\nContinue calculation with result? (yes/no): ").strip().lower()
            if again != "yes":
                previous_answer = None

    return previous_answer


def advanced_menu(previous_answer=None):
    while True:
        print("\n========== ADVANCED FEATURES ==========")
        print("1. Square")
        print("2. Square Root")
        print("3. Power")
        print("4. Factorial")
        print("5. Trigonometry")
        print("6. Logarithm")
        print("7. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            previous_answer = square(previous_answer)
        elif choice == "2":
            previous_answer = square_root(previous_answer)
        elif choice == "3":
            previous_answer = power(previous_answer)
        elif choice == "4":
            factorial()
        elif choice == "5":
            trigonometry()
        elif choice == "6":
            previous_answer = logarithm(previous_answer)
        elif choice == "7":
            break
        else:
            print("Invalid Choice")

        if previous_answer is not None:
            again = input("\nContinue calculation with result? (yes/no): ").strip().lower()
            if again != "yes":
                previous_answer = None

    return previous_answer


# ---------- MAIN PROGRAM ----------

def main():
    print("Loading Scientific Calculator...")
    print("Please wait...\n")

    print("=" * 50)
    print("    WELCOME TO SCIENTIFIC CALCULATOR")
    print("    Developed By Misbah Areej")
    print("    Software Development Internship")
    print("=" * 50)

    input("\nPress Enter to Continue...")

    previous_answer = None

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Basic Operations")
        print("2. Advanced Features")
        print("3. History")
        print("4. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            previous_answer = basic_menu(previous_answer)
        elif choice == "2":
            previous_answer = advanced_menu(previous_answer)
        elif choice == "3":
            show_history()
        elif choice == "4":
            print("\nThank you for using Scientific Calculator!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()