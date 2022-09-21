#!/usr/bin/env python3

import shutil
import os

def main():
    
    # move into the working directory
    os.chdir('/home/student/mycode/')

    # copy fileA to fileB
    shutil.move('raynor.obj', 'ceph_storage/')

    




if __name__ == "__main__":
    main()
