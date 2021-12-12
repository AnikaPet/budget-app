'''Class User'''
import os
from category import Category

class User:
    '''Class that is used to represent single user.

    Each user is identified by name. Names are case sensitive.

    Attributes
    -----------
    name : str
            name of the user
    balance : float
            current balance
    categories : list
            list of Category objects representing categories in user's budget
    file_name: str
            name of user's .txt file containing all transactions

    Methods
    --------
    category_error_message(category_name)
        Prints error message indicating that category with
        name category_name does not exist in user's budget.
    add_category(category_name)
        Creates Category object and adds it to the categories list if possible.
    print_category(category_name)
        Calls __str__ method for each Category object from categories list.
    budget_summary()
        Print summary of user's budget.
    withdraw(amount,category_name,description="")
        Withdraws money from specific category if possible.
    deposit(amount,category_name,description="")
        Deposits money to specific category if possible.
    transfer(amount,source_category_name,dest_category_name)
        Transfers money from one to another category if possible.
    '''

    def __init__(self,name):
        '''
        Parameters
        -----------
        name : str
                name of user

        Raises
        -------
        FileExistsError
            If user with name given as parameter already exists.
        '''

        if not os.path.isdir("users"):
            os.makedirs("users", exist_ok=True) #creates users directory

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
            user_file.write(self.name+"'s transactions"+"\n") #creates .txt file for each user

    def category_error_message(self,category_name):
        '''prints error message for not existing category'''

        print(self.name+ " does not have "+category_name+" category in the budget.")

    def add_category(self,category_name):
        '''adds category in user's budget if category does not exist in user's budget'''

        category = [category for category in self.categories if category.name == category_name]
        if category:
            print(self.name+" already has "+category_name+" category in the budget.")
        else:
            self.categories.append(Category(category_name))

    def print_category(self,category_name):
        '''prints category if possible'''

        category = [category for category in self.categories if category.name == category_name]
        if category:
            category = category[0]
            print("*** "+self.name+"'s "+category_name+" ***")
            print(category)
        else:
            self.category_error_message(category_name)

    def budget_summary(self):
        '''prints budget summary - categories with percentages
        Raises
        -------
        ZeroDivisonError:
                If user didn't spent any money in category.
        '''

        lines = []
        lines.append("*** "+self.name+"'s budget summary"+" ***")
        for category in self.categories:
            try:
                category.percent = round((category.spent/self.spent)*100)
                lines.append(category.name+": "+str(category.percent)+"%")
            except ZeroDivisionError:
                lines.append(category.name+": 0%")

        lines.append("------------------------")
        lines.append("Balance: "+str(self.balance))
        lines.append("Spent: "+str(self.spent))

        result = "\n".join(lines)
        print(result)

    def withdraw(self,amount,category_name,description=""):
        '''withdraws money from category if possible

        Parameters
        -----------
        amount: float
                amount of money
        category_name : str
                name of the category
        description :
                description of transaction
        '''

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
        '''checks if there is enough funds for transaction

        Parameters
        -----------
        amount : float
                amount of money
        category : Category
        '''

        return category.balance>=amount

    def deposit(self,amount,category_name,descripton=""):
        ''' deposits money to category if possible

        Parameters
        -----------
        amount : float
                amount of money
        category_name : str
                name of the category
        description : str
                description of transaction
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
        '''transfers money from one to another category if possible

        Parameters
        -----------
        amount : float
                amount money
        source_category_name : str
                name of source category for transfer
        dest_category_name : str
                name of destionation category for transfer
        '''

        transaction = {"amount":amount,"description":"Transfer from "+source_category_name+" to "+dest_category_name}

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

        if self.withdraw(amount,source_category_name,"Transfer to "+dest_category_name):
            self.deposit(amount,dest_category_name,"Transfer from "+dest_category_name)

            with open(self.file_name,'a',encoding="utf8") as user_file:
                user_file.writelines([str(transaction),"\n"])

            return True

        else:
            print("Transfer unsuccessful.")
            print(self.name+" does not have enough funds for this action.")
            print(str(transaction))
            return False
