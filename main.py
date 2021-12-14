'''Small budget app.

Tracks all your spending and transactions by categories.
Supports multiple users. Each user has it's own .txt file in 
directory users. Files contain user's transactions.

Name of categories are unique and case insensitive.
Name of users are unique and case insenstivie. 
'''

from user import User

user_1 = User("Petar")
user_1.add_category("Food")
user_1.deposit(100,"Food","initial deposit")
user_1.withdraw(30,"Food","groceries")
user_1.add_category("Car")
user_1.transfer(2,"Food","Car")
user_1.budget_summary()
user_1.print_category("Car")

user_2 = User("Janko")
user_2.add_category("School")
user_2.deposit(30,"School","initial deposit")
user_2.add_category("Food")
user_2.budget_summary()
