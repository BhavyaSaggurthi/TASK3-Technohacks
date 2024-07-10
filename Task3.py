class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} successfully. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Withdrew {amount} successfully. Current balance: {self.balance}"


if __name__ == "__main__":
    atm = ATM(1000)  # Set an initial balance

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Your balance is {atm.check_balance()}")

        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit(amount))

        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(atm.withdraw(amount))

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
