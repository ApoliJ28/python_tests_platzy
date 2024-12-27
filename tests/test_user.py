import unittest
from faker import Faker
from src.user import User
import os
from src.bank_account import BankAccount

class UserTest(unittest.TestCase):
    
    def setUp(self):
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())
    
    def test_user_creation(self):
        name = self.faker.name()
        email = self.faker.email()
        user = User(name=name, email=email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
    
    def test_user_with_multiple_accounts(self):
        
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension=".txt")
            )
            self.user.add_account(account=bank_account)

        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value, expected_value)
    
    def tearDown(self):
        for account in self.user.accounts:
            os.remove(account.log_file)