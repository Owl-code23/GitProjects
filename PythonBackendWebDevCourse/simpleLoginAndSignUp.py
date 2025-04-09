print("Create your account")

iusername = input("Input username: ")
ipassword = input("Input password: ")

print(f"user '{iusername}' created successfully")
print("Login now")

lusername = input("Input username: ")
lpassword = input("Input password: ")

if iusername == lusername and ipassword == lpassword:
    print("User logged in successfully")
else:
    print("Invalid credentials")