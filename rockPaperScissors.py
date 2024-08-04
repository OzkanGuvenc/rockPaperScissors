import random

def userInput():
    return str(
        input("Please Make Your Choice:\n1. Rock\n2. Paper\n3. Scissors\nTo quit:'quit'\nChoice Number: "))


opponent = ["Rock", "Paper", "Scissors"]
finish = int(input("How many rounds do you want to play? : "))

playerScore = 0
opponentScore = 0

while playerScore < finish and opponentScore < finish:
    playerInput = userInput()
    if playerInput == 'quit':
        print("Game Over!")
        break

    opponentChoice = random.choice(opponent)

    if playerInput == "1" and opponentChoice == "Scissors":
        print(
            "opponent Choice: " + opponentChoice + "\nYour Choice: " + "Rock" + "\nWinner: Congrats!! You won! Rock, smashes the scissors!")
        playerScore += 1
    elif playerInput == "2" and opponentChoice == "Scissors":
        print(
            "opponent Choice: " + opponentChoice + "\nYour Choice: " + "Paper" + "\nWinner: So sad! opponent won! Scissors, cuts the paper!")
        opponentScore += 1
    elif playerInput == "3" and opponentChoice == "Scissors":
        print("opponent Choice: " + opponentChoice + "\nYour Choice: " + "Scissors" + "\nNo winner: Tie!")
    elif playerInput == "1" and opponentChoice == "Paper":
        print(
            "opponent Choice: " + opponentChoice + "\nYour Choice: " + "Rock" + "\nWinner: So sad! opponent won! Paper, covers the Rock!")
        opponentScore += 1
    elif playerInput == "2" and opponentChoice == "Paper":
        print("opponent Choice: " + opponentChoice + "\nYour Choice: " + "Paper" + "\nNo winner: Tie!")
    elif playerInput == "3" and opponentChoice == "Paper":
        print(
            "opponent Choice: " + opponentChoice + "\nYour Choice: " + "Scissors" + "\nWinner: Congrats! You won! Scissors, cuts the paper!")
        playerScore += 1
    elif playerInput == "1" and opponentChoice == "Rock":
        print("opponent Choice: " + opponentChoice + "\nYour Choice: " + "Rock" + "\nNo winner: Tie!")
    elif playerInput == "2" and opponentChoice == "Rock":
        print(
            "opponent Choice: " + opponentChoice + "\nYour Choice: " + "Paper" + "\nWinner: Congrats! You won! Paper, covers the Rock!")
        playerScore += 1
    elif playerInput == "3" and opponentChoice == "Rock":
        print(
            "opponent Choice: " + opponentChoice + "\nYour Choice: " + "Scissors" + "\nWinner: So sad! opponent won! Rock, smashes the scissors!")
        opponentScore += 1
    else:
        print("Geçersiz seçim!")

    print("Score: You: " + str(playerScore) + " <<>> Opponent: " + str(opponentScore))

if playerScore == finish:
    print("Game Over! Congrats!, YOU WON!")
elif opponentScore == finish:
    print("Game Over! So sad, OPPONENT WON!")
