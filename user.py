'''Small budget app.

Tracks all your spending and transactions by categories.
'''
import os
from category import Category

class User:
    '''Class that is used to represent single user.

    Brief summary.
    Each user has it's own file. Write every transaction(dictionary) in json file.

    balance: sum of all balances in categories
    budget_summary: for category in categories print category.summary
    TODO: change error messages
    '''

    def __init__(self,name):

        if not os.path.isdir("users"):
            os.makedirs("users", exist_ok=True)

        try:
            open("users\\user_"+name.lower()+".txt",'x',encoding="utf8")
        except FileExistsError:
            print("User with name "+name+" already exists. Please use another name.")

        self.name = name
        self.balance = 0.0
        self.spent = 0.0
        self.categories = []
        self.file_name = "users\\user_"+self.name.lower()+".txt"

        with open(self.file_name,'w',encoding="utf8") as user_file:
            user_file.write(self.name+"'s transactions"+"\n")

    def category_error_message(self,category_name):
        '''print error message for not existing category'''

        print(self.name+ " does not have "+category_name+" category in the budget.")

    def add_category(self,category_name):
        '''adding category in user's budget'''

        category = [category for category in self.categories if category.name == category_name]
        if category:
            print(self.name+" already has "+category_name+" category in the budget.")
        else:
            self.categories.append(Category(category_name))

    def print_category(self,category_name):
        '''printing category if exists'''

        category = [category for category in self.categories if category.name == category_name]
        if category:
            category = category[0]
            print("*** "+self.name+"'s "+category_name+" ***")
            print(category)
        else:
            self.category_error_message(category_name)

    def budget_summary(self):
        '''prints budget summary'''

        lines = []
        lines.append("*** "+self.name+"'s budget summary"+" ***")
        for category in self.categories:
            category.percent = round((category.spent/self.spent)*100)
            lines.append(category.name+": "+str(category.percent)+"%")

        lines.append("------------------------")
        lines.append("Balance: "+str(self.balance))
        lines.append("Spent: "+str(self.spent))

        result = "\n".join(lines)
        print(result)

    def withdraw(self,amount,category_name,description=""):
        '''withdraw method'''

        transaction = {"amount":-1*amount,"description":description}
        category = [category for category in self.categories if category.name == category_name]

        if category:
            category = category[0]

            if self.check_funds(amount,category):
                category.transactions.append(transaction)
                category.balance -= round(amount,2)
                category.spent += round(amount,2)
                self.spent += round(amount,2)
                self.balance -= round(amount,2)

                with open(self.file_name,'a',encoding="utf8") as user_file:
                    user_file.writelines([str(transaction),"\n"])

                return True

            print("Withdraw unsuccessful.")
            print(self.name+" does not have enough funds for this action.")
            print(str(transaction))
            return False

        print("Withdraw unsuccessful.")
        self.category_error_message(category_name)
        return False

    def check_funds(self,amount,category):
        '''checks if there is enough funds for transaction'''

        return category.balance>=amount

    def deposit(self,amount,category_name,descripton=""):
        '''
        deposit money
        '''

        category = [category for category in self.categories if category.name == category_name]
        if category:
            category = category[0]

            transaction = {"amount":amount,"description":descripton}
            category.transactions.append(transaction)
            category.balance += round(amount,2)
            self.balance += round(amount,2)

            with open(self.file_name,'a',encoding="utf8") as user_file:
                    user_file.writelines([str(transaction),"\n"])

        else:
            print("Deposit unsuccessful.")
            self.category_error_message(category_name)

    def transfer(self,amount,source_category_name,dest_category_name):
        '''transfers money from one to another category if possible'''

        transaction = {"amount":amount,"description":"Transfer from {self.name} to {dest_category.name}"}

        source_category = [category for category in self.categories if category.name == source_category_name]
        if source_category:
            source_category = source_category[0]
        else:
            print("Transfer unsuccessful.")
            self.category_error_message(source_category_name)
            return False

        dest_category = [category for category in self.categories if category.name == dest_category_name]
        if dest_category:
            dest_category = dest_category[0]
        else:
            print("Transfer unsuccessful.")
            self.category_error_message(dest_category_name)
            return False

        if source_category.withdraw(amount,"Transfer to {dest_category.name}"):
            dest_category.deposit(amount,"Transfer from {self.name}")

            with open(self.file_name,'a',encoding="utf8") as user_file:
                user_file.writelines([str(transaction),"\n"])

            return True
        
        else:
            print("Transfer unsuccessful.")
            print(self.name+" does not have enough funds for this action.")
            print(str(transaction))
            return False
