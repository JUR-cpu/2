import random
options = ["rock", "paper", "scissors", "lizard", "spock"]
while True:
    CPU = random.choice(options)
    entrance = input("Let's play rock, paper, scissors, lizard, spock! Choose your option: ").lower()
    if entrance == "rock":
        if entrance == CPU:
            print("I chose Rock too :O!")
            print("It's a tie! Let's play again!")
        elif CPU == "lizard" or CPU == "scissors":
            if CPU == "lizard":
                print("I chose lizard :c!")
            else:
                print("I chose scissors :c!")
            print("You win! Congratulations!")
        elif CPU == "paper" or CPU == "spock":
            if CPU == "paper":
                print("I chose Paper :D!")
            else:
                print("I chose spock :D!")
            print("Shame, you lost! Try again!") 

    elif entrance == "paper":
        if entrance == CPU:
            print("I chose Paper too :O!")
            print("It's a tie! Let's play again!")
        elif CPU == "rock" or CPU == "spock":
            if CPU == "rock":
                print("I chose Rock :c!")
            else:
                print("I chose spock :c!")
            print("You win! Congratulations!")
        elif CPU == "lizard" or CPU == "scissors":
            if CPU == "lizard":
                print("I chose Lizard :D!")
            else:
                print("I chose scissors :D!")
            print("Shame, you lost! Try again!")

    elif entrance == "scissors":
        if entrance == CPU:
            print("I chose Scissors too :O!")
            print("It's a tie! Let's play again!")
        elif CPU == "paper" or CPU == "Lizard":
            if CPU == "paper":
                print("I chose Paper :c!")
            else:
                print("I chose Lizard :c!")
            print("You win! Congratulations!")
        elif CPU == "spock" or CPU == "rock":
            if CPU == "rock":
                print("I chose Rock :D!")
            else:
                print("I chose spock :D!")
            print("Shame, you lost! Try again!")

    elif entrance == "spock":
        if entrance == CPU:
            print("I chose Spock too :O!")
            print("It's a tie! Let's play again!")
        elif CPU == "Rock" or CPU == "Scissors":
            if CPU == "Rock":
                print("I chose Rock :c!")
            else:
                print("I chose Scissors :c!")
            print("You win! Congratulations!")
        elif CPU == "lizard" or CPU == "paper":
            if CPU == "lizard":
                print("I chose Lizard :D!")
            else:
                print("I chose paper :D!")
            print("Shame, you lost! Try again!")

    elif entrance == "lizard":
        if entrance == CPU:
            print("I chose Lizard too :O!")
            print("It's a tie! Let's play again!")
        elif CPU == "paper" or CPU == "spock":
            if CPU == "paper":
                print("I chose Paper :c!")
            else:
                print("I chose spock :c!")
            print("You win! Congratulations!")
        elif CPU == "rock" or CPU == "scissors":
            if CPU == "rock":
                print("I chose Rock :D!")
            else:
                print("I chose scissors :D!")
            print("Shame, you lost! Try again!")

    else:
        print("That's not part of the game :/")

    retry = input("Want to play again? ")
    if retry.lower() == "no":
        print("Understandable, have a great day :D!")
        break