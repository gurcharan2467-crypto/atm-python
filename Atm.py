class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []

    def display_balance(self):
        return self.balance

    def deposit_money(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(("Deposit", amount, self.balance))
        return self.balance

    def withdraw_money(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(("Withdraw", amount, self.balance))
        return self.balance

    def statement(self):
        if not self.transactions:
            return "No transactions yet."
        lines = ["Transaction Statement:", f"{'Type':<10} {'Amount':>10}  {'Balance':>10}"]
        lines.append("-" * 35)
        for tx_type, amount, balance in self.transactions:
            lines.append(f"{tx_type:<10} ${amount:>8.2f}  ${balance:>8.2f}")
        return "\n".join(lines)


def main():
    atm = ATM(100)  # Initialize ATM with $100
    print("Welcome to the ATM!")
    print(f"Current balance: ${atm.display_balance():.2f}")
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Statement")
        print("4. Exit")
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            try:
                new_balance = atm.deposit_money(amount)
                print(f"Deposit successful! New balance: ${new_balance:.2f}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            try:
                new_balance = atm.withdraw_money(amount)
                print(f"Withdrawal successful! New balance: ${new_balance:.2f}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            print(atm.statement())

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()