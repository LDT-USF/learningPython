#!/usr/bin/python3

import fileinput

for line in fileinput.input():
     field = line.split(',')


     print(field[1])
     date = list(field[1])
     print(date[2])

fileinput.close()
