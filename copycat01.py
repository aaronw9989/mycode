#!/usr/bin/env python3
""" Copy files and folder using os and shutil"""

# shutil tools helps us move around files and folders 
import shutil
# os module lets us use the operating system
import os


def main():

    # move into the working directory
    os.chdir("/home/student/mycode/")

    # copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # remove the existing backup file
    # copy the entire diectoryA to directoryB
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")


if __name__ == "__main__":
    main()
