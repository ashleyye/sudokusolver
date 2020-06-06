import os
import tkinter
from tkinter import *
from tkinter import messagebox

sudokuBoard = [[[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
              [[0], [0], [0], [0], [0], [0], [0], [0], [0]]]
def reset():
   for i in range(0, 9):
       for j in range(0,9):
           if len(sudokuBoard[i][j]) < 1:
               sudokuBoard[i][j].append(0)
           elif len(sudokuBoard[i][j]) > 1:
               for k in range(0, len(sudokuBoard[i][j]) - 1):
                   sudokuBoard[i][j].pop()



def inputSudoku(s):
   reset()
   for i in range(0, 9):
       j = 0
       while j < 9:
           x = s.read(1)
           if x != '\n':
               sudokuBoard[i][j][0] = int(x)
               j += 1



def display(s):
   s.write("\n")
   s.write("Sudoku solution:")
   for i in sudokuBoard:
       s.write("\n")
       s.write(str(i))


def solved():
   s = True
   for i in range(0, 9):
       for j in range(0, 9):
           if len(sudokuBoard[i][j]) != 1:
               s = False
   return s


def rowValueCheck(row, value):
   found = False
   for i in range(0, 9):
       if row[i][0] == value and len(row[i]) == 1:
           found = True
   return found


def columnValueCheck(columnNum, value):
   found = False
   for i in range(0, 9):
       if sudokuBoard[i][columnNum][0] == value and len(sudokuBoard[i][columnNum]) == 1:
           found = True
   return found


def boxValueCheck(rowNum, columnNum, value):
   found = False
   if 0 <= rowNum < 3:
       if 0 <= columnNum < 3:
           for i in range(0, 3):
               for j in range(0, 3):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
       if 3 <= columnNum < 6:
           for i in range(0, 3):
               for j in range(3, 6):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
       if 6 <= columnNum < 9:
           for i in range(0, 3):
               for j in range(6, 9):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
   if 3 <= rowNum < 6:
       if 0 <= columnNum < 3:
           for i in range(3, 6):
               for j in range(0, 3):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
       if 3 <= columnNum < 6:
           for i in range(3, 6):
               for j in range(3, 6):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
       if 6 <= columnNum < 9:
           for i in range(3, 6):
               for j in range(6, 9):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
   if 6 <= rowNum < 9:
       if 0 <= columnNum < 3:
           for i in range(6, 9):
               for j in range(0, 3):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
       if 3 <= columnNum < 6:
           for i in range(6, 9):
               for j in range(3, 6):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
       if 6 <= columnNum < 9:
           for i in range(6, 9):
               for j in range(6, 9):
                   if sudokuBoard[i][j][0] == value and len(sudokuBoard[i][j]) == 1:
                       found = True
   return found


# board initialization
def boardInitialization():
   for i in range(0, 9):
       for j in range(0, 9):
           if sudokuBoard[i][j] == [0]:
               for x in range(1, 10):
                   if not rowValueCheck(sudokuBoard[i], x) and not columnValueCheck(j, x) and not boxValueCheck(i, j,
                                                                                                                x):
                       if sudokuBoard[i][j] == [0]:
                           sudokuBoard[i][j].pop()
                       sudokuBoard[i][j].append(x)


def remove(row, column, value):
   for i in range(0, 9):
       for j in range(0, len(sudokuBoard[row][i])):
           if sudokuBoard[row][i][j] == value and i != column:
               sudokuBoard[row][i].pop(j)
               break
   for i in range(0, 9):
       for j in range(0, len(sudokuBoard[i][column])):
           if sudokuBoard[i][column][j] == value and i != row:
               sudokuBoard[i][column].pop(j)
               break
   boxRow = (int(row / 3)) * 3
   boxColumn = (int(column / 3)) * 3
   for i in range(boxRow, boxRow + 3):
       for j in range(boxColumn, boxColumn + 3):
           for k in range(0, len(sudokuBoard[i][j])):
               if sudokuBoard[i][j][k] == value and not (i == row and j == column):
                   sudokuBoard[i][j].pop(k)
                   break


def uniqueCandidate():
   uniqueCandidateEdited = True
   while uniqueCandidateEdited:
       uniqueCandidateEdited = False
       # unique candidate (row)
       for x in range(1, 10):
           for i in range(0, 9):
               count = 0
               row = 0
               column = 0
               for j in range(0, 9):
                   for k in range(0, len(sudokuBoard[i][j])):
                       if sudokuBoard[i][j][k] == x:
                           row = i
                           column = j
                           count += 1
               if count == 1:
                   l = 0
                   while l < len(sudokuBoard[row][column]):
                       pop = False
                       if sudokuBoard[row][column][l] != x:
                           sudokuBoard[row][column].pop(l)
                           pop = True
                           uniqueCandidateEdited = True
                       if pop:
                           l = 0
                       else:
                           l += 1
                   remove(row, column, x)

                   # unique candidate (column)
       for x in range(1, 10):
           for j in range(0, 9):
               count = 0
               row = 0
               column = 0
               for i in range(0, 9):
                   for k in range(0, len(sudokuBoard[i][j])):
                       if sudokuBoard[i][j][k] == x:
                           row = i
                           column = j
                           count += 1
               if count == 1:
                   l = 0
                   while l < len(sudokuBoard[row][column]):
                       pop = False
                       if sudokuBoard[row][column][l] != x:
                           sudokuBoard[row][column].pop(l)
                           pop = True
                           uniqueCandidateEdited = True
                       if pop:
                           l = 0
                       else:
                           l += 1
                   remove(row, column, x)

    # unique candidate (box)
       boxRow = 0
       boxColumn = 0
       for x in range(1, 10):
           box = 0
           row = 0
           column = 0
           while box < 9:
               count = 0
               boxRow %= 9
               boxColumn %= 9
               for i in range(boxRow, boxRow + 3):
                   boxColumn %= 9
                   for j in range(boxColumn, boxColumn + 3):
                       for k in range(0, len(sudokuBoard[i][j])):
                           if sudokuBoard[i][j][k] == x:
                               row = i
                               column = j
                               count += 1
               if count == 1:
                   l = 0
                   while l < len(sudokuBoard[row][column]):
                       pop = False
                       if sudokuBoard[row][column][l] != x:
                           sudokuBoard[row][column].pop(l)
                           pop = True
                           uniqueCandidateEdited = True
                       if pop:
                           l = 0
                       else:
                           l += 1
                   remove(row, column, x)
               boxColumn += 3
               if boxColumn == 9:
                   boxRow += 3
               box += 1


def withinBlock():
   interactionEdited = True
   while interactionEdited:
       interactionEdited = False
       for x in range(1, 10):
           for i in range(0, 9):
               column = []
               for j in range(0,9):
                   for k in range(0,len(sudokuBoard[i][j])):
                       if sudokuBoard[i][j][k] == x:
                           column.append(j)
               if 0 < len(column) <= 3:
                   if 0 <= i < 3:
                       if column[0] >= 0 and column[-1] <= 2:
                           for j in range(0, 3):
                               if j != i:
                                   for k in range(0,3):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif column[0] >= 3 and column[-1] <= 5:
                           for j in range(0, 3):
                               if j != i:
                                   for k in range(3, 6):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif column[0] >= 6 and column[-1] <= 8:
                           for j in range(0, 3):
                               if j != i:
                                   for k in range(6, 8):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                   elif 3 <= i < 5:
                       if column[0] >= 0 and column[-1] <= 2:
                           for j in range(3, 5):
                               if j != i:
                                   for k in range(0,3):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif column[0] >= 3 and column[-1] <= 5:
                           for j in range(3, 5):
                               if j != i:
                                   for k in range(3, 6):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif column[0] >= 6 and column[-1] <= 8:
                           for j in range(3, 5):
                               if j != i:
                                   for k in range(6, 8):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                   elif 6 <= i < 9:
                       if column[0] >= 0 and column[-1] <= 2:
                           for j in range(6, 9):
                               if j != i:
                                   for k in range(0,3):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif column[0] >= 3 and column[-1] <= 5:
                           for j in range(6, 9):
                               if j != i:
                                   for k in range(3, 6):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif column[0] >= 6 and column[-1] <= 8:
                           for j in range(6, 9):
                               if j != i:
                                   for k in range(6, 8):
                                       l = 0
                                       while l < len(sudokuBoard[j][k]):
                                           if sudokuBoard[j][k][l] == x:
                                               sudokuBoard[j][k].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
           for i in range(0, 9):
               row = []
               for j in range(0,9):
                   for k in range(0,len(sudokuBoard[j][i])):
                       if sudokuBoard[j][i][k] == x:
                           row.append(j)
               if 0 < len(row) <= 3:
                   if 0 <= i < 3:
                       if row[0] >= 0 and row[-1] <= 2:
                           for j in range(0, 3):
                               if j != i:
                                   for k in range(0,3):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif row[0] >= 3 and row[-1] <= 5:
                           for j in range(0, 3):
                               if j != i:
                                   for k in range(3, 6):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif row[0] >= 6 and row[-1] <= 8:
                           for j in range(0, 3):
                               if j != i:
                                   for k in range(6, 9):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                   elif 3 <= i < 5:
                       if row[0] >= 0 and row[-1] <= 2:
                           for j in range(3, 6):
                               if j != i:
                                   for k in range(0,3):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif row[0] >= 3 and row[-1] <= 5:
                           for j in range(3, 6):
                               if j != i:
                                   for k in range(3, 6):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif row[0] >= 6 and row[-1] <= 8:
                           for j in range(3, 6):
                               if j != i:
                                   for k in range(6, 9):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                   elif 6 <= i < 9:
                       if row[0] >= 0 and row[-1] <= 2:
                           for j in range(6, 9):
                               if j != i:
                                   for k in range(0,3):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif row[0] >= 3 and row[-1] <= 5:
                           for j in range(6, 9):
                               if j != i:
                                   for k in range(3, 6):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1
                       elif row[0] >= 6 and row[-1] <= 8:
                           for j in range(6, 9):
                               if j != i:
                                   for k in range(6, 9):
                                       l = 0
                                       while l < len(sudokuBoard[k][j]):
                                           if sudokuBoard[k][j][l] == x:
                                               sudokuBoard[k][j].pop(l)
                                               interactionEdited = True
                                               l = -1
                                           l += 1


def valueFound(values, new):
   for i in values:
       if i == new:
           return False
   return True


def nestedSubset(arr1, arr2):
   for i in arr2:
       if valueFound(arr1, i):
           return False
   return True

def nakedSubset():
   subsetEdited = True
   while subsetEdited:
       for length in range(2, 4):
           subsetEdited = False
           for i in range(0, 9):
               values = []
               column = []
               temp = []
               finalColumn = []
               for j in range(0,9):
                   if length == 2:
                       if len(sudokuBoard[i][j]) == length:
                           values.append(sudokuBoard[i][j])
                           column.append(j)
                   elif length == 3:
                       if len(sudokuBoard[i][j]) == length or len(sudokuBoard[i][j]) == length - 1:
                           values.append(sudokuBoard[i][j])
                           column.append(j)
               if len(values) >= length:
                   if length == 2:
                       for j in range(0, len(values)):
                           for k in (j + 1, len(values)):
                               if k < len(values):
                                   if sorted(values[j]) == sorted(values[k]):
                                       temp.append(values[j])
                                       finalColumn.append(column[j])
                                       finalColumn.append(column[k])
                       for j in range(0, 9):
                           for l in temp:
                               k = 0
                               while k < len(sudokuBoard[i][j]):
                                   if not valueFound(l, sudokuBoard[i][j][k]) and valueFound(finalColumn, j):
                                       sudokuBoard[i][j].pop(k)
                                       k = -1
                                       subsetEdited = True
                                   k += 1
                   if length == 3:
                       j = 0
                       while j < len(values):
                           k = j + 1
                           while k < len(values):
                               l = k + 1
                               while l < len(values):
                                   if nestedSubset(values[j], values[k]) and nestedSubset(values[j],values[l]):
                                       temp.append(values[j])
                                       finalColumn.append(column[j])
                                       finalColumn.append(column[k])
                                       finalColumn.append(column[l])
                                   elif nestedSubset(values[k], values[j]) and nestedSubset(values[k], values[l]):
                                       temp.append(values[k])
                                       finalColumn.append(column[j])
                                       finalColumn.append(column[k])
                                       finalColumn.append(column[l])
                                   elif nestedSubset(values[l], values[j]) and nestedSubset(values[l], values[k]):
                                       temp.append(values[l])
                                       finalColumn.append(column[j])
                                       finalColumn.append(column[k])
                                       finalColumn.append(column[l])
                                   l += 1
                               k += 1
                           j += 1
                       for j in range(0, 9):
                           for l in temp:
                               k = 0
                               while k < len(sudokuBoard[i][j]):
                                   if not valueFound(l, sudokuBoard[i][j][k]) and valueFound(finalColumn, j):
                                       sudokuBoard[i][j].pop(k)
                                       k = -1
                                       subsetEdited = True
                                   k += 1
           for i in range(0, 9):
               values = []
               row = []
               temp = []
               finalRow = []
               for j in range(0,9):
                   if length == 2:
                       if len(sudokuBoard[j][i]) == length:
                           values.append(sudokuBoard[j][i])
                           row.append(j)
                   elif length == 3:
                       if len(sudokuBoard[j][i]) == length or len(sudokuBoard[j][i]) == length - 1:
                           values.append(sudokuBoard[j][i])
                           row.append(j)
               if len(values) >= length:
                   if length == 2:
                       for j in range(0, len(values)):
                           for k in (j + 1, len(values)):
                               if k < len(values):
                                   if sorted(values[j]) == sorted(values[k]):
                                       temp.append(values[j])
                                       finalRow.append(row[j])
                                       finalRow.append(row[k])
                       for j in range(0, 9):
                           for l in temp:
                               k = 0
                               while k < len(sudokuBoard[j][i]):
                                   if not valueFound(l, sudokuBoard[j][i][k]) and valueFound(finalRow, j):
                                       sudokuBoard[j][i].pop(k)
                                       k = -1
                                       subsetEdited = True
                                   k += 1
                   if length == 3:
                       j = 0
                       while j < len(values):
                           k = j + 1
                           while k < len(values):
                               l = k + 1
                               while l < len(values):
                                   if nestedSubset(values[j], values[k]) and nestedSubset(values[j],values[l]):
                                       temp.append(values[j])
                                       finalRow.append(row[j])
                                       finalRow.append(row[k])
                                       finalRow.append(row[l])
                                   elif nestedSubset(values[k], values[j]) and nestedSubset(values[k],values[l]):
                                       temp.append(values[k])
                                       finalRow.append(row[j])
                                       finalRow.append(row[k])
                                       finalRow.append(row[l])
                                   elif nestedSubset(values[l], values[j]) and nestedSubset(values[l], values[k]):
                                       temp.append(values[l])
                                       finalRow.append(row[j])
                                       finalRow.append(row[k])
                                       finalRow.append(row[l])
                                   l += 1
                               k += 1
                           j += 1
                       for j in range(0, 9):
                           for l in temp:
                               k = 0
                               while k < len(sudokuBoard[j][i]):
                                   if not valueFound(l, sudokuBoard[j][i][k]) and valueFound(finalRow, j):
                                       sudokuBoard[j][i].pop(k)
                                       k = -1
                                       subsetEdited = True
                                   k += 1
           box = 0
           boxRow = 0
           boxColumn = 0
           while box < 9:
               values = []
               coordinates = []
               temp = []
               finalCoordinates = []
               boxRow %= 9
               boxColumn %= 9
               for i in range(boxRow, boxRow + 3):
                   boxColumn %= 9
                   for j in range(boxColumn, boxColumn + 3):
                       if length == 2:
                           if len(sudokuBoard[j][i]) == length:
                               if valueFound(values, sudokuBoard[i][j]):
                                   values.append(sudokuBoard[i][j])
                                   coordinates.append([i, j])
                       elif length == 3:
                           if len(sudokuBoard[j][i]) == length or len(sudokuBoard[j][i]) == length - 1:
                               if valueFound(values, sudokuBoard[i][j]):
                                   values.append(sudokuBoard[i][j])
                                   coordinates.append([i, j])
               if len(values) >= length:
                   if length == 2:
                       for j in range(0, len(values)):
                           for k in (j + 1, len(values)):
                               if k < len(values):
                                   if sorted(values[j]) == sorted(values[k]):
                                       temp.append(values[j])
                                       finalCoordinates.append(coordinates[j])
                                       finalCoordinates.append(coordinates[k])
                       for i in range(boxRow, boxRow + 3):
                           boxColumn %= 9
                           for j in range(boxColumn, boxColumn + 3):
                               for l in temp:
                                   k = 0
                                   while k < len(sudokuBoard[i][j]):
                                       if not valueFound(l, sudokuBoard[i][j][k]) and valueFound(finalCoordinates, [i, j]):
                                           sudokuBoard[i][j].pop(k)
                                           k = -1
                                           subsetEdited = True
                                       k += 1
                   if length == 3:
                       j = 0
                       while j < len(values):
                           k = j + 1
                           while k < len(values):
                               l = k + 1
                               while l < len(values):
                                   if nestedSubset(values[j], values[k]) and nestedSubset(values[j],values[l]):
                                       temp.append(values[j])
                                       finalCoordinates.append(coordinates[j])
                                       finalCoordinates.append(coordinates[k])
                                       finalCoordinates.append(coordinates[l])
                                   elif nestedSubset(values[k], values[j]) and nestedSubset(values[k],values[l]):
                                       temp.append(values[k])
                                       finalCoordinates.append(coordinates[j])
                                       finalCoordinates.append(coordinates[k])
                                       finalCoordinates.append(coordinates[l])
                                   elif nestedSubset(values[l], values[j]) and nestedSubset(values[l], values[k]):
                                       temp.append(values[l])
                                       finalCoordinates.append(coordinates[j])
                                       finalCoordinates.append(coordinates[k])
                                       finalCoordinates.append(coordinates[l])
                                   l += 1
                               k += 1
                           j += 1
                       for i in range(boxRow, boxRow + 3):
                           boxColumn %= 9
                           for j in range(boxColumn, boxColumn + 3):
                               for l in temp:
                                   k = 0
                                   while k < len(sudokuBoard[i][j]):
                                       if not valueFound(l, sudokuBoard[i][j][k]) and valueFound(finalRow, j):
                                           sudokuBoard[i][j].pop(k)
                                           k = -1
                                           subsetEdited = True
                                       k += 1
               boxColumn += 3
               if boxColumn == 9:
                   boxRow += 3
               box += 1


def algorithms(f):
   c = 0
   n = 0
   while not solved() and n < 3:
       if n == 0:
           uniqueCandidate()
           c += 1
           n = c
       elif n == 1:
           nakedSubset()
           n -= 1
       elif n == 2:
           withinBlock()
           n -= 1
   if solved():
       display(f)
       return ("Solvable")
   else:
       return("Unsolvable")

def solutions():
   s = []
   for root, dirs, files in os.walk("C:/Users/ashle/PycharmProjects/" + E2.get()):
       for file in files:
           if file.endswith('.txt'):
               with open(os.path.join(root, file), 'r+') as f:
                   inputSudoku(f)
                   boardInitialization()
                   s.append(algorithms(f))
   if len(s) == 0:
       messagebox.showinfo("Sudoku solutions ", "No files found")
   else:
       if len(s) > int(E1.get()):
           for i in range(0, len(s) - int(E1.get())):
               s.pop()
       messagebox.showinfo("Sudoku solutions ", s)


# main method starts HERE
top = tkinter.Tk()
L1 = Label(top, text="Number of Sudokus:").grid(row=0)
E1 = tkinter.Entry(top)
E1.grid(row=0, column=1)
L2 = Label(top, text="Folder name:").grid(row=1)
E2 = tkinter.Entry(top)
E2.grid(row=1, column=1)

B = tkinter.Button(top, text ="Solve", command = lambda: solutions()).grid(row=3, column=0)

top.mainloop()