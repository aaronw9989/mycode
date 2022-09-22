#!/usr/bin/python3

import os

# count number of vampire
num_vampire = 0 

# remove old vampy times text file
os.system("rm /home/student/mycode/challenge_programs/dracula/vampytimes.txt")

# open the file for reading
with open("/home/student/mycode/challenge_programs/dracula/dracula.txt") as book:

    # loop over file line by line
    for line in book:
        
        #print each line
        #print(line)

        if "vampire" in line or "Vampire" in line:
            print(line)
            num_vampire += 1
            with open("/home/student/mycode/challenge_programs/dracula/vampytimes.txt", "a") as count_file:
                count_file.write(line)

print("The number of times vampire appears: ", num_vampire)

