import random

print("Welcome to Rock Paper Scissors!")
print("-------------------------------------------")

##set up variables

cpuScore = 0
playerScore = 0
tieScore = 0

possibleHands = ["Rock","Paper","Scissors"]
#playing = True

#while playing:

   # player = None
   # computer = random.choice(options)

    #while player not in options:
      #player = input("Enter a choice (rock,paper,scissors):")

   # print(f"Player: {player}")
   # print(f"Computer:{computer}")

def checkForWinner(playerHand,computerHand):
    if playerHand == computerHand:
        print("It's a tie, play again!")
        return "Tie"
    elif playerHand == "Rock" and computerHand == "Scissors":
        print("Congrats! You Win:")
        return "Player"
    elif playerHand == "Paper" and computerHand == "Rock":
        print("Congrats! You Win:")
        return "Player"
    elif playerHand == "Scissors" and computerHand == "Paper":
        print("Congrats! You Win:")
        return "Player"
    else:
        print("Sorry, You lose!")
        return "Cpu"


while(playerScore != 3 and cpuScore != 3):
      while True:
         playerHand = input("\nPick a hand. Rock, Paper, Scissors: ")
         if(playerHand == "Rock" or playerHand == "Paper" or playerHand == "Scissors"):
           break
         else:
             print("Invalid input try again.")


      computerHand = random.choice(possibleHands)

      print("Player: ", playerHand )
      print("Computer: ", computerHand)
      result = checkForWinner(playerHand, computerHand)
      if(result == "Player"):
          playerScore += 1
      elif(result == "Cpu"):
          cpuScore += 1
      else:
          tieScore += 1

      print("Your score:",playerScore,
             "Cpu:",cpuScore,
             "Ties:",tieScore)



print("Game over! Thank you ----")






