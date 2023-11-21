# Subprograms Group Activity

## This simple bank system consists of several subprograms to breaking down this large problem into smaller modules

# For validating username and password; it takes name, password, and a dictionary as its arguments
def validator(name, passw, reg_users_and_password):
    if name in reg_users_and_password.keys():
        first_value = reg_users_and_password.get(name)
        get_pass = first_value[0]
        if passw == get_pass:
            return True
    return False

# For the program's withdrawal feature; it takes name, password, dictionary, balance and amount to withdraw as its arguments
def withdrawal(name, passw, reg_users_and_password, balance, amount_to_withdraw):
    withdrawal_fee = 15
    if validator(name, passw, reg_users_and_password):
        if balance < amount_to_withdraw:
            return "Not enough balance"
        else:
            amt = balance - amount_to_withdraw
            final_amt = amt - withdrawal_fee
            reg_users_and_password[name][1] = final_amt
            return final_amt
    return "Invalid request"

# For the program's deposit feature; it takes name, password, dictionary, balance and amount to deposit as its arguments
def deposit(name, passw, reg_users_and_password, balance, amount_to_deposit):
    if validator(name, passw, reg_users_and_password):
        new_balance = balance + amount_to_deposit
        reg_users_and_password[name][1] = new_balance
        return new_balance
    return "Invalid request"

# To process inputs given by a user
def chosen_action(action, name, passw, reg_users_and_password, balance):
    if action.lower() == "w":
        amount_to_withdraw = int(input("Enter the amount to withdraw: "))
        new_balance = withdrawal(name, passw, reg_users_and_password, balance, amount_to_withdraw)
        if new_balance == "Not enough balance":
            print(new_balance)
        else:
            print(f"Withdrawal successful! New balance: {new_balance}")
    elif action.lower() == "d":
        amount_to_deposit = int(input("Enter the amount to deposit: "))
        new_balance = deposit(name, passw, reg_users_and_password, balance, amount_to_deposit)
        if new_balance == "Invalid request":
            print(new_balance)
        else:
            print(f"Deposit successful! New balance: {new_balance}")
    else:
        print("Invalid action")

# Dictionary that stores username and passwords
reg_users_and_password = {
    "user_1": ["admin1234", 20000],
    "user_2": ["admin1234", 20000],
    "user_3": ["admin1234", 20000],
    "user_4": ["admin1234", 20000],
}

while True:
    name = input("\nEnter your name: ")
    passw = input("Enter the password: ")

    # If validator detects no issue
    if validator(name, passw, reg_users_and_password):
        user_info = reg_users_and_password.get(name)

        # Get only the balance
        balance = user_info[1]

        # Display balance
        print(f"Current Balance: {balance}")

        action = input("Do you want to withdraw or deposit? (w/d): ")

        # Invoke the chosen action subprogram to process user's choice
        chosen_action(action, name, passw, reg_users_and_password, balance)

    else:
        print("Invalid request")

    choice = input("Do you want to try again? (y/n): ")
    if choice.lower() == "n":
        print("Thanks for your time!")
        break
