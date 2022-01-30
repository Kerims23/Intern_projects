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
        self.name = int(input("Enter account number here: "))
        self.deposit = int(input("Enter account number here: "))
        self.type = int(input("Enter account number here: "))