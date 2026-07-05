balance = 5000

def show_balance_wrong():
    balance = 0
    print(f"Inside function: {balance}")

show_balance_wrong()
print(f"Outside function (unchanged): {balance}")

def deposit_wrong(amount):
    balance = balance + amount
    return balance

def deposit_correct(current_balance, amount):
    return current_balance + amount

balance = deposit_correct(balance, 100)
print(f"Correct pattern: {balance}")