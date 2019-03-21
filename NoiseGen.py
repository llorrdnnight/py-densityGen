import random
import math
import time
import numpy as np

field = []
rows = 0
colums = 0
#emptyLine = ["-"] * 10

#Create the noisefield
def generateField(rows_p, colums_p):
	rows = rows_p
	colums = colums_p
	emptyRow = ["-"] * colums
	for x in range(rows-1):
		field.append(emptyRow)

def printField():
    print(np.matrix(field))

def testField():
	x = 10
	x ++
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
	for i in range(rows):
		for j in range(colums):
			chance = random.randomint(1,100)
			if chance < 6:
				#add weigth
				field[i][j] = 100
			else:
				field[i][j] = "+"




#The actual runtime
testField()
