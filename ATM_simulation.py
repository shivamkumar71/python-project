# this is fuction for user login 
def enter_pin():
        atm_pin = 12345
        use_pin = int(input("Enter your PIN for ATM: "))
        if use_pin== atm_pin:
            print("you have success full entered your ATM")
        else:
            print("invalid PIN, try again later")
            exit()   
            
         # Initialize account details
def atm_simulation():   
        balance = 5000  # Initial balance
        pin = 12345  # Default PIN
        transaction_history = []  # List to store transaction history

            # function for checking balance
        def check_balance():
            print(f"Your current balance is: ${balance}")

            # Function to deposit money into the account
        def deposit(amount):
            nonlocal balance
            balance += amount
            transaction_history.append(f"Deposited: ₹{amount}")
            print(f"${amount} deposited successfully. Your new balance is: ${balance}")

            # Function to withdraw money from the account.
        def withdraw(amount):
            nonlocal balance
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                transaction_history.append(f"Withdrew: ₹{amount}")
                print(f"${amount} withdrawn successfully. Your new balance is: ${balance}")

            # Function to change the PIN
        def change_pin():
            nonlocal pin
            old_pin = int(input("Enter your current PIN: "))
            if old_pin == pin:
                new_pin = int(input("Enter your new PIN: "))
                confirm_pin = int(input("Confirm your new PIN: "))
                
                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("New PINs do not match. Try again.")
            else:
                print("Incorrect current PIN.")

            # Function to view transaction history.
        def view_transaction_history():
            
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(f"- {transaction}")
            else:
                print("No transactions yet.")

        while True:
            # Display menu
            print(""" 
            ###################################################################################
                
                            ##   Welcome to the ATM Simulator  ##
            
                                   1. Check Balance.
                                   2. Deposit Money.
                                   3. Withdraw Money.
                                   4. Change PIN.
                                   5. View Transaction History.
                                   6. Exit.
            
            ######################################################################################
            """)

            # Get user choice
            choice = input("Enter your choice: ")

            if choice == "1":
                check_balance()
            elif choice == "2": # 2 choice for deposit money
                
                try:
                    amount = float(input("Enter amount to deposit: "))
                    if amount > 0:
                        deposit(amount)
                    else:
                        print("Enter a valid amount.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            elif choice == "3": # 3 choice for withdraw
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount > 0:
                        withdraw(amount)
                    else:
                        print("Enter a valid amount.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            elif choice == "4": # 4 choice for change pin
                change_pin()
                
                
            elif choice == "5":
                view_transaction_history() # for check transaction history
                
            elif choice == "6": # exit
                print("Thank you for using the ATM Simulator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
# run login function
enter_pin()

# Run the ATM simulation program
atm_simulation()
