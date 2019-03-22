import random
import math
import time
import numpy as np

field = []
global rows, colums
rows = 0
colums = 0

#Create the noisefield
def generateField(rows_p, colums_p):
    global rows, colums
    rows = rows_p
    colums = colums_p
    emptyRow = ["-"] * colums
    for x in range(rows-1):
        field.append(emptyRow)

def printField():
    print(np.matrix(field))

def testField():
    x = 10
    x = x+1
    y = 15
    generateField(x, y)
    init_world_anchors()
    printField()
    time.sleep(20)

#Init first achors of world
'''
    We run over the field, for each position we make a check, if the check applies
'''
def init_world_anchors():
    global rows, colums
    for i in range(rows-1):
        for j in range(colums):
            chance = random.randint(1,100)
            time.sleep(0.01)
            if chance < 11:
                field[i][j] = 100
            else:
                field[i][j] = "+"
            print(chance)
            print(field[i][j])

#The actual runtime
testField()
