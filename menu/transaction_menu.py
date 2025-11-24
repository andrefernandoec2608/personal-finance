from utils.util_message_label import show_transactions_menu, label_choose_option, label_choose_invalid
from application import Application
from manager.transaction_manager import TransactionManager

transaction_actions = {
    "1": lambda manager, transactions: create_transaction_flow(manager, transactions),
    "2": lambda manager, transactions: modify_transaction_flow(manager, transactions),
    "3": lambda manager, transactions: delete_transaction_flow(manager, transactions),
    "4": lambda manager, transactions: list_all_transaction_flow(manager, transactions),
    "5": lambda manager, transactions: list_transaction_by_id_flow(manager, transactions),
}

def run_transaction_menu(application: Application) -> None:
    while True:
        show_transactions_menu()
        choice = input(label_choose_option).strip()

        if choice == "6":
            # Back to main menu
            break

        action = transaction_actions.get(choice)
        if action:
            action(application.transaction_manager, application.state.transaction)
        else:
            print(label_choose_invalid)

def create_transaction_flow(manager: TransactionManager, transactions: list) -> None:
    print("create_transaction_flow")
    print("TO DO: Not implemented yet.")

def modify_transaction_flow(manager: TransactionManager, transactions: list) -> None:
    print("modify_transaction_flow")
    print("TO DO: Not implemented yet.")

def delete_transaction_flow(manager: TransactionManager, transactions: list) -> None:
    print("delete_transaction_flow")
    print("TO DO: Not implemented yet.")

def list_all_transaction_flow(manager: TransactionManager, transactions: list) -> None:
    print("list_all_transaction_flow")
    print("TO DO: Not implemented yet.")

def list_transaction_by_id_flow(manager: TransactionManager, transactions: list) -> None:
    print("list_transaction_by_id_flow")
    print("TO DO: Not implemented yet.")