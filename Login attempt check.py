import time

class LoginSystem:
    def __init__(self):
        self.correct_password = None #This is being setup by the user
        self.attempts = 0 #Counts the number of attempts
        self.locked_until = None #Time period set to lock the user out

    def set_password(self):
        self.correct_password=input("Enter the password that will be set to verify")
        print(f"Password has been set successfully")
    
    def is_locked(self):
        if self.locked_until and time.time() < self.locked_until: #If self.locked_until is None which we have initially assigned, it means the account was never locked, so it skips checking further. If self.locked_until has a time, it means the account was locked, so we continue checking.
            return True # If locked_until has a time and the current time is still within the lock period , it return is locked
        return False 
    
    def login(self):
        if self.correct_password is None:
            print(f"You have not set a password")
            return False
    
        password= input ("Please enter your password")

        if password == self.correct_password:
            print (f"Successfuly login")
            self.attempt=0
            return True

        else:
             self.attempts+=1
             print (f"you have set the wrong password")
    
        if self.attempts >=3:
            self.locked_until = time.time() + 30
            print(f"Too many attempts, you account has been locked for 30 seconds")

        return False

# Example usage
login_system = LoginSystem()
login_system.set_password()  # User sets their password

while True:
    login_system.login()
    time.sleep(1)  # Small delay to simulate real usage
    

    
        