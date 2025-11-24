import pytest

from manager.account_manager import AccountManager
from exceptions.finance_manager_exception import DuplicateIDException
from exceptions.finance_manager_exception import NotFoundIDException
from utils.enums import AccountType, Currency

def test_account_manager_create_and_find_integration(tmp_path, monkeypatch):
    manager = AccountManager(set())
    manager.create_account(
        1,
        "My Wallet",
        AccountType.WALLET.value,
        Currency.USD.value,
    )

    assert manager._find_account_by_id(1) is not None


def test_account_manager_duplicate_integration():
    manager = AccountManager(set())
    manager.create_account(
        1,
        "Wallet",
        AccountType.WALLET.value,
        Currency.USD.value,
    )

    with pytest.raises(DuplicateIDException):
        manager.create_account(
            1,
            "Another Wallet",
            AccountType.WALLET.value,
            Currency.USD.value,
        )


def test_account_manager_modify_delete_integration():
    manager = AccountManager(set())
    manager.create_account(
        10,
        "TestName",
        AccountType.WALLET.value,
        Currency.EUR.value,
    )

    # ----- MODIFY -----
    manager.modify_account(10, "UpdatedName")
    acc = manager._find_account_by_id(10)
    assert acc.name == "UpdatedName"

    # ----- DELETE -----
    manager.delete_account(10)
    assert manager._find_account_by_id(10) is None

    # ----- DELETE NON-EXISTENT -----
    with pytest.raises(NotFoundIDException):
        manager.delete_account(999)