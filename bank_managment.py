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

    def modify_account(self):
        print(f"Account Number: {self.acc_num}")
        self.name = input("Modify account holder name: ")
        self.type = input("Modify type of Account: ")
        self.deposit = int(input("Modify Balance: "))

    def show_account(self):
        print(f"Account Number: {self.acc_num}")
        print(f"Account Holder Name: {self.name}")
        print(f"Type of Account {self.type}")
        print(f"Balance: {self.deposit}")

    def report(self):
        print(f"{self.acc_num}, {self.name}, {self.type}, {self.deposit}")


#return statments 
def get_acc_num(self):
    return self.acc_num
