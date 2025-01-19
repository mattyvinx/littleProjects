import random #random to be used in game
print("Welcome to rock, paper, scissors.") #greet user
choice = '' #set choice in variable below
while choice != 'y' and choice != 'n': 
    choice = input("Do you know how to play? Enter 'y' or 'n' : ") #ask user if they know how to play.
    if choice != 'y' and choice != 'n':
        print("Invalid choice. Please enter 'y' or 'n'. ") #repeat if invalid input
    if choice == 'n':
        print("Game Rules: ")
        print("Scissors beats paper.")
        print("Paper beats rock.")
        print("Rock beats scissors.")
        print("You will play the computer. The computer will keep track of score.\nThe player with most points wins")
        print("When it is your turn, enter 's' for scissors, 'r' for rock, or 'p' for paper.")

def moveMade(playerMove, compMove):
    #players make same move
    if playerMove == compMove:
        print("Tie!")
        return 0
    #player rock, computer scissor
    if playerMove == 'r' and compMove =='s':
        print("Rock beats scissors! Player wins.")
        return 1
    #player rock, computer paper
    if playerMove == 'r' and compMove =='p':
        print("Paper beats rock! Computer wins.")
        return 2
    #player scissor, computer rock
    if playerMove == 's' and compMove =='r':
        print("Rock beats scissors! Computer wins.")
        return 2
    #player scissor, computer paper
    if playerMove == 's' and compMove =='p':
        print("Scissors beat paper! Player wins.")
        return 1
    #player paper, computer scissor
    if playerMove == 'p' and compMove =='s':
        print("Scissors beat paper! Computer wins.")
        return 2
    #player paper, computer rock
    if playerMove == 'p' and compMove =='r':
        print("Paper beats rock! Player wins.")
        return 1
    else:
        return 3


playing = 'y' #start game
mapping = { #set up mapping from random choice
    1:"s",
    2:"r",
    3:"p"
}
playerScore = 0
cpScore = 0
while playing!='n': #begin game
    compChoiceInt = random.randint(1,3)
    compChoice= mapping[compChoiceInt]
    playerChoice = ''
    while playerChoice != 's' and playerChoice !='r' and playerChoice !='p':
        playerChoice = input('Enter r, p, or s for rock, paper, or scissors. ')
        if playerChoice != 's' and playerChoice !='r' and playerChoice !='p':
            print("Invalid move.")
    moveWinner = moveMade(playerChoice, compChoice)
    #if player wins
    if moveWinner == 1:
        playerScore+=1
    #if computer wins
    if moveWinner == 2:
        cpScore +=1
    playing = input("Keep playing? Enter n to stop, or anything else to continue. ")

if playerScore > cpScore:
    print("You win!")
elif playerScore< cpScore:
    print("You lose.")
else:
    print("Tie!")

        