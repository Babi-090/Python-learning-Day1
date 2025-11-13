
word=input("Enter a word to guess: ")
guessed_letters=set()
display=["_"]*len(word)
lives=6

while "_" in display and lives>0:
  print("\n"+"  ".join(display))
  guess=input("Guess a letter: ")
  if guess in guessed_letters:
    print("You have already guessed that letter.")
    continue
  guessed_letters.add(guess)
  if guess in word:
    for i in range(len(word)):
      if word[i]== guess:
        display[i]=guess
    print("correct")

  else:
      lives -= 1
      print(f"wrong guess! lives left:{lives}")

if "_" not in display:
  print(f"Congratulations you have won! The word is {word}")
else:
    print(f"You lost it . The word was:{word}")