import random

def get_choices():
  player_choice = input("Enter a choice (rock , paper , scissor) :")
  computer_choice = random.choice(['rock' , 'paper' , 'scissor'])

  choices = {"player" : player_choice , "computer" : computer_choice}

  return choices

def check_win(player , computer):
  # print("You choose " + player + ", computer choose " + computer)
  print(f"You choose {player} and the computer choose {computer}")
  if(player == computer):
    return "It's a tie!"
  
  if((player == "rock" and computer == "scissor") or (player == "paper" and computer == "rock") or (player == "scissor" and computer == "paper")) :
    return "Player wins"
  else :
    return "Computer wins"

choices = get_choices()
result = check_win(choices['player'] , choices['computer'])

print(result)