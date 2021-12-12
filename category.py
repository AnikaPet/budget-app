'''Class Category'''

class Category:
    '''Class is used to represent category in the budget.

    Category is identified by the name. Names are case sensitive.

    Attributes
    ----------
    name : str
            name of the category
    balance : float
            current balance for single category
    spent : float
            how much money is spent in this category
    percent : int
            how many percents category represents in user's budget
    transactions : list
            each element is dictionary representing one transaction
            transaction has two keys: amount(float) and description(optinal,default is empty string)
    '''

    def __init__(self,name):
        '''
        Parameters
        -----------
        name : str
                name of the category
        '''

        self.name = name
        self.balance = 0.0
        self.spent = 0.0
        self.percent = 0.0
        self.transactions = []

    def __str__(self):
        '''prints all transactions from one category and current balance'''

        lines = []

        for transaction in self.transactions:
            lines.append(transaction['description'][0:20]+" "+str(transaction['amount']))
        lines.append("------------------------")
        lines.append("balance: "+str(self.balance)+"\n")

        return "\n".join(lines)

    def get_balance(self):
        '''returns current balance'''

        return self.balance
