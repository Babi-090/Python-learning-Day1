#python quiz game
questions=(("Who is the prime minister of Nepal?"),
           ("What is the capital city of France?"),
           ("When was Python created?"),)
           

options=(("A. Babisha Adhikari","B. Sushila Karki","C. KP Oli"),
         ("A. Kathmandu","B. Vienna","C. Paris"),
         ("A. 2000","B. 1991","C. 1881"))

answers=(("B"),
         ("C"),
         ("B"))
guesses=[]
score=0
question_num=0
for question in questions:
  print("-----------------")
  print(question)
  for option in options[question_num]:
    print(option)
  guess=input("Enter (A ,B , C):" ).upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score+=1
    print("CORRECT")
  else:
    print("INCORRECT")
    print(f"{answers[question_num]} is the correct answer.")
  question_num+=1
print(f"Your answers are:{guesses}")
print(f"The correct answers are:{answers}")
print(f"Your score is: {score}/{len(questions)}")