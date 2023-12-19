class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password
        
        
        
    def change_name(self,new_name):    
        self.name = new_name

    def change_pin(self,new_pin):
        self.pin = new_pin
        
        
    def change_password(self,new_password):
        self.password = new_password
        
        
class BankUser(User):
    def __init__ (self,name,pin,password):
        super().__init__(name,pin,password) 
        self.balance = 0
        
        
    def show_balance(self):
        print(self.name, "has an account of:",self.balance)  
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
        print (self.name,"has an account of:",self.balance)
        
        
    def deposit(self,amount):
        self.balance = self.balance + amount     
        print (self.name,"has an account of:",self.balance)       
        
    
    def transfer_money(self,transfer_amount,receiver):
        print("You are transferring $",transfer_amount,"to",receiver.name)
        print("Authentication Required")
        user_pin = int(input("Enter your PIN:"))
        if user_pin == self.pin:
            print("Transfer aunthorized")
            print("Transferring $",transfer_amount,"to",receiver.name)
            self.balance -= transfer_amount
            receiver.balance = receiver.balance + transfer_amount
            return True
        else:
            print("Invalid PIN. Transaction cancelled.")
            return False
            
    def request_money(self,request_amount,receiver):    
        print("You are requesting $",request_amount,"from",self.name)
        print("User authentication is required...")
        user_pin = int(input("Enter "+ self.name + "'s PIN:"))
        if user_pin == self.pin:
            request_password = input("Enter your password:")
            if request_password == receiver.password:
                print("Request Authorized")
                print(self.name,"sent $",request_amount)
                self.balance = self.balance - request_amount
                receiver.balance = receiver.balance + request_amount
            else:
                print("Invalid password. Transaction cancelled.")    
            return True
    
        elif user_pin != self.pin:
            print("Invalid PIN. Transaction cancelled.")
            return False
            
            
            







'''"""Driver() code for Task 1"""

user1 = User("Bob",1234,"password")
print(user1.name,user1.pin,user1.password)'''


'''"""Driver code for Task 2"""
user1.name = "Ranaa"
user1.pin = 4567
user1.password = "newpassword"

print(user1.name,user1.pin,user1.password)'''


'''"""Driver code for task 3"""

bankuser1 = BankUser("Bob",1234,"password")
print(bankuser1.name,bankuser1.pin,bankuser1.password,bankuser1.balance)'''


"""'''Driver code for Task 4'''
bankuser1 = BankUser("Bob",1234,"password")
bankuser1.show_balance()
bankuser1.deposit(float(1000))
bankuser1.withdraw(float(500))"""

'''Driver code for Task 5'''

bankuser1 = BankUser("Bob",1234,"password")
bankuser2 = BankUser("Alice",5678,"newpassword")
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.transfer_money(500,bankuser1)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser1.request_money(250,bankuser2)
bankuser2.show_balance()
bankuser1.show_balance()
