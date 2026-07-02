bal = 5000
print("===== Welcome TO THE SIM ATM =====")
n=0
while (n==0):
    i=0
    print("1. Check Your Balance \t2. Deposit")
    print("3. Withdraw           \t4. Exit")
    x=int(input("Choose an Option: "))
    if x == 1:
        print(f"Your current balance is: {bal}\n")
    elif x == 2:
        y=int(input("Enter amount to deposit:"))
        bal= bal+y
        print(f"Updated Balance: {bal}\n")
    elif x == 3:
        z=int(input("Enter amount to withdraw:"))
        bal=bal-z
        print(f"Updated Balance: {bal}\n")
    elif x == 4:
        print("Thank you for using SIM ATM\n")
        n=1
    else:
        print("Please enter a valid option\n")