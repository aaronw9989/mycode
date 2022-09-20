#!/usr/bin/env python3

"""Animal list challenge"""


def main():

    # create a list of animals
    animals = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]

    # print the list of animals
    print(f'A list of animals: {animals} \n')

    # function to display animals
    def display_animals(): 
        # print out one animal on each line
        for count, animal in enumerate (animals):
            print(f'Animal Number: {count} Name: {animal}')

    print()
    print("Unsorted Animals List\n")
    # display the unsorted animals list
    display_animals()

    # sort our list of animals
    animals.sort()

    print()
    print("Sorted Animals List\n")

    # display the sorted list of animals
    display_animals()

    print("\nKeep the change ya filthy animal.")

if __name__ == "__main__":
    main()

