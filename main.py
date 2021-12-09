'''
demonstration
Name of categories ARE case sensitive.
'''

from user import User

user_1 = User("Marko")
user_1.add_category("Food")
user_1.deposit(100,"Food","initial deposit")
user_1.withdraw(300,"Food","groceries")

user_2 = User("Janko")
