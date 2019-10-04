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
    for x in range(rows-1):
        emptyRow = ["-"] * colums
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

#Init first anchors of world
'''
    We run over the field, for each position we make a check, if the check applies
'''
def init_world_anchors():
    global rows, colums
    for i in range(rows-1):
        for j in range(colums):
            chance = random.randint(1,100)
            if chance < 11:
                field[i][j] = 100
            else:
                field[i][j] = "+"
#Init nth level promotions
'''
    We run over the field locate a world anchor,
    evaluate the hexes near it and give it a slight chance to promote.
    A promoted hex will be of a lower evaluate
    Each promoted hex will then again have a low chance to spawn lesser promotions
'''

#The actual runtime
testField()
