#!/usr/bin/python

myFile = open('in.dat', 'w')

myVarArray = ["Never", "go", "anywhere", "without", "your", "towel"]

for i in myVarArray:
     myFile.write(i)

myFile.close()
