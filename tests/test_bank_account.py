import unittest
import os
from src.bank_account import BankAccount
from unittest.mock import patch
from src.exceptions import WithdrawalTimeRestrictionError, WithdrawalWeekDayRestrictionError


class BankAccountTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
    
    def tearDown(self):
        if os.path.exists("transaction_log.txt"):
            os.remove(self.account.log_file)
    
    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())
    
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500
        self.assertEqual(new_balance, 1500, "El balance no es igual.")
    
    def test_withdraw(self):
        new_balance = self.account .withdraw(500)
        # assert new_balance == 500
        self.assertEqual(new_balance, 500, "El balance no es igual")
    
    def test_get_balance(self):
        self.assertEqual(self.account .get_balance(), 1000, "El balance no es igual")
        # assert self.account .get_balance() == 1000
    
    def test_transfer(self):
        new_balance = self.account.transfer(amount=200)
        assert new_balance == 800
    
    def test_transaction_log(self):
        self.account.deposit(500)
        # assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))
    
    def test_count_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
    
    def test_change_currency(self):
        url = "https://www.bcv.org.com/"
        
        with self.assertRaises(Exception):
            self.account.change_moneda(url=url)
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussnues_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_blaance = self.account.withdraw(100)
        self.assertEqual(
            new_blaance, 900
        )
    
    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussnies_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussnues_weekday(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        mock_datetime.now.return_value.weekday = 4
        new_blaance = self.account.withdraw(100)
        self.assertEqual(
            new_blaance, 900
        )
    
    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussnues_weekday(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        mock_datetime.now.return_value.weekday = 6
        with self.assertRaises(WithdrawalWeekDayRestrictionError):
            self.account.withdraw(100)
    
    def test_deposit_multiple_ammounts(self):
        
        tests_cases=[
            {"ammount": 100, "expected": 1100},
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500},
        ]
        
        for case in tests_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transaction.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])