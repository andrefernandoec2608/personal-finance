from utils.util_message_label import show_main_menu, label_exit_warning_message, label_choose_option, label_choose_invalid
from application import Application
from .common import ask_yes_no

from .account_menu import run_account_menu
from .transaction_menu import run_transaction_menu
from .budget_menu import run_budget_menu

# Diccionario de acciones del menú principal
main_actions = {
    "1": lambda application: run_account_menu(application),
    "2": lambda application: run_transaction_menu(application),
    "3": lambda application: run_budget_menu(application),
}

def run_main_menu(application: Application) -> None:
    while True:
        show_main_menu()
        choice = input(label_choose_option).strip()

        if choice == "4":
            if ask_yes_no(label_exit_warning_message):
                print("Goodbye!")
                break
            else:
                print("Exit cancelled.")
                continue

        action = main_actions.get(choice)
        
        if action:
            action(application)
        else:
            print(label_choose_invalid)