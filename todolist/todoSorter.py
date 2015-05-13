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
     for j in range(i, counter):
          if(todoList[i][0] < todoList[j][0]):
               swap = todoList[j]
               todoList[j] = todoList[i]
               todoList[i] = swap
          elif(todoList[i][3] > todoList[j][3]):
               swap = todoList[j]
               todoList[j] = todoList[i]
               todoList[i] = swap
          elif(todoList[i][3] < todoList[j][3]):
               continue
          elif(todoList[i][2] > todoList[j][2]):
               swap = todoList[j]
               todoList[j] = todoList[i]
               todoList[i] = swap
          elif(todoList[i][2] < todoList[j][2]):
               continue
          elif(todoList[i][1] > todoList[j][1]):
               swap = todoList[j]
               todoList[j] = todoList[i]
               todoList[i] = swap
          else:
               continue

#for i in range(counter):
#     print(todoList[i])

FH = open("myTodoList", "w")

for i in range(counter):
     FH.write(str(todoList[i]).strip('[]'))
     FH.write("\n")
FH.close()

