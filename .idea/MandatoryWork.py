def main():
    quiz()
    return
answer = {}
points = 0
def login_info(my_dict, loginAttempt, passwordAttempt):
    for item in my_dict:
        if loginAttempt in my_dict:
            if my_dict[loginAttempt] == passwordAttempt:
                print("login succesfull")
                return True
            else:
                print("wrong password. try again")
                return False

        else:
            print("user not found. try again")
            return  False




def quiz():
    my_dict = {"PGR107":"Python"}
    running = True

    while running == True:
        loginAttempt = input("enter your user name: ")
        passwordAttempt = input("enter your password: ")
        if login_info(my_dict,loginAttempt,passwordAttempt) == True:
            Q1()
            Q2()
            Q3()
            Q4()
            Q5()
            Q6()
            Q7()
            Q8()
            Q9()
            Q10()
            result()
            running = False
        else:
            continue
    return


def Q1():
    global points
    print("\nquestion 1: \n")
    print("what is the capital of Norway?")
    print("a: Bergen\nb: Oslo\nc: Stavanger\nd: Trondheim")
    userInput = input().lower()
    answer = userInput
    correct_Answer = "oslo"
    correct_Answer2 = "b"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    print("what is the capital of Norway?")
    return
def Q2():
    print("\nquestion 2: \n")
    global points
    print("What is the currency of Norway?")
    print("a: Euro\nb: Pound\nc: Krone\nd: Deutsche Mark")
    userInput = input().lower()
    answer = userInput
    correct_Answer = "krone"
    correct_Answer2 = "c"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return
def Q3():
    print("\nquestion 3: \n")
    global points
    print("What is the largest city in Norway?")
    print("a: Oslo\nb: Stavanger\nc: Bergen\nd: Trondheim")
    userInput = input().lower()
    answer = userInput
    correct_Answer = "oslo"
    correct_Answer2 = "a"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return
def Q4():
    print("\nquestion 4: \n")
    global points
    print("When is constitution day (the national day) of Norway?")
    print("a: 27th May\nb: 17th May\nc: 17th April\nd: 27th April")
    user = input().lower()
    answer = user
    userInput =user.replace(" ", "")
    correct_Answer = "17thmay"
    correct_Answer2 = "b"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return
def Q5():
    print("\nquestion 5: \n")
    global points
    print("What color is the background of the Norwegian flag?")
    print("a: Red\nb: White\nc: Blue\nd: Yellow")
    userInput = input().lower()
    answer = userInput
    correct_Answer = "red"
    correct_Answer2 = "a"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return
def Q6():
    print("\nquestion 6: \n")
    global points
    print("How many countries does Norway border?")
    print("a: 1\nb: 2\nc: 3\nd: 4")
    userInput = input().lower()
    answer = userInput
    correct_Answer = "3"
    correct_Answer2 = "c"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return
def Q7():
    print("\nquestion 7: \n")
    global points
    print("What is the name of the university in Trondheim?")
    print("a: UiS\nb: UiO\nc: NMBU\nd: NTNU")
    userInput = input().upper()
    answer = userInput
    correct_Answer = "NTNU"
    correct_Answer2 = "C"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return
def Q8():
    print("\nquestion 8: \n")
    global points
    print("How long is the border between Norway and Russia?")
    print("a: 96 Km\nb: 196 Km\nc: 296 Km\nd: 396 Km")
    user = input().lower()
    answer = user
    userInput = user.replace(" ","")
    correct_Answer = "196km"
    correct_Answer2 = "b"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return
def Q9():
    print("\nquestion 9: \n")
    global points
    print("Where in Norway is Stavanger?")
    print("a: North Km\nb: South\nc: South-west\nd: South-east")
    user = input().lower()
    answer = user
    userInput = user.replace(" ","")
    correct_Answer = "south-west"
    correct_Answer2 = "c"
    correct_Answer3 = "southwest"
    if userInput == correct_Answer or userInput == correct_Answer2 or correct_Answer3:
        points += 1
    return
def Q10():
    print("\nquestion 10: \n")
    global points
    print("From which Norwegian city did the world’s famous composer Edvard Grieg come?")
    print("a: Oslo\nb: Bergen\nc: Stavanger\nd: Tromø")
    userInput = input().upper()
    answer = userInput
    correct_Answer = "bergen"
    correct_Answer2 = "b"
    if userInput == correct_Answer or userInput == correct_Answer2:
        points += 1
    return

def result():
    global points
    print("\nresult: \n")
    for i, item in enumerate(answer):
        if i == 0:
            print("question: what is the capital of Norway?")
            print(f"your answer: {item}\ncorrect answer: Oslo")
        elif i == 1:
            print("question: What is the currency of Norway?")
            print(f"your answer: {item}\ncorrect answer: Krone")
        elif i == 2:
            print("question: What is the largest city in Norway?")
            print(f"your answer: {item}\ncorrect answer: Oslo")
        elif i == 3:
            print("question: When is constitution day (the national day) of Norway?")
            print(f"your answer: {item}\ncorrect anser: 17thmay")
        elif i == 4:
            print("question: What color is the background of the Norwegian flag?")
            print(f"your answer {item}\ncorrect answer: Red")
        elif i == 5:
            print("question: How many countries does Norway border?")
            print(f"your answer {item}\ncorrect answer: 3")
        elif i == 6:
            print("question: What is the name of the university in Trondheim?")
            print(f"your answer {item}\ncorrect answer: NTNU")
        elif i == 7:
            print("question: How long is the border between Norway and Russia?")
            print(f"your answer: {item}\ncorrect answer: 196 Km")
        elif i == 8:
            print("question: Where in Norway is Stavanger?")
            print(f"your answer: {item}\ncorrect answer: South-west")

        elif i == 9:
            print("question: From which Norwegian city did the world’s famous composer Edvard Grieg come?")
            print(f"your answer: {item}\ncorrect answer: Bergen")
    print(f"total amounts of points: {points}/10")
    print("thanks for participating on this quiz")
    return
if __name__ == "__main__":
    main()