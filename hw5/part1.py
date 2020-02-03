
# -*- coding: utf-8 -*-
#!/usr/bin/python

def findmax2(ylist):
	totalsum=0
	minnum=1
	lindex=len(ylist)-1
	lastbenefit=abs(ylist[lindex]-ylist[lindex-1])
	newlastbenefit=abs(ylist[lindex-1]-minnum)
	if newlastbenefit>lastbenefit:
		ylist[lindex]=minnum

	beginbenefit=abs(ylist[0]-ylist[1])
	newbeginbenefit=abs(ylist[1]-minnum)
	if newlastbenefit>lastbenefit:
		ylist[0]=minnum

	for i in range(1,len(ylist)-1):
		maxnum=ylist[i]
		if (abs(maxnum-ylist[i-1])+abs(maxnum-ylist[i+1]))<(abs(minnum-ylist[i-1])+abs(minnum-ylist[i+1])):
			print("değişti")
			ylist[i]=minnum
		totalsum=totalsum+abs(ylist[i]-ylist[i-1])
	totalsum=totalsum+abs(ylist[lindex]-ylist[lindex-1])
	print(ylist)
	return totalsum
Y = [50,28,1,1,13,7]
#Y = [14,1,14,1,14]
#Y = [1,9,11,7,3]


def findmax(ylist):
	totalsum=0

	sortedlist=sorted(ylist)
	for i in range(1,len(ylist)):
		j=i

		maxtemp=abs(ylist[i]-ylist[i-1])
		print("i="+ str(i))
		print("maxtemp="+ str(maxtemp))
		while(j>0 ):
			if abs(ylist[j]-ylist[i-1])>maxtemp:
				maxtemp=abs(ylist[j]-ylist[i-1])
				print("maxtemp değişti,j=%0,max=%1 ",str(j),str(maxtemp))
			j=j-1
		j=i
		while(j<len(ylist)):
			if abs(ylist[j]-ylist[i-1])>maxtemp :
				maxtemp=abs(ylist[j]-ylist[i-1])
				print("maxtemp değişti,j=%0,max=%1 ",str(j),str(maxtemp))
			j=j+1
		totalsum=totalsum+maxtemp
		print("tempmax toplama eklendi = %0",totalsum)
	return totalsum

print(findmax2(Y))
