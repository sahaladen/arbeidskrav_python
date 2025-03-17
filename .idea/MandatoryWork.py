def main():
    temp()
    return

def login_info(my_dict, loginAttempt, passwordAttempt):
    for item in my_dict:
        if loginAttempt in my_dict:
            if my_dict[loginAttempt] == passwordAttempt:
                print("login succesfull")
                return True
            else:
                print("wrong password")
                return False

        else:
            print("user not found")
            return  False




def temp():
    my_dict = {"PGR107":"Python"}
    running = True
    while running == True:

        loginAttempt = input("enter your user name: ")
        passwordAttempt = input("enter your password: ")
        login_info(my_dict,loginAttempt,passwordAttempt)
        if login_info() == True:
            Q1()
        running = False

    return


def Q1():
    print("inni q1")
    return
def Q2():
    print("inni q2")
    return
def Q3():
    print("inni q3")
    return
def Q4():
    print("inni q4")
    return
def Q5():
    print("inni q5")
    return
def Q6():
    print("inni q6")
    return
def Q7():
    print("inni q7")
    return
def Q8():
    print("inni q8")
    return
def Q9():
    print("inni q9")
    return
def Q10():
    print("inni q10")
    return
if __name__ == "__main__":
    main()