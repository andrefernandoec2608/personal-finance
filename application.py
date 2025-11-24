from pathlib import Path
from app_state import AppState
from manager.account_manager import AccountManager
from manager.budget_manager import BudgetManager
from manager.transaction_manager import TransactionManager
from utils.util import load_storage_from_cvs, name_account_file

class Application:

    def __init__(self) -> None:
        self.state = AppState()
        self.account_manager = AccountManager(self.state.accounts)
        self.transaction_manager = TransactionManager(self.state.transaction)
        self.budget_manager = BudgetManager(self.state.budget)

    def run(self) -> None:
        self._load_accounts_from_cvs()

    def _load_accounts_from_cvs(self):
        list_accounts = load_storage_from_cvs(name_account_file)
        self.account_manager.import_accounts_fron_csv(list_accounts)