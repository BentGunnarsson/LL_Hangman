import random
from hangman_sll import LinkedList

def add_to_high_scores(name, score):
    '''Arcade style scoring system, one user can enter multiple scores.'''
    high_sc = open("high_scores.txt","a")
    high_sc.write(name+": "+str(score)+"\n")
    high_sc.close()

def open_word_bank():
    word_b = []
    words = open("words.txt","r")
    for line in words:
        line = line.strip()
        word_b.append(line)
    words.close()
    return word_b

def display_high_scores():
    high_sc = open("high_scores.txt","r")
    for line in high_sc:
        line = line.strip()
        print(line)

def add_word_to_bank(word):
    word_b = open("words.txt","a")
    word_b.write("\n"+word)
    word_b.close()

word_bank = open_word_bank()

play = True
wins = 0
losses = 0
total_score = 0
scores = []
while play == True:

    random_num = random.randint(0,len(word_bank)-1) # getting random index for word_bank
    random_word = word_bank[random_num]

    word_sll = LinkedList() # this is where the magic happens
    for char in random_word:
        word_sll.push_back(char) 
    
    print("Let's play a game of hangman!")
    guesses = int(input("How many wrong guesses are to be allowed? "))
    print("Your word to guess is: ",end = "")
    print(word_sll)
    print("Good luck!")

    already_guessed = []
    score = 100
    while guesses != 0:
        if word_sll.check_win_con():
            print("\nCongratulations! You win.")
            scores.append(score)
            wins += 1
            total_score += score
            break

        print("Amount of guesses left: "+str(guesses))

        while True:
            #runs forever until you guess something original
            guess = input("Your guess: ")
            if guess not in already_guessed:
                already_guessed.append(guess)
                break
            print("Hmm, you already guessed that.")


        if len(guess) > 1:
            if guess == random_word:
                # Allowing to guess whole word
                print("Congratulations! You win.")
                scores.append(score)
                wins += 1
                total_score += score
                break

        checker = word_sll.find(guess)
        if checker:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly :(")
            score -= 10
            guesses -= 1
        
        print("Current score: "+str(score))
        print(word_sll)
    
    if guesses == 0:
        print("Uh oh! You ran out of guesses! Better luck next time!")
        print("The word you were trying to guess was: "+random_word)
        total_score -= 35
        if total_score < 0:
            # Constructive criticism only! No negative scores
            total_score = 0

        scores.append(0)
        losses += 1
    
    print("Current wins: "+str(wins))
    print("Current losses: "+str(losses))
    print("Total score: "+str(total_score))
    print("Previous scores: ",end="")
    print(scores)
    print()

    again = input("Would you like to play again? (y/n) ")

    if again == "n":
        addname = input("Would you like to add your name to the list of high scores? (y/n) ")
        if addname == "y":
            name = input("Enter your name: ")
            add_to_high_scores(name, total_score)
            print("The name "+name+" with the score of "+str(total_score)+" has been added!")

        addword = input("Would you like to make a word contribution to the collection of words? (y/n) ")
        if addword == "y":
            word = input("Enter word: ")
            add_word_to_bank(word)
            print("The word "+word+" has been added to the ever growing list of words. Thanks for the contribution!\n")

        print("Thanks for playing!\n")
        print("High scores:")
        display_high_scores()
        play = False