# python quiz game git
questions = ("how many elements are there in an periodic table?: " ,
"Which animal lays the largest eggs?:" ,
             "what is the most abundnt gas in earth's atmosphere?: " ,
             "how many bones are in the human body?:" ,
             "which planet in the solar system is the hottest?: ")


options = (("A.116", "B.200 ","C.118 ","D.122 "),
           ("A.blue whale ", "B.Ostrich ","C.shark ","D.Elephant "),
           ("A.Nitrogen ", "B.Hydrogen ","C.Oxygen ","D.Helium "),
           ("A.206 ", "B.205 ","C.114 ","D.222 "),
           ("A.Mars ", "B.Venus ","C.Earth ","D.Jupyter "))

answers = ("C" , "B" , "A" , "A" , "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)

    for option in options[question_num]:
        print(option)

   guess = input("Enter (A, B , C ,D): ").upper()
   guesses.append(guess)
   if guess == answers[question_num]
       score += 1
       print("Correct")
   else:
       print("Incorrect")
       Print(f"{answers[question_num]} is the Correct Answer")
   question_num += 1


print("---------------")
print("     RESULT    ")
print("---------------")

print("answers: " , end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: " , end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")




