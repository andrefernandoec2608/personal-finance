from typing import Set, Optional

from model.budget import Budget
from utils.enums import Category
from exceptions.finance_manager_exception import (
    DuplicateIDException,
    NotFoundIDException,
)

class BudgetManager:
    def __init__(self, budgets: Set[Budget]) -> None:
        self._budgets: Set[Budget] = budgets

    def create_budget(
        self,
        budget_id: int,
        month: str,
        category: Category,
        limit_amount: float,
    ) -> None:
        
        budget = Budget(budget_id, month, category, limit_amount)
        if budget in self._budgets:
            raise DuplicateIDException(budget_id)

        self._budgets.add(budget)

    def modify_budget(
        self,
        budget_id: int,
        limit_amount: float,
    ) -> None:
        budget = self._find_budget_by_id(budget_id)
        if budget is None:
            raise NotFoundIDException(budget_id)

        budget.limit_amount = limit_amount

    def delete_budget(self, budget_id: int) -> None:
        budget = self._find_budget_by_id(budget_id)
        if budget is None:
            raise NotFoundIDException(budget_id)

        self._budgets.remove(budget)

    def list_all_budgets(self) -> None:
        if not self._budgets:
            print("There are no budgets registered at the moment.")
            return

        print("\nList of all budgets:")
        for budget in self._budgets:
            print(budget)

    def print_budget_by_id(self, budget_id: int) -> None:
        budget = self._find_budget_by_id(budget_id)
        if budget is None:
            raise NotFoundIDException(budget_id)

        print(budget)

    def _find_budget_by_id(self, budget_id: int) -> Optional[Budget]:
        for budget in self._budgets:
            if budget.id == budget_id:
                return budget
        return None