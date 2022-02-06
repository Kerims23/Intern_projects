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
        #the def write_acc_file should work with this
        write_acc_file(acc)
        
        
        
    def write_acc_file(account):
        #get the file
        file = pathlib.Path("accounts.data")
        if file.exists():
            #take the file, open it and load info
            infile = open("accounts.data", "rb")
            oldlist = pickle.load(infile)
            oldlist.append(account)
            infile.close()
            os.remove("accounts.data")

    #this is to display all accounts and info
    def display_all():
        file = pathlib.Path("accounts.data")
        #this is to read the file 
        if file.exists():
            infile = open("accounts.data", "rb")
           #this is the imported command
            my_list = pickle.load(infile)
            #making a for list to items in my_list
            for item in my_list:
                #prints out the items and account info etc
                print(item.acc_num, ' ', item.name, ' '. item.type, ' ',item.deposit)
            #must close file once im finished with file
            infile.close()
        #if it does not fall into my if then it will go to my else statement 
        else:
            #this print statement helps me know if the records are not being displayed or if something is wrong
            print("No records to display")

        
        def display_sp(num):
            file = path.lib.Path("accounts.data")
            if file.exists():
                infile = open("accounts.data", 'rb')
                my_list

