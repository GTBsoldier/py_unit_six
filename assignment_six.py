import random

def get_birthdays():
    """Generate a list of 23 random numbers representing birthdays."""
    return [random.randint(1, 365) for _ in range(23)]

def is_duplicates(birthdays):
    """
    Check if there are two people with the same birthday in the given list.

    birthdays (list): List of integers representing birthdays.

    Returns:
    True if there are duplicates, False otherwise.
    """
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return True
    return False

def main():
    """Run the Birthday Paradox simulation."""
    duplicate_count = 0

    try:
        simulation_count = int(input("How many times would you like to run the Birthday simulation? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for _ in range(simulation_count):
        birthdays = get_birthdays()
        if is_duplicates(birthdays):
            duplicate_count += 1

    success_percentage = (duplicate_count / simulation_count) * 100
    print("Out of", simulation_count, "simulations, two people shared a birthday in", duplicate_count, "cases.")
    print("This occurred", success_percentage, "% of the time.")


main()
