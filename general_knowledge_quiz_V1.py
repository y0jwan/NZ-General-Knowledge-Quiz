""""Kids NZ General Knowledge Quiz - v1 Welcome Screen
Created by Yojwan Chua"""

"""Variables"""
get_info = ""
name = ""
age = 0

"""Component 1 - Welcome user to quiz"""
print("********** NZ General Knowledge Quiz **********")
print(" ")
print("  Welcome to the New Zealand general knowledge \n"
      "            quiz for kids aged 5-11")
print()

"""Let user choose to start or quit program"""
begin_quiz = input("Press 'Y' to start or 'X' to quit: ")
if begin_quiz == "X":
    print("You have exited the quiz.")
else:
    """Get user info"""
    name = input("Please enter your name : ")
    age = int(input(f"Welcome {name}, please enter your age: "))
    """Give quiz instructions"""
    print()
    print("Here are the quiz instructions: \n"
          "1. You will be asked five questions about New Zealand. \n"
          "2. You will need to choose one out of the four answers in every question. \n"
          "3. If you correctly answer a question, a point will be added to your total score. \n"
          "4. If you incorrectly answer a question, no points will be added to your total score. \n"
          "5. At the end of the quiz you will be shown your total score which will be a mark out of five.")





    

    

   
