#importing classes
import pickle
import os
import pathlib

#defining the first class
class Account:
    acc_num = 0
    name = ""
    deposit = 0 
    type = ""

    def create_account(self):
        self.acc_num = int(input("Enter account number here: "))
        self.name = int(input("Enter account name here: "))
        self.deposit = int(input("Enter amount deposited here: "))
        self.type = int(input("Enter account type here: "))
        print("Account Created")

    def deposit_amount(self, amount):
        self.deposit += amount

    def withdraw_amount(self):
        self.deposit -= amount 

