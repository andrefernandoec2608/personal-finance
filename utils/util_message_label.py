def show_main_menu() -> None:
    print("\n" * 5)
    print("=== PERSONAL FINANCE MENU ====")
    print("1. Manage Accounts")
    print("2. Manage Transactions")
    print("3. Manage Budget")
    print("4. Exit")

def show_accounts_menu() -> None:
    print("\n" * 5)
    print("=== MANAGE ACCOUNTS ===")
    print("1. Create account")
    print("2. Modify account")
    print("3. Delete account")
    print("4. List all accounts")
    print("5. List account by ID")
    print("6. Back to main menu")

def show_transactions_menu() -> None:
    print("\n" * 5)
    print("=== MANAGE TRANSACTIONS ===")
    print("1. Create transaction")
    print("2. Modify transaction")
    print("3. Delete transaction")
    print("4. List all transaction")
    print("5. List transaction by ID")
    print("6. Back to main menu")

def show_budgets_menu() -> None:
    print("\n" * 5)
    print("=== MANAGE BUDGETS ===")
    print("1. Create budget")
    print("2. Modify budget")
    print("3. Delete budget")
    print("4. List all budget")
    print("5. List budget by ID")
    print("6. Back to main menu")

label_exit_warning_message = (
    "\nYou are about to exit the system.\n"
    "Make sure you have saved your data to avoid losing it."
)

label_exit_confirmation_message = "Are you sure you want to exit?"

label_choose_option = "Choose an option: "
label_choose_invalid = "Invalid option, please try again."