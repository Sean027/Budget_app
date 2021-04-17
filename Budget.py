#Create a Budget class
     #instantiate it with a category like food, entertainment, clothing etc ......

     #object should be able to deposit, withdraw, transfer, and find the balance.

from Budget import Budget
class Budget:

    def _init_(self, name, balance)
      self.name = Name
      self.balance = balance


#deposit method
    def deposit(self, amount):
        old_balance = self.balance
        self.balance = self.balance + amount  #this adds the old balance and the amount the user wants to deposit

        return f'old balance: {old_balance}, New balance: {self.balance}'  #this shows the current balance 

#withdrawal method 
    def withdraw(self,amount):
        old_balance = self.balance
        if(self.balance < amount):
            print('You do not have sufficient funds')
        else:
            self.balance = self.balance - amount
            retun f'old balance: {old_balance}, New balance: {self.balance}
            
            
#balance method
    def get_balance(self):
        feedback = f'Your budget app balance is {self.balance}'
        return feedback

#transfer method
    def transfer(self, amount, transfer_to):
        if(self.balance < amount):
            print('You do not have sufficient funds')
        else:
            self.balance = self.balance - amount  #this subtracts the amount removed from the category transferred from
            transfer_to.balance = transfer_to.balance + amount #this adds the amount transferred to the previous amount in that category

            feedback = f'You transferred $ {amount} to {transfer_to.name} \n'
            feedback += f'The balance for {self.name} is now {self.balance} \n'
            feedback += f'The balance for {trasfer_to.name} is now {transfer_to.balance}'
            return feedback

#foodC = Budget('food', 10000) #food_budget is the object from the class, Budget
#clothingC = Budget('clothing', 25000)
#entertainmentC = Budget('Entertainment', 15000)

#foodC.deposit(3000)

#foodC.withdraw(amount=4000)

#food_budget.transfer(2000, entertainment_budget)

#foodC.get_balance()
#clothingC.get_balance()
#entertainmentC.get_balance()

#print(foodC.transfer(1000, entertainmentC))