""""Kids NZ General Knowledge Quiz - v5 Error control
Created by Yojwan Chua"""

"""Variables"""
get_info = ""
name = ""
start_quiz_a = ""
quiz_a1 = ""
quiz_a2 = ""
quiz_a3 = ""
quiz_a4 = ""
quiz_a5 = ""
start_quiz_b = ""
quiz_b1 = ""
quiz_b2 = ""
quiz_b3 = ""
quiz_b4 = ""
quiz_b5 = ""
one_point = 1

def age_check(question):
    """Check for valid age"""
    int_error = "\nSorry, you need to enter a number for your age.\n"
    age_error = "\nSorry, this quiz is only meant for kids age 5-11 year olds."
    age_ = ""
    while not age_:
        try:
            age_ = int(input(question))
            if age_ < 5 or age_ > 11:
                return age_error
        except ValueError:
            print(int_error)
    return age_

def replay():
    restart_quiz = input("Would you like to restart the quiz? \n"
                             "Press 'Y' to restart or press 'X' to quit: ").upper()
    if restart_quiz == "X":
        print("\nYou have exited the quiz. \n"
                "Have a nice day!")

"""Component 2 - Quiz A for 5-7 year olds"""
def quiz_a():
    """Component 3 - Set up total score"""
    total_score = 0
    valid_answers = ["A", "B", "C", "D"]
    start_quiz_a = input("Press 'Y' to begin the quiz: ").upper()
    if start_quiz_a == "Y":
        print()
        quiz_a1 = input("Question 1. \n"
                        "What is the capital of New Zealand? \n"
                        " A) Auckland \n "
                        "B) Wellington \n "
                        "C) Christchurch \n "
                        "D) Hamilton \n "                   
                        "Enter answer: ").upper()
        while quiz_a1 not in valid_answers:
            quiz_a1 = input("\nPlease enter a valid answer. \n"
                            "\nQuestion 1. \n"
                        "What is the capital of New Zealand? \n"
                        " A) Auckland \n "
                        "B) Wellington \n "
                        "C) Christchurch \n "
                        "D) Hamilton \n "                   
                        "Enter answer: ").upper()
        if quiz_a1 == "B":
            print(f"\nGood Job, {name}! Wellington is the capital of New Zealand. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: B) Wellington.")
        quiz_a2 = input("\nQuestion 2. \n"
                        "Which city is known as 'The Garden City'? \n"
                        " A) Wellington \n "
                        "B) Christchurch \n "
                        "C) Paeroa \n "
                        "D) Auckland \n "                   
                        "Enter answer: ").upper()
        while quiz_a2 not in valid_answers:
            quiz_a2 = input("\nPlease enter a valid answer. \n"
                            "\nQuestion 2. \n"
                        "Which city is known as 'The Garden City'? \n"
                        " A) Wellington \n "
                        "B) Christchurch \n "
                        "C) Paeroa \n "
                        "D) Auckland \n "                   
                        "Enter answer: ").upper()
        if quiz_a2 == "B":
            print(f"\nGood Job, {name}! Christchurch is known as the 'The Garden City'. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: B) Christchurch")
        quiz_a3 = input("\nQuestion 3. \n"
                        "Where did L&P Soda originally come from? \n"
                        " A) Putaruru \n "
                        "B) Waihi \n "
                        "C) Paeroa \n "
                        "D) Auckland \n "                   
                        "Enter answer: ").upper()
        while quiz_a3 not in valid_answers:
            quiz_a3 = input("\nPlease enter a valid answer. \n"
                            "\nQuestion 3. \n"
                        "Where did L&P Soda originally come from? \n"
                        " A) Putaruru \n "
                        "B) Waihi \n "
                        "C) Paeroa \n "
                        "D) Auckland \n "                   
                        "Enter answer: ").upper()
        if quiz_a3 == "C":
            print(f"\nGood Job, {name}! L&P Soda originally came from Paeroa. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: C) Paeroa.")
        quiz_a4 = input("\nQuestion 4. \n"
                        "What month is Matariki celebrated in? \n"
                        " A) April \n "
                        "B) May \n "
                        "C) May, June, or July \n "
                        "D) July \n "                   
                        "Enter answer: ").upper()
        while quiz_a4 not in valid_answers:
            quiz_a4 = input("\nPlease enter a valid answer. \n"
                            "\nQuestion 4. \n"
                        "What month is Matariki celebrated in? \n"
                        " A) April \n "
                        "B) May \n "
                        "C) May, June, or July \n "
                        "D) July \n "                   
                        "Enter answer: ").upper
        if quiz_a4 == "C":
            print(f"\nGood Job, {name}! Matariki is celebrated in May, June, or July. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: C) May, June, or July.")
        quiz_a5 = input("\nQuestion 5. \n"
                        "What colour is Kakariki? \n"
                        " A) Green \n "
                        "B) Blue \n "
                        "C) Black \n "
                        "D) Grey \n "                   
                        "Enter answer: ").upper()
        while quiz_a5 not in valid_answers:
            quiz_a5 = input("\nPlease enter a valid answer. \n"
                            "\nQuestion 5. \n"
                        "What colour is Kakariki? \n"
                        " A) Green \n "
                        "B) Blue \n "
                        "C) Black \n "
                        "D) Grey \n "                   
                        "Enter answer: ").upper()
        if quiz_a5 == "A":
            print(f"\nGood Job, {name}! Kakariki is green. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: A) Green.")
    print("\nYou have successfully completed the NZ General Quiz!\n"
          f"Your final score was: {total_score}/5 \n"
          f"\nThank you for participating {name}!")
    
