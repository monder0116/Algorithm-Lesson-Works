# -*- coding: utf-8 -*-
#!/usr/bin/python

import copy
def findThiefway(coinMatrix):
	newgainmatrix=copy.deepcopy(coinMatrix)
	for x in range(len(newgainmatrix)):
		for y in range(1,len(newgainmatrix[x])):
			newgainmatrix[x][y]=-1
	sonl=len(newgainmatrix)-1
	if newgainmatrix[sonl][0]<newgainmatrix[sonl-1][0]:
		newgainmatrix[sonl][0]=newgainmatrix[sonl-1][0]
	for x in range(0,len(newgainmatrix)):

		for y in range(1,len(newgainmatrix[x])):
			rightup=coinMatrix[x-1][y] if x-1>=0 else coinMatrix[x][y]
		#	rightdown=coinMatrix[x+1][y] if x+1<len(coinMatrix[x]) else coinMatrix[x][y]
			right=coinMatrix[x][y]
			tempmax=max(right,rightup)

			#print("right",right,"rightup",rightup)
			print("tempmax",tempmax)
			if x-1>=0 and tempmax==newgainmatrix[x-1][y]==rightup :
				j=y
				while j<len(newgainmatrix[x-1]):
					print("kopyalandı")
					newgainmatrix[x][j]=newgainmatrix[x-1][j]
					j=j+1
			else:
				newgainmatrix[x][y]=tempmax
		print("-----")
	print(newgainmatrix)

amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
findThiefway(amountOfMoneyInLand)