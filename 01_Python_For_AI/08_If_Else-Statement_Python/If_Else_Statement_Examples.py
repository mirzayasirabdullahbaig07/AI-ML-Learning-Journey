# if else statement are also called dicision control statement
# These are used in every programing language
# if else statement are used when the branching occur
# for example login page
# if credantial are right login in else send error msg


# A login page example for understanding if else statements

# correct email: yasirabdullah4549@gmail.com
# password: yasir@1234

email = input("Enter your email: ")

if '@' in email:
    if email == "yasirabdullah4549@gmail.com":
        password = input("Enter your password: ")
        if password == "yasir@1234":
            print("Welcome to my website")
        else:
            print("Password incorrect")
            password = input("Again enter your password: ")
            if password == "yasir@1234":
                print("Finally, password is correct")
            else:
                print("Password is still incorrect")
    else:
        print("Incorrect email or password")
else:
    print("Enter the correct email")


# we covered if else, elif, and nested elif, we covered 3 level statements    

