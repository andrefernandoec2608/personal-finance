from typing import List, Set, Optional
from model.account import Account
from model.bank_account import BankAccount
from model.savings_account import SavingsAccount
from model.wallet_account import WalletAccount
from exceptions.finance_manager_exception import (
    DuplicateIDException,
    NotFoundIDException,
    FinanceManagerException,
)
from utils.enums import AccountType, Currency
from pathlib import Path
from utils.util import load_storage_to_cvs, name_account_file

storage_dir = Path("./storage")

class AccountManager:
    def __init__(self, accounts: Set[Account]) -> None:
        self._accounts: Set[Account] = accounts

    def create_account(
        self,
        account_id: int,
        name: str,
        account_type: str,
        currency: str,
    ) -> None:
        if Account(account_id, "") in self._accounts:
            raise DuplicateIDException(account_id)
        
        if account_type == AccountType.BANK.value:
            account = BankAccount(account_id, name, Currency(currency))
        elif account_type == AccountType.SAVINGS.value:
            account = SavingsAccount(account_id, name, Currency(currency))
        elif account_type == AccountType.WALLET.value:
            account = WalletAccount(account_id, name, Currency(currency))
        else:
            raise FinanceManagerException(
                "Unsupported account type. Use 'CashAccount' or 'BankAccount'."
            )
        self._accounts.add(account)
        self._save_accounts()

    def modify_account(self, account_id: int, name: str) -> None:
        account = self._find_account_by_id(account_id)
        if account is None:
            raise NotFoundIDException(account_id)

        account.name = name
        self._save_accounts()

    def delete_account(self, account_id: int) -> None:
        account = self._find_account_by_id(account_id)
        if account is None:
            raise NotFoundIDException(account_id)
        
        self._accounts.remove(account)
        self._save_accounts()

    def list_all_accounts(self) -> None:
        if not self._accounts:
            print("There are no accounts registered at the moment.")
            return

        for acc in self._accounts:
            print(acc)

    def list_account_by_id(self, account_id: int) -> None:
        account = self._find_account_by_id(account_id)
        if account is None:
            raise NotFoundIDException(account_id)

        print(account)

    def _save_accounts(self):
        account_list = self._export_accounts_to_csv()
        load_storage_to_cvs(name_account_file, account_list)
    
    def _export_accounts_to_csv(self) -> list[list[str]]:
        exported: list[list[str]] = []
        for account in self._accounts:
            exported.append(account.transform_to_csv())

        return exported        

    def import_accounts_fron_csv(self, records: list[list[str]]) -> None:
        self._accounts.clear()

        for row in records:
            if len(row) != 4:
                raise ValueError(f"CSV row must have 4 values, got: {row}")

            account_id_str, name, account_type, currency = row
            account_id = int(account_id_str)

            self.create_account(account_id, name, account_type, currency,)

    def _find_account_by_id(self, account_id: int) -> Optional[Account]:
        for acc in self._accounts:
            if acc.id == account_id:
                return acc
        return None