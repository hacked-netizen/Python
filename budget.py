import math

class Category:
  def __init__(self, categoryName):
    self.categoryName = categoryName
    self.ledger = list()
    self.balance = 0

  def __str__(self):
    statement = ""
    descWidth = 23
    amtWidth = 7
    statement += self.categoryName.center(descWidth+amtWidth, "*") + "\n"
    for transaction in self.ledger:
      statement += transaction["description"][:descWidth].ljust(descWidth, " ") + "{:.2f}".format(transaction["amount"]).rjust(amtWidth, " ") + "\n"
    statement += "Total: {:.2f}".format(self.balance)
    return statement

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({
      "amount": amount,
      "description": description
    })

  def withdraw(self, amount, description=""):
    if self.balance-amount < 0:
      return False
    else:
      self.balance -= amount
      self.ledger.append({
      "amount": -amount,
      "description": description
    })
    return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.balance-amount < 0:
      return False
    else:
      self.withdraw(amount, "Transfer to {}".format(category.categoryName))
      category.deposit(amount, "Transfer from {}".format(self.categoryName))
      return True

  def check_funds(self, amount):
    if self.balance < amount:
      return False
    return True    

def create_spend_chart(categories):
  spendingByCategory = {}
  totalSpending = 0
  for category in categories:
    spending = 0
    for transaction in category.ledger:
      if transaction["amount"]<0:
        spending += abs(transaction["amount"])
    spendingByCategory[category.categoryName] = spending
    totalSpending += spending
  percentageSpending = {}
  for category in spendingByCategory:
    percentageSpending[category] = math.floor((spendingByCategory[category]/totalSpending)*10)*10
  
  bar_chart = "Percentage spent by category\n"
  width = 3
  for percentage in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
    bar_chart += str(percentage).rjust(width, " ")
    bar_chart += "|"
    for category in percentageSpending:
      if percentage <= percentageSpending[category]:
        bar_chart += "o".center(width, " ")
      else:
        bar_chart += "".center(width, " ")
    bar_chart += " \n"
  bar_chart += "    "
  largest = None
  for category in percentageSpending:
    bar_chart += "---"
    if largest is None or len(category)>largest:
      largest = len(category)
  bar_chart += "-\n"
  for index in range(largest):
    bar_chart += "    "
    for category in percentageSpending:
      if index < len(category):
        bar_chart += category[index].center(width, " ")
      else:
        bar_chart += "".center(width, " ")
    bar_chart += " \n"
  return bar_chart[:len(bar_chart)-1]
  