"""Component 2 - Quiz B for 8-11 year olds"""
def quiz_b():
    """Component 3 - Set up total score"""
    total_score = 0
    start_quiz_b = input("Press 'Y' to begin the quiz: ").upper()
    if start_quiz_b == "Y":
        print()
        quiz_b1 = input("Question 1. \n"
                        "What is the name of the stretch of water that separates the North and South Islands? \n"
                        " A) Wellington Strait \n "
                        "B) Tasman Channel \n "
                        "C) Cook Strait \n "
                        "D) Kaikoura Strait \n "                   
                        "Enter answer: ").upper()
        if quiz_b1 == "C":
            print(f"\nGood Job, {name}! The Cook Strait separates the North and South Islands. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: C) Cook Strait.")
        quiz_b2 = input("\nQuestion 2. \n"
                        "Which city houses the Beehive? \n"
                        " A) Wellington \n "
                        "B) Christchurch \n "
                        "C) Paeroa \n "
                        "D) Auckland \n "                   
                        "Enter answer: ").upper()
        if quiz_b2 == "A":
            print(f"\nGood Job, {name}! The Beehive is located in Wellington. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: A) Wellington.")
        quiz_b3 = input("\nQuestion 3. \n"
                        "Which town has a giant carrot as a landmark? \n"
                        " A) Taihape \n "
                        "B) Waihi \n "
                        "C) Paeroa \n "
                        "D) Ohakune \n "                   
                        "Enter answer: ").upper()
        if quiz_b3 == "D":
            print(f"\nGood Job, {name}! Ohakune has a giant carrot as their landmark. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: D) Ohakune.")
        quiz_b4 = input("\nQuestion 4. \n"
                        "Where is the 90 mile beach? \n"
                        " A) Top of the North Island \n "
                        "B) Bottom of the South Island \n "
                        "C) Bottom of the North Island \n "
                        "D) Top of the South Island \n "                   
                        "Enter answer: ").upper()
        if quiz_b4 == "A":
            print(f"\nGood Job, {name}! The 90 mile beach is located at the top of the North Island. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: A) Top of the North Island.")
        quiz_b5 = input("\nQuestion 5. \n"
                        "When was the Treaty of Waitangi? \n"
                        " A) 1815 \n "
                        "B) 1840 \n "
                        "C) 1855 \n "
                        "D) 1875 \n "                   
                        "Enter answer: ").upper()
        if quiz_b5 == "B":
            print(f"\nGood Job, {name}! The Treaty of Waitangi was signed in 1840. \n"
                "+1 Point")
            total_score += one_point
        else:
            print(f"\nUnfortunately, that is incorrect {name}. The answer was: B) 1840.")
    print("\nYou have successfully completed the NZ General Quiz!\n"
          f"Your final score was {total_score}/5 \n"
          f"\nThank you for participating {name}!")
    
"""Give quiz instructions"""
def quiz_instructions():
    print("\nHere are the quiz instructions: \n"
        "1. You will be asked five questions about New Zealand. \n"
        "2. You will need to choose one out of the four answers in every question by entering the \n"
        "letter that corresponds with your answer. \n"
        "3. If you correctly answer a question, a point will be added to your total score. \n"
        "4. If you incorrectly answer a question, no points will be added to your total score. \n"
        "5. At the end of the quiz you will be shown your total score which will be a mark out of five.")
    print()
    
#Main Routine
"""Component 1 - Welcome user to quiz"""
print("********** NZ General Knowledge Quiz **********")
print()
print("  Welcome to the New Zealand general knowledge \n"
      "            quiz for kids aged 5-11")
print()
"""Let user choose to start or quit program"""
begin_quiz = input("Press 'Y' to start or 'X' to quit: ").upper()
while len(begin_quiz) > 1:
    begin_quiz = input("\nPlease enter only one character. \n"
                       "\nPress 'Y' to start or 'X' to quit: ").upper()
if begin_quiz == "X":
    print("You have exited the quiz. \n"
          "Have a nice day!")
else:
    restart_quiz = ""
    while restart_quiz != "X":
        """Get user info"""
        name = input("\nPlease enter your name: ")
        while len(name) < 2:
            name = input("Names must be at least 2 characters long\n"
                        "Please enter your name: ")
        age = age_check(f"Welcome {name}, please enter your age: ")
        if not isinstance(age,int):
            print(age)
            continue
        if age < 8 and age > 4:
            quiz_instructions()
            quiz_a()
            replay()
        if age < 12 and age > 7:
            quiz_instructions()
            quiz_b()    
            replay()
            
        

  
            
        


    
        



    
    


  
            
        


    
        



    
    

