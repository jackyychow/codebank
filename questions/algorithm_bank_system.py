# Question: Implement a bank supporting transfer, deposit, and withdrawal operations.
#

from typing import List
import unittest

class Bank:

    def __init__(self, balance: List[int]):
        self.numOfAccounts=len(balance)
        self.account=balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1>self.numOfAccounts or account2>self.numOfAccounts:
            return False
        if self.account[account1-1]<money:
            return False
        self.account[account1-1]-=money
        self.account[account2-1]+=money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if account>self.numOfAccounts:
            return False
        self.account[account-1]+=money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account>self.numOfAccounts:
            return False
        if self.account[account-1]<money:
            return False
        self.account[account-1]-=money
        return True
    
    def print(self):
        print(self.account)

class Test(unittest.TestCase):
    def test_account_number_not_found(self):
        bank=Bank([])
        self.assertEqual(False, bank.deposit(1,5))

if __name__=="__main__":
    unittest.main()
    # bank=Bank([100])
    # print(bank.deposit(1,5))
    # print(bank.print())