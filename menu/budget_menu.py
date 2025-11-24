from utils.util_message_label import show_budgets_menu, label_choose_option, label_choose_invalid
from application import Application
from manager.budget_manager import BudgetManager

budget_actions = {
    "1": lambda manager, budgets: create_budget_flow(manager, budgets),
    "2": lambda manager, budgets: modify_budget_flow(manager, budgets),
    "3": lambda manager, budgets: delete_budget_flow(manager, budgets),
    "4": lambda manager, budgets: list_all_budget_flow(manager, budgets),
    "5": lambda manager, budgets: list_budget_by_id_flow(manager, budgets),
}

def run_budget_menu(application: Application) -> None:
    while True:
        show_budgets_menu()
        choice = input(label_choose_option).strip()

        if choice == "6":
            # Back to main menu
            break

        action = budget_actions.get(choice)
        if action:
            action(application.budget_manager, application.state.budget)
        else:
            print(label_choose_invalid)

def create_budget_flow(manager: BudgetManager, budgets: list) -> None:
    print("create_budget_flow")
    print("TO DO: Not implemented yet.")

def modify_budget_flow(manager: BudgetManager, budgets: list) -> None:
    print("modify_budget_flow")
    print("TO DO: Not implemented yet.")

def delete_budget_flow(manager: BudgetManager, budgets: list) -> None:
    print("delete_budget_flow")
    print("TO DO: Not implemented yet.")

def list_all_budget_flow(manager: BudgetManager, budgets: list) -> None:
    print("list_all_budget_flow")
    print("TO DO: Not implemented yet.")

def list_budget_by_id_flow(manager: BudgetManager, budgets: list) -> None:
    print("list_budget_by_id_flow")
    print("TO DO: Not implemented yet.")