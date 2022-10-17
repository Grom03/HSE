import pytest
from account import Account
from datetime import datetime

def test_add_money():
    account = Account()

    assert account.put_money(500) == 500


def test_take_money():
    account = Account()

    account.put_money(500)
    assert account.take_money(300) == (None, 200)
    assert account.take_money(300) == ("You don't have that sum", 200)

def test_correct_operations():
    account = Account()
    expected_operations = []
    account.put_money(500)
    expected_operations.append(
        {
            "Time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"), 
            "Amount": f"+{500}", 
            "Balance": 500
        }
    )
    account.take_money(300)
    expected_operations.append(
        {
            "Time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"), 
            "Amount": f"-{300}", 
            "Balance": 200
        }
    )

    account.take_money(300)
    assert account.get_operations() == expected_operations