
quiz = {
    'question1' : {
      "question": "what is the capital of France?",
      "answer" : "Paris"},
    'question2' : {
        "question" : "what is the capital of Nepal?",
        "answer" : "Kathmandu"},
    'question3': {
        "question": "what is the capital of Italy?",
        "answer": "Rome"},
    'question4': {
        "question": "what is the capital of Germany?",
        "answer": "Berlin"},
    'question5': {
        "question": "what is the capital of Portugal?",
        "answer": "Lisbon"},
    'question6': {
        "question": "what is the capital of Spain?",
        "answer": "Madrid"},
    'question7': {
        "question": "what is the capital of Switzerland?",
        "answer": "Bern"},
    'question8': {
        "question": "what is the capital of Morocco?",
        "answer": "Rabat"},
    'question9': {
        "question": "what is the capital of Russia?",
        "answer": "Moscow"},
    'question10': {
        "question": "what is the capital of China?",
        "answer": "Beijing"}
}

score = 0

for key , value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
           print("Your score = ",score)
           print("")

    else:
          print("Wrong")
          print("The right answer is " + value["answer"])
          print("Your score = ",score)
          print("")

print("You got " + str(score) + " out of 10")git