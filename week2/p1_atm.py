def update_atm_amount_distribution(operation: str, amount_dict: dict, atm_amount_distribution: dict):
    for denomination, count in amount_dict.items():
        if operation == "add":
            atm_amount_distribution[denomination] += count
        elif operation == "withdraw":
            atm_amount_distribution[denomination] -= count


def check_add_amount(amount_dict: dict, atm_amount_distribution: dict) -> tuple:
    for denomination, count in amount_dict.items():
        if atm_amount_distribution[denomination] + count > 500:
            return False, f"Cannot add more than 500 notes of {denomination} denomination"
    return True, ""


def draw_cash(notes: dict, amount: int) -> tuple:
    notes_count: int = 0
    solution: dict = {}

    if amount > sum(note * count for note, count in notes.items()):
        return False, {}, "ATM does not have sufficient balance"

    if amount % 10 != 0 or amount < 100:
        return False, {}, "Amount should be a multiple of 10 and greater than or equal to 100"

    if amount > 10000:
        return False, {}, "Amount should be less than 10,000"

    for note in sorted(notes.keys(), reverse=True):
        if note <= amount:
            if notes[note] <= 0:
                continue

            num_notes = min(amount // note, notes[note])
            solution[note] = num_notes
            notes[note] -= num_notes
            notes_count += num_notes

            print(f"Attempting to withdraw {num_notes} notes of ₹{note}")

            if notes_count > 40:
                return False, {}, "Limitation Exceeds: Maximum number of notes, it can dispense is 40"

            amount -= num_notes * note

    print(f"Final dispensed notes: {solution}")
    print(f"Remaining amount to dispense: {amount}")

    if amount == 0:
        return True, solution, ""
    else:
        return False, {}, "Unable to dispense the exact amount"


def print_denomination(notes: dict):
    total: int = 0
    print("\nDenomination Summary:")
    print(f"{'Denomination':<12} {'Count':<6} {'Total':<10}")
    print("-" * 30)

    for entry in sorted(notes.keys(), reverse=True):
        print(f'{entry:<12} {notes[entry]:<6} {entry * notes[entry]:<10}')
        total += entry * notes[entry]

    print(f"\nTotal balance is: {total}\n")


def amount_input():
    while True:
        try:
            amount = int(input("Enter the amount to be withdrawn: "))
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            return amount
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid amount.")


def main():
    atm_amount_distribution = {
        500: 500,
        100: 500,
        50: 500,
        20: 500
    }

    while True:
        print("\nCurrent ATM Balance:")
        print_denomination(atm_amount_distribution)

        print("Select Operation:")
        print("1. Withdraw")
        print("2. Add")
        print("3. Denomination Summary")
        print("4. Exit")
        operation = input("Enter the operation number (1/2/3/4): ")

        if operation == "1":
            amount = amount_input()
            success, solution, message = draw_cash(
                atm_amount_distribution.copy(), amount)

            if success:
                print("\nSuccessfully withdrew the amount:")
                update_atm_amount_distribution(
                    "withdraw", solution, atm_amount_distribution)
                print_denomination(solution)
            else:
                print(f"Error: {message}")

        elif operation == "2":
            try:
                denominations = input(
                    "Enter denominations and counts to add (e.g., '500 2, 100 3'): ")
                amounts_to_add = {int(k): int(v) for k, v in (
                    item.split() for item in denominations.split(','))}
                valid, message = check_add_amount(
                    amounts_to_add, atm_amount_distribution)

                if valid:
                    update_atm_amount_distribution(
                        "add", amounts_to_add, atm_amount_distribution)
                    print("\nAmount successfully added.")
                else:
                    print(f"Error: {message}")

            except ValueError:
                print(
                    "Invalid input format. Please enter denominations and counts correctly.")

        elif operation == "3":
            print_denomination(atm_amount_distribution)

        elif operation == "4":
            print("Exiting...")
            break

        else:
            print("Invalid operation. Please try again.")


if __name__ == "__main__":
    main()
