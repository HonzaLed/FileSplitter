#!/bin/python3

import os

def doNothing():
    pass

dir = os.path.join(os.getcwd(), "splitted")

print("Trying to use directory",dir)

if not os.path.exists(dir):
    print("Directory not found, exiting...")
    exit(1)

print("Using directory",dir)

os.system("mkdir -p source")

files = os.listdir(dir)

os.chdir(dir)
#print("[DEBUG]",os.getcwd())

newFiles=[]
[newFiles.append(i[:-2]) if not i[:-2] in newFiles else doNothing() for i in os.listdir()]

print("Found files:")

[print(i[:-1],end="  ") for i in newFiles]
print("")

confirm = input("Confirm combining (Y/n): ")
if confirm.lower() != "y":
    print("OK, exiting...")
    exit(0)
print("Starting combining files!")


for i in newFiles:
    print("Proccessing file", i[:-1])
    cmd = "cat "+i+"?? > "+os.path.join( os.path.join( os.path.join( os.getcwd(), ".."), "source"), i[:-1])
    #print("[DEBUG]",cmd)
    os.system(cmd)

print("Combining completed!")
