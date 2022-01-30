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