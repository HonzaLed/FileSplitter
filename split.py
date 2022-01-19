#!/bin/python3

import os
import sys

try:
    splitSize = sys.argv[1]
except:
    splitSize = "980"

dir = os.path.join(os.getcwd(), "source")

print("Trying to use directory",dir)

if not os.path.exists(dir):
    print("Directory not found, exiting...")
    exit(1)

print("Using directory",dir)

os.system("mkdir -p splitted")

files = os.listdir(dir)

print("Found files:")

[print(i,end="  ") for i in files]
print("")

confirm = input("Confirm splitting (Y/n): ")
if confirm.lower() != "y":
    print("OK, exiting...")
    exit(0)
print("Starting splitting files!")

os.chdir(dir)
#print("[DEBUG]",os.getcwd())

for i in files:
    print("Proccessing file", i)
    cmd = "split -b "+splitSize+"M "+i+" "+os.path.join( os.path.join( os.path.join( os.getcwd(), ".."), "splitted"), i+".")
    #print("[DEBUG]",cmd)
    os.system(cmd)

print("Splitting completed!")
