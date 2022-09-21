#!/usr/bin/env python3
""" A simple script to move files into ceph_storage """


import shutil
import os

def main():
    
    # move into the working directory
    os.chdir('/home/student/mycode/')

    # copy fileA to fileB
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt user for a new name for the kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj? ')

    # rename the current kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


# this calls our main function
if __name__ == "__main__":
    main()
