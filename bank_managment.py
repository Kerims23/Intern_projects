#importing classes
import pickle
import os
import pathlib


print("hi")
#import colorama 

#defining the first class
class Account:
    acc_num = 0
    name = ""
    deposit = 0 
    type_of_acct = ""  # rename this variable because type is reserved

    # look into creating a constructor __init__
    # this is a function that runs when the object is created/ instantiated

    def create_account(self):
        self.acc_num = int(input("Enter account number here: "))
        self.name = int(input("Enter account name here: "))
        self.deposit = int(input("Enter amount deposited here: "))
        self.type_of_acct = int(input("Enter account type here: "))
        print("Account Created")

    def deposit_amount(self, amount):
        self.deposit += amount

    def withdraw_amount(self):
        self.deposit -= amount 

    def modify_acc(self):
        print(f"Account Number: {self.acc_num}")
        self.name = input("Modify account name: ")
        self.type_of_acct = input("Modify type of Account: ")
        self.deposit = int(input("Modify Balance: "))

    # you can override __str__ function
    def show_account(self):
        print(f"Account Number: {self.acc_num}")
        print(f"Account Name: {self.name}")
        print(f"Type of Account: {self.type_of_acct}")
        print(f"Balance: {self.deposit}")

    def report(self):
        print(f"{self.acc_num}, {self.name}, {self.type_of_acct}, {self.deposit}")


#return statments 
    def get_acc_num(self):
        return self.acc_num

    def get_acc_name(self):
        return self.name
    
    def get_acc_type(self):
        return self.type_of_acct

    def get_acc_deposit(self):
        return self.deposit


#intro screen, this is a filler for future flask maybe
        

# write account
    def write_acc(self):
        #pulling the class account from before and making it a variable
        self.create_account()
        #the def write_acc_file should work with this
        write_acc_file(acc_num)
        
        
   #this is to create the file for acct     
    def write_acc_file(self, account):
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
                print(item.acc_num, ' ', item.name, ' '. item.type_of_acct, ' ',item.deposit)
            #must close file once im finished with file
            infile.close()
        #if it does not fall into my if then it will go to my else statement 
        else:
            #this print statement helps me know if the records are not being displayed or if something is wrong
            print("No records to display")

    #this is to display sp
    def display_sp(num):
        #to find and open file
        file = path.lib.Path("accounts.data")
        #if there is a file follow through with if statement
        if file.exists():
            infile = open("accounts.data", 'rb')
            my_list = pickle.load(infile)
            infile.close()
            found_file = False
            for item in my_list:
                if item.acc_num == num:
                    found = True
                    print(f"your account balance is = {item.deposit}")
        #this is to filter if an account is not found
        elif not found:
            print("No record with this number")

        #the else statment filters if there are no files with the account
        else: 
            print("No records to search")
      

    #we are creating the deposit and withdraw function
    def deposit_and_withdraw(num1, num2):
        #same procedure with opening file and file and loading it
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open("accounts.data", 'rb')
            my_list = pickle.load(infile)
            infile.close()
            os.remove("accounts.data")
            #for loop coming for item in mylist
            for item in my_list:
                if item.acc_num == num1:
                    #to check user wants to deposit
                    if num2 == 1:
                        amount = int(input("Enter the amount to deposit: "))
                        item.deposit += amount
                        print("Your account is updated")
                    #to check if user wants to withdraw
                    elif num2 == 2:
                        amount = int(input("Enter the amount to withdraw: "))
                        #parameter for withdraw
                        if amount <= item.deposit:
                            item.deposit -=amount
                        else:
                            print("Withdraw is too large, greater then amount in account.")
                else:
                    print("no records to search")
                    outfile = open('new_accounts.data','wb')
                    pickle.dump(my_list,outfile)
                    outfile.close()
                    os.rename('new_accounts.data', 'accounts.data')

#creating this to delete entire account
    def delete_acc(num):
        file = pathlib.Path("accounts.data")
        #reads file if it exists
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            #new list to add into 
            newlist = []
            for item in oldlist:
                if item.acc_num == num:
                    item.name = input("Enter the account name: ")
                    item.type = input("Enter the account type: ")
                    item.deposit = input("Enter the amount: ")
            #close file
            outfile = open('newaccounts.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newaccounts.data', 'accounts.data')

    
    def write_accounts_file(account):
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            oldlist.append(account)
            infile.close()
            os.remove('accounts.data')
        else:
            oldlist = [account]
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


#Display
i = ''
num = 0
#this intro did not work 
#intro()

while i != 8:
    print("\t MAIN MENU")
    print("\t1. New Account")
    print("\t2. Deposit Amount")
    print("\t3. Withdraw Amount")
    print("\t4. Balance Enquiry")
    print("\t5. All Account Holder List")
    print("\t6. Close Account")
    print("\t7. Modify An Account")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    i = input()


    if i == '1':
        write_acc()
    elif i == '2':
        num = int(input("\tEnter the Account Number: "))
        deposit_and_withdraw(num, 1)
    elif i == '3':
        num = int(input("\tEnter the Account Number: "))
        deposit_and_withdraw(num, 2)
    elif i == '4':
        num = int(input("\tEnter the Account Number: "))
        display_sp(num)
    elif i == '5':
        display_all()
    elif i == '6':
        num = int(input("\tEnter the Account Number: "))
        delete_acc(num)
    elif i == '7':
        num = int(input("\tEnter the Account Number: "))
        modify_acc(num)
    elif i == '8':
        print("\t Thanks for using our Bank Management System  :)")
    else:
        print("invalid choice")
    
    i = input("Enter your choice: ")


            


        