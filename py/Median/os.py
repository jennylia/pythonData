#!/usr/bin/env python

import os

def get_filepaths(directory):

    for root, dirs, files in os.walk(directory):
        for name in files:
            print("name of file : " + os.path.join(root,name))
            f = open(os.path.join(root,name), 'r')
            for line in f:
                print(line)
            f.close
print get_filepaths(".")
