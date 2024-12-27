from src.web_bcv import obtener_tasa
from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError, WithdrawalWeekDayRestrictionError

class BankAccount:
    
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta Creada")
    
    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8 am to 5pm.")
        
        if now.weekday in (5,6):
            raise WithdrawalWeekDayRestrictionError("Withdrawals are only allowed from Monday to Friday")
        
        if amount >0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Checket balance: {self.balance}")
        return self.balance

    def transfer(self, amount):
        if self.balance < amount:
            self._log_transaction(f"Saldo insuficiente para hacer la transferencia, balance: {self.balance}")
            raise Exception("Saldo insuficiente")
        self.balance -= amount
        return self.balance
    
    def change_moneda(self, url):
        tasa = obtener_tasa(url)
        
        balance_dolar = self.balance / tasa
        print(balance_dolar)
        self._log_transaction(f"Se hizo la convercion de bolivares a dolares, balance ($): {balance_dolar}")