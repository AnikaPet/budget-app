'''Small budget app.

Tracks all your spending and transactions by categories.
Supports multiple users. Each user has it's own .txt file in 
directory users. Files contain user's transactions.

Name of categories are unique and case sensitive.
Name of users are unique and case senstivie. 
'''

from user import User

user_1 = User("Marko")
user_1.add_category("Food")
user_1.deposit(100,"Food","initial deposit")
user_1.withdraw(300,"Food","groceries")

user_2 = User("Janko")
