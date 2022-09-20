#!/usr/bin/env python3

import random

def main(): 
    
    # Part 1
    wordbank = ["indentation", "spaces"]

    # Part 2
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # Part 3
    wordbank.append(4)

    # Part 4
    num = int(input("\nEnter a number between 0 and 18: "))

    #print(f'Wordbank: {wordbank}')

    # Part 5
    student_name = tlgstudents[num]

    # print(f'Student name: {student_name}')

    # Part 6
    print(f'\n{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.')

    # Super bonus - random student
    ran_student = random.choice(tlgstudents)

    print(f'\nRandom student {ran_student} always uses {wordbank[2]} {wordbank[1]} to indent.')

    # Mega bonus
    third_student_input = input("\nEnter a name or number between 0 and 18: ")

    if third_student_input.isnumeric():
        student_num = int(third_student_input)
        print(f'\nStudent {tlgstudents[student_num]} always uses {wordbank[2]} {wordbank[1]} to indent.')
    else: 
        print(f'\nStudent {third_student_input} always uses {wordbank[2]} {wordbank[1]} to indent.')



if __name__ == "__main__":
    main()
