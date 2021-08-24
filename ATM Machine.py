balance = 300000

print ("""
Welcome to TymeBank

Choose Transaction

1) BALANCE
2) WITHDRAW
3) DEPOSIT
4) EXIT

""")
while True:
    option = int(input("Enter Transaction: "))

#Here the user must enter an number in order for them choose their transaction
#After the user is finished with their transaction, they will be given a choice to
#choose another transaction or not
    if(option == 1):
        print("Your Balance is: R", balance)
        anothertrans = input("Do you want to make another transaction YES/NO: ")
        if(anothertrans == "YES" or anothertrans =="Yes" or anothertrans == "yes"):
            continue
        else:
            break
    elif(option == 2):
        withdraw = float(input("Enter amount to withdraw: "))
        if(balance > withdraw):
            total = balance - withdraw
            print("Success, your new balance is: ", total)
        else:
            print("insufficient balance")
        anothertrans = input("Do you want to make another transaction YES/NO: ")
        if (anothertrans == "YES" or anothertrans == "Yes" or anothertrans == "yes"):
            continue
        else:
            break

    elif(option == 3):
        deposit = float(input("Enter amount to deposit: "))
        total_balance = balance + deposit
        print("Success, total balance now is: ", total_balance)

        anothertrans = input("Do you want to make another transaction YES/NO: ")
        if (anothertrans == "YES" or anothertrans == "Yes" or anothertrans == "yes"):
            continue
        else:
            break
    elif(option == 4):
        print("Closing the program")
        exit()
    else:
        print("No selected transaction")

