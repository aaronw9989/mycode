#!/usr/bin/env python3


""" Lab 31 """

def main():
    
    round = 0

    while True:

        round = round + 1

        print('Finish the movie title, "Monty Python\'s The Life of ______"')

        # get the user input
        answer = input("Your guess--> ")

        # check user input
        if answer == 'Brian':
            print('Correct')
            break
        elif round == 3:
            print("Sorry, the answer was Brian.")
            break
        else: 
            print("Sorry! Try again!")








if __name__ == "__main__":
    main()
