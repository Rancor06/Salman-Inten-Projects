from bank_utils import format_currency, is_valid_amount, build_log_line, check_pin

LOG_FILE = "transactions.log"
CORRECT_PIN = "1234"
MAX_PIN_ATTEMPTS = 3

MENU_TEXT = (
    "\n===== WELCOME TO SIM ATM =====\n"
    "1. Check Balance   2. Deposit\n"
    "3. Withdraw        4. View Transaction History\n"
    "5. Exit"
)

def authenticate():
    """Prompt for PIN up to MAX_PIN_ATTEMPTS times. Returns True if successful."""
    for attempt in range(MAX_PIN_ATTEMPTS):
        pin = input("Enter your 4-digit PIN: ")
        if check_pin(pin, CORRECT_PIN):
            print("PIN accepted.\n")
            return True
        remaining = MAX_PIN_ATTEMPTS - attempt - 1
        if remaining > 0:
            print(f"Incorrect PIN. {remaining} attempt(s) remaining.\n")
    print("Too many failed attempts. Card locked.\n")
    return False

def show_menu():
    print(MENU_TEXT)

def log_transaction(txn_type, amount, balance_after):
    line = build_log_line(txn_type, amount, balance_after)
    with open(LOG_FILE, "a") as f:
        f.write(line)

def check_balance(balance):
    print(f"Balance: {format_currency(balance)}")

def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    if not is_valid_amount(amount):
        print("Deposit must be a positive amount.")
        return balance
    balance += amount
    log_transaction("DEPOSIT", amount, balance)
    print(f"Deposit successful! New balance: {format_currency(balance)}")
    return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if not is_valid_amount(amount) or amount > balance:
        print("Invalid withdrawal amount.")
        return balance
    balance -= amount
    log_transaction("WITHDRAW", amount, balance)
    print(f"Withdrawal successful! New balance: {format_currency(balance)}")
    return balance

def view_history():
    print("\n--- Transaction History ---")
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
        if not lines:
            print("No transactions yet.")
        else:
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No transactions yet.")

def run_atm():
    if not authenticate():
        return

    balance = 5000
    transaction_count = 0

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            new_balance = deposit(balance)
            if new_balance != balance:
                transaction_count += 1
            balance = new_balance
        elif choice == "3":
            new_balance = withdraw(balance)
            if new_balance != balance:
                transaction_count += 1
            balance = new_balance
        elif choice == "4":
            view_history()
        elif choice == "5":
            print(f"Total transactions this session: {transaction_count}")
            print("Thank you for using SIM ATM.")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    run_atm()