def main():
    temp()
    return

def login_info(my_dict, loginAttempt, passwordAttempt):
    for item in my_dict:
        if loginAttempt in my_dict:
            if my_dict[loginAttempt] == passwordAttempt:
                print("login succesfull")
            else:
                print("wrong password")

        else:
            print("user not found")
    return




def temp():
    my_dict = {"PGR107":"Python"}
    running = True
    while running == True:

        loginAttempt = input("enter your user name: ")
        passwordAttempt = input("enter your password: ")
        login_info(my_dict,loginAttempt,passwordAttempt)
        running = False

    return


if __name__ == "__main__":
    main()