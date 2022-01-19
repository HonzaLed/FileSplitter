#!/bin/python3

import os

os.chdir( os.path.join( os.getcwd(), "splitted"))

print("Starting removing files...")

for i in os.listdir():
    #print("Removing file",i)
    os.remove(i)

print("Completed!")
