import sys
from pathlib import Path
from model.wallet_account import WalletAccount
from utils.enums import Currency, AccountType

def test_wallet_account_initialization():
    account = WalletAccount(1, "My Wallet", Currency.USD)

    assert account.id == 1
    assert account.name == "My Wallet"
    assert account.accountType == AccountType.WALLET
    assert account.currency == Currency.USD


def test_wallet_account_str_representation():
    account = WalletAccount(2, "Travel Wallet", Currency.EUR)

    result = str(account)

    # Check simple string pieces, like your base example
    assert "WalletAccount" in result
    assert "id=2" in result
    assert "Travel Wallet" in result
    assert "Wallet" in result        # accountType.value
    assert "EUR" in result           # currency.value

# Run with:
# pytest -vv