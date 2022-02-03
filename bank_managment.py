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
        self.name = input("Modify account name: ")
        self.type = input("Modify type of Account: ")
        self.deposit = int(input("Modify Balance: "))

    def show_account(self):
        print(f"Account Number: {self.acc_num}")
        print(f"Account Name: {self.name}")
        print(f"Type of Account {self.type}")
        print(f"Balance: {self.deposit}")

    def report(self):
        print(f"{self.acc_num}, {self.name}, {self.type}, {self.deposit}")


#return statments 
    def get_acc_num(self):
        return self.acc_num

    def get_acc_name(self):
        return self.name
    
    def get_acc_type(self):
        return self.type

    def get_acc_deposit(self):
        return self.deposit


#intro screen, this is a filler for future flask maybe

    def intro():
        print("*****************************")
        print("*** Bank Management System ***")
        print("*****************************")

        input()
        

    

# write account
    def write_acc():
        #pulling the class account from before and making it a variable
        acc = Account()
        acc.create_account()
        #the def write_acc_file will work with this
        write_acc_file(acc)
        
        
        
    def write_acc_file(account):
        file = pathlib.Path("accounts.data")