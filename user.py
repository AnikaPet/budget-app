'''Small budget app.

Tracks all your spending and transactions by categories.
'''

from category import Category

class User:
    '''Class that is used to represent single user.

    Brief summary.
    Each user has it's own file. Write every transaction(dictionary) in json file.

    balance: sum of all balances in categories
    budget_summary: for category in categories print category.summary
    TODO: replace error messages with raising exceptions
    TODO: figure out how to write transactions in json file
    '''

    def __init__(self,name):

    # check if directory user exists if it does not create one
    # check if given user_name already exists in directory users if yes raise exception

        self.name = name
        self.balance = 0.0
        self.categories = []

        file_name = "user_"+self.name.lower()+".txt"
        with open(file_name,'w',encoding="utf8") as user_file:
            user_file.writelines(self.name+"'s transactions")

    def add_category(self,category_name):
        '''adding category in user's budget'''

        category = [category for category in self.categories if category.name == category_name]
        if category:
            print(self.name+" already has this category in the budget.")
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
            print(self.name+ " does not have this category in the budget.")

    def withdraw(self,amount,category_name,description=""):
        '''withdraw method'''

        category = [category for category in self.categories if category.name == category_name]

        if category:
            category = category[0]

            if self.check_funds(amount,category):
                transaction = {"amount":-1*amount,"description":description}
                category.transactions.append(transaction)
                category.balance -= round(amount,2)
                category.spent += round(amount,2)
                return True

            print("Withdraw unsuccessful.")
            print(self.name+" does not have enough funds for this action.")
            return False

        print("Withdraw unsuccessful.")
        print(self.name+" does not have this category in budget.")
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
        else:
            print("Deposit unsuccessful.")
            print(self.name+" does not have this category in budget.")

    def transfer(self,amount,source_category_name,dest_category_name):
        '''transfers money from one to another category if possible'''

        source_category = [category for category in self.categories if category.name == source_category_name]
        if source_category:
            source_category = source_category[0]
        else:
            print("Transfer unsuccessful.")
            print(self.name+" does not have source category in the budget.")
            return False

        dest_category = [category for category in self.categories if category.name == dest_category_name]
        if dest_category:
            dest_category = dest_category[0]
        else:
            print("Transfer unsuccessful.")
            print(self.name+" does not have destination category in the budget.")
            return False

        if source_category.withdraw(amount,"Transfer to {dest_category.name}"):
            dest_category.deposit(amount,"Transfer from {self.name}")
            return True
        return False
