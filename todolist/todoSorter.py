#!/usr/bin/python3

import fileinput

todoList = [[]]
counter = 0

for line in fileinput.input():
     field = line.split(',')
     date = list(field[1])
     day = int(date[2]+date[3])
     month = int(date[0]+date[1])
     year = int(date[4]+date[5])

     if(counter > 0):
          todoList.append([])

     todoList[counter].append(int(field[0]))
     todoList[counter].append(day)
     todoList[counter].append(month)
     todoList[counter].append(year)
     todoList[counter].append(field[2].rstrip('\n'))

     counter += 1

fileinput.close()

for i in range(counter):
     print(todoList[i])
