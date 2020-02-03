
# -*- coding: utf-8 -*-
#!/usr/bin/python


def printdecent(lenght):
	five=""
	three=""
	for i in reversed(range(lenght+1)):
		k=lenght-i
		print(i)
		if (i*3)%5==0 and (k*5)%3==0 :
			for x in range(k):
				five=five+"5"
			for y in range(i):
				three=three+"3"
			break	

	print(five+three)
	
printdecent(6)