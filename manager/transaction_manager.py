from typing import Set, Optional
from datetime import date

from model.transaction import Transaction
from utils.enums import Category
from exceptions.finance_manager_exception import (
    DuplicateIDException,
    NotFoundIDException,
)

class TransactionManager:
    def __init__(self, transactions: Set[Transaction]) -> None:
        self._transactions: Set[Transaction] = transactions

    def create_transaction(
        self,
        transaction_id: int,
        account_id: int,
        trx_date: date,
        amount: float,
        description: str,
        category: Category,
    ) -> None:
        transaction = Transaction(
            transaction_id,
            account_id,
            trx_date,
            amount,
            description,
            category,
        )

        if transaction in self._transactions:
            raise DuplicateIDException(transaction_id)

        self._transactions.add(transaction)

    def modify_transaction(
        self,
        transaction_id: int,
        description: str,
        category: Category,
    ) -> None:
        transaction = self._find_transaction_by_id(transaction_id)
        if transaction is None:
            raise NotFoundIDException(transaction_id)

        transaction.description = description
        transaction.category = category

    def delete_transaction(self, transaction_id: int) -> None:
        transaction = self._find_transaction_by_id(transaction_id)
        if transaction is None:
            raise NotFoundIDException(transaction_id)

        self._transactions.remove(transaction)

    def list_all_transactions(self) -> None:
        if not self._transactions:
            print("There are no transactions registered at the moment.")
            return

        print("\nList of all transactions:")
        for transaction in self._transactions:
            print(transaction)

    def print_transaction_by_id(self, transaction_id: int) -> None:
        transaction = self._find_transaction_by_id(transaction_id)
        if transaction is None:
            raise NotFoundIDException(transaction_id)

        print(transaction)

    def _find_transaction_by_id(
        self,
        transaction_id: int,
    ) -> Optional[Transaction]:
        for transaction in self._transactions:
            if transaction.id == transaction_id:
                return transaction
        return None