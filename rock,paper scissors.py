import random
howmanygoes = int(input("How many goes would you like to do.(6 or more)"))
computer_choice = "paper"
i = 0
#0 is for computer's point 1 is for human points 2 is for a draw
totalpoints = [0,0,0]
human_last_choice = ""
human_last_choice2 = ""
human_last_choice3 = ""
for i in range(howmanygoes):
  human_choice = str(input("ROCK OR PAPER OR SCISSORS"))
  human_choice = human_choice.lower()
  #Draw
  if human_choice == 'rock' and computer_choice == 'rock' or human_choice == 'paper' and computer_choice == 'paper' or human_choice == 'scissors' and computer_choice == 'scissors':
      print("It is a draw!\n")
      totalpoints[2] = totalpoints[2] + 1
  #Computer wins
  if human_choice == 'rock' and computer_choice == 'paper' or human_choice == 'paper' and computer_choice == 'scissors' or human_choice == 'scissors' and computer_choice == 'rock':
      print("The computer won the round!\n")
      totalpoints[0] = totalpoints[0] + 1
  #Human wins
  if human_choice == 'paper' and computer_choice == 'rock' or human_choice == 'rock' and computer_choice == 'scissors' or human_choice == "scissors" and computer_choice == 'paper':
     print("You won the round!\n")
     totalpoints[1] = totalpoints[1] + 1
  #Incorrect choice
  if human_choice != "paper" and human_choice != "scissors" and human_choice != "rock":
      print("You can only choose something from : ROCK PAPER OR SCISSORS")
  #Computer Choosing
  human_last_choice3 = human_last_choice2
  human_last_choice2 = human_last_choice
  human_last_choice = human_choice
  if human_choice == human_last_choice2 and human_last_choice3:
    if human_last_choice == "rock":
      computer_choice = "paper"
    elif human_last_choice == "paper":
      computer_choice = "scissors"
    elif human_last_choice == "scissors":
      computer_choice =  "rock"
  else:
    computer_choice = random.choice(("rock", "scissors", "paper"))


print ("The stats: computer's points:",totalpoints[0],".Your points:",totalpoints[1],".You drew",totalpoints[2],"times!")
if totalpoints[0] == totalpoints[1]:
  print ("You drew with the computer")
elif totalpoints[0] > totalpoints[1]:
  print ("The computer won")
else:
  print ("You won")
