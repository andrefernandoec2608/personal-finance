from utils.enums import AccountType, Currency
from utils.util_message_label import show_accounts_menu, label_choose_option, label_choose_invalid
from application import Application
from manager.account_manager import AccountManager
from .common import ask_yes_no, ask_input_int, ask_input_str

account_actions = {
    "1": lambda manager, accounts: create_account_flow(manager, accounts),
    "2": lambda manager, accounts: modify_account_flow(manager, accounts),
    "3": lambda manager, accounts: delete_account_flow(manager, accounts),
    "4": lambda manager, accounts: list_all_account_flow(manager, accounts),
    "5": lambda manager, accounts: list_account_by_id_flow(manager, accounts),
}

def run_account_menu(application: Application) -> None:
    while True:
        show_accounts_menu()
        choice = input(label_choose_option).strip()

        if choice == "6":
            # Back to main menu
            break

        action = account_actions.get(choice)
        if action:
            """
            try:
                action(application.account_manager, application.state.accounts)
            except Exception as e:
                print(f"Error Account Manager: {e}")
            """
            action(application.account_manager, application.state.accounts)
        else:
            print(label_choose_invalid)

def create_account_flow(manager: AccountManager, accounts: list) -> None:
    print("\n=== Create Account ===")
    print("\nLet's create a new account.")
    print("Fill in the details. Type 'exit' at any moment to cancel.\n")

    # --- Account Type ---
    account_type = ask_type_account()

    # --- Currency ---
    currency_type = ask_currency()

    # --- Account Name ---
    name = ask_input_str("Account name")
    if name == "exit":
        print("Operation cancelled.")
        return
    # --- Account ID ---
    raw_id = ask_input_int("Account ID (integer): ")
    if raw_id == "exit":
        print("Operation cancelled.")
        return
    account_id = int(raw_id)
    # --- Confirmation ---
    print("\nPlease confirm the following details:")
    print(f"  ID: {account_id}")
    print(f"  Name: {name}")
    print(f"  Type: {account_type}")
    print(f"  Currency: {currency_type}")

    if not ask_yes_no("Do you want to create this account?"):
        print("Operation cancelled.")
        return

    manager.create_account(account_id,name,account_type,currency_type)    
    print("Operation successfully.")
    print("=========================\n")

def modify_account_flow(manager: AccountManager, accounts: list) -> None:
    print("\n=== Modify Account (Name Only) ===")
    print("\nLet's modify an account.")
    print("Fill in the details. Type 'exit' at any moment to cancel.\n")

    # 1) Ask for the account ID
    raw_id = ask_input_int("Enter account ID to modify")
    if raw_id == "exit":
            print("No changes made. Operation cancelled.")
            return
    account_id = int(raw_id)

    # 2) Ask for the new name
    new_name = input("\nNew name (or type 'exit' to cancel): ").strip()
    if not new_name or new_name.lower() == "exit":
        print("No changes made. Operation cancelled.")
        return
    
    manager.modify_account(account_id, new_name)
    print("Account name updated successfully.\n")
    print("=========================\n")

def delete_account_flow(manager: AccountManager, accounts: list) -> None:
    print("\n=== Delete Account ===")
    print("\nLet's delete an account.")
    print("Fill in the details. Type 'exit' at any moment to cancel.\n")

     # 1) Ask for the account ID
    raw_id = ask_input_int("Enter account ID to delete")
    if raw_id == "exit":
            print("No changes made. Operation cancelled.")
            return
    account_id = int(raw_id)
    manager.delete_account(account_id)
    print("Account deleted successfully.\n")
    print("=========================\n")

def list_all_account_flow(manager: AccountManager, accounts: list) -> None:
    print("\n=== List All Accounts ===")
    manager.list_all_accounts()
    print("=========================\n")

def list_account_by_id_flow(manager: AccountManager, accounts: list) -> None:
    print("\n=== Search Account by ID ===")
    print("\nLet's search an account.")
    print("Fill in the details. Type 'exit' at any moment to cancel.\n")

    # 1) Ask for the account ID
    raw_id = ask_input_int("Enter account ID to search")
    if raw_id == "exit":
            print("Operation cancelled.")
            return
    account_id = int(raw_id)
    manager.list_account_by_id(account_id)
    print("=========================\n")

def ask_type_account() -> str:
    print("Choose Account type:")
    while True:
        answer = input("Input an option: B for BankAccount or S for SavingsAccount: or W for WalletAccount ").strip().lower()
        if answer.lower() in ("b"):
            return AccountType.BANK.value
        if answer.lower() in ("s"):
            return AccountType.SAVINGS.value
        if answer.lower() in ("w"):
            return AccountType.WALLET.value

        print("Invalid option.")

def ask_currency() -> str:
    print("Choose Currency type:")
    while True:
        answer = input("Input an option: U for USD or E for EUR: ").strip().lower()
        if answer.lower() in ("u"):
            return Currency.USD.value
        if answer.lower() in ("e"):
            return Currency.EUR.value
       
        print("Invalid option.")