def valid_pin(pin):
    
    # Validate that the PIN is a 4-digit numeric value.
   
    return pin.isdigit() and len(pin) == 4

def atm_login(correct_pin):
   
    # Simulate ATM login with a 4-digit PIN.
   
    attempts = 5  # Number of allowed attempts

    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")

        if valid_pin(entered_pin):
            if entered_pin == correct_pin:
                print("Login successful!")
                return True
            else:
                attempts -= 1
                print(f"Invalid PIN. You have {attempts} attempts left.")
        else:
            print("Invalid input. PIN must be a 4-digit number.")

    print("Your account is locked due to too many failed attempts.")
    exit()
    return False


# Set the correct PIN (in a real system, this would be securely stored)
correct_pin = "1234"



            
         # Initialize account details
def atm_simulation():   
        balance = 5000  # Initial balance
        pin = 12345  # Default PIN
        transaction_history = []  # List to store transaction history

            # function for checking balance
        def check_balance():
            transaction_history.append(f"your corrent balance: ₹{balance}")
            print(" ################################################################## ")
            
            print(f"Your current balance is: ₹{balance}")
            
            print(" ################################################################## ")

            # Function to deposit money into the account
        def deposit(amount):
            nonlocal balance
            balance += amount
            transaction_history.append(f"Deposited: ₹{amount}")    # for save in history
            
            print(" ################################################################# ")
            
            print(f"${amount} deposited successfully. Your new balance is: ${balance}")
            
            print(" ################################################################# ")

            # Function to withdraw money from the account.
        def withdraw(amount):
            nonlocal balance
            if amount > balance:
                print(" ############################################################ ")
                
                print("Insufficient balance!")
                
                print(" ############################################################ ")
            else:
                balance -= amount
                transaction_history.append(f"Withdrew: ₹{amount}")      # for save in history
                print(f"${amount} withdrawn successfully. Available balance is: ${balance}")

            # Function to change the PIN
        def change_pin():
            nonlocal pin
            old_pin = int(input("Enter your current PIN: "))
            
            if old_pin == pin:
                new_pin = int(input("Enter your new PIN: "))
                confirm_pin = int(input("Confirm your new PIN: "))
                
                if new_pin == confirm_pin:
                    pin = new_pin
                    print(" ######################################################### ")
                    
                    print("PIN changed successfully.")
                    
                    print(" ######################################################### ")
                    
                    transaction_history.append(f"atm pin changed: {new_pin}") # for save in history
                else:
                    print("New PINs do not match. Try again.")
            else:
                print("Incorrect current PIN.")

            # Function to view transaction history.
        def view_transaction_history():
            
            if transaction_history:
                print("Transaction & all activity History:")
                for transaction in transaction_history:
                    print(f"- {transaction}")
            else:
                print("No transactions yet.")

        while True:
            # Display menu
            print(""" 
#######################################################################################
                
     ##   Welcome to the ATM Simulator  ##
            
    1. Balance enquiry.
    2. Deposit Money.
    3. Withdraw Money.
    4. Change PIN.
    5. View Transaction & activity History.
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
atm_login(correct_pin)

# Run the ATM simulation program
atm_simulation()
