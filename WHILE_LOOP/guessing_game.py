#guessing game

#generating random integer between 1 to 100
import random
jackpot = random.randint(1,100)

guess = int(input("Guess a number:"))
counter = 1
while guess!=jackpot:
  if guess < jackpot:
    print('wrong! guess higher')
  else:
    print('Wrong!guess lower')    

  guess = int(input("Guess a number:"))
  counter += 1
else:
  print('correct guess')    
  print('attempts:',counter)