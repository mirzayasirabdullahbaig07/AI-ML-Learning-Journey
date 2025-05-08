class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.main_menu()

    def main_menu(self):
        user_input = input("""
Welcome to the ATM System.
Please select an option:
1 - Set your PIN
2 - Make a Deposit
3 - Make a Withdrawal
4 - View Balance
5 - Exit
Enter your choice: """)
        if user_input == "1":
            self.set_pin()
        elif user_input == "2":
            self.add_funds()
        elif user_input == "3":
            self.take_cash()
        elif user_input == "4":
            self.view_balance()
        else:
            print("Thank you for using our ATM. Have a great day!")

    def set_pin(self):
        self.pin = input("Please enter a new PIN: ")
        print("Your PIN has been successfully created.")

    def add_funds(self):
        entered_pin = input("Enter your PIN to continue: ")
        if entered_pin == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"{amount} has been added to your account.")
        else:
            print("Incorrect PIN. Access denied.")

    def take_cash(self):
        entered_pin = input("Enter your PIN to continue: ")
        if entered_pin == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} completed successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN. Access denied.")

    def view_balance(self):
        entered_pin = input("Enter your PIN to check your balance: ")
        if entered_pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Incorrect PIN. Access denied.")

# Start the ATM session
atm = Atm()
