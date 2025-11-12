import random

words =["laptop", "python" , "program","university","engineering"]
chosen_Word=random.choice(words)

lives=6
history = set()
display=["_"]*len(chosen_Word)

while "_" in display and lives>0:

  print("\n"+"  ".join(display))
  guess=input("Guess a letter: ").lower()
 
  if guess in history:
         print(f"You have already used the letter {guess}")
         continue
  history.add(guess)

  if guess in chosen_Word:
    for i in range(len(chosen_Word)):
      if chosen_Word[i]== guess:
        display[i]=guess
    print("correct")
      
  else:
      lives -= 1
      print(f"wrong guess! lives left:{lives}")

if "_" not in display:
    print("Congratulations you have won! The word is:",chosen_Word)
else:
    print("You lost it . The word was",chosen_Word)