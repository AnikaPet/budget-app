'''Class category'''

class Category:
    '''Class is used to represent category in the budget.

    Category is identified by the name. Names are case sensitive.
    A brief summary of its purpose and behavior
    Any public methods, along with a brief description
    Any class properties (attributes)
    '''

    def __init__(self,name):
        '''
        A brief description of what the method is and what it’s used for
        Any arguments (both required and optional) that are passed including keyword arguments
        Label any arguments that are considered optional or have a default value
        Any side effects that occur when executing the method
        Any exceptions that are raised
        Any restrictions on when the method can be called
        '''

        self.name = name
        self.balance = 0.0
        self.spent = 0.0
        self.percent = 0.0
        self.transactions = []

    def __str__(self):

        lines = []

        for transaction in self.transactions:
            lines.append(transaction['description'][0:20]+" "+str(transaction['amount']))
        lines.append("---------------")
        lines.append("balance: "+str(self.balance)+"\n")

        return "\n".join(lines)

    def get_balance(self):
        '''returns current balance'''

        return self.balance
