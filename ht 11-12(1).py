class Password:
    def __init__(self, password):
        self.password = password

    def display(self):
        if len(self.password) < 8:
            return "Password must contain at least 8 characters"
        elif self.password.islower():
            return "Password must contain an uppercase letter"
        elif self.password.isupper():
            return "Password must contain a lowercase letter"
        elif self.password.isalpha():
            return "Password must contain at least one number"
        elif not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for char in self.password):
            return "Password must contain at least one symbol"
        else:
            return "Password is valid"

# User Input
user_password = input("Enter the password: ")
p = Password(user_password)
print(p.display())
