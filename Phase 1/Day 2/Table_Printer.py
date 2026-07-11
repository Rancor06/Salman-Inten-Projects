n=0
while (n==0):
    num = int(input("Enter a number:"))
    for i in range (1,11):
        print (f"{num} x {i} = {num*i}")
    x = input("Continue?\n")
    x= x.lower()
    if x == "no":
        n=1