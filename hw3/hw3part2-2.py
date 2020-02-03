# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
	

def permutation(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    resultlist = [] 
    for i in range(len(arr)):
       temp = arr[i]
       newlist = list(arr[i+1:])
       newlist.extend(arr[:i])
       recurlist=permutation(newlist)
       for p in recurlist:
           newlist=[temp]
           newlist.extend(p)
           resultlist.append(newlist)
    return resultlist
 
def createlistofperms(array):
	liste=permutation(range(len(array)))
	return liste
	

def permcontex(arr):
  if len(arr[0])>len(arr):
    return []
  permutasyonlar=createlistofperms(arr)
  yeniperms=[]

  for i in permutasyonlar:
      templist=[]
      for j in i:
          if j<len(arr[0]):
              templist.append(j)
          else:
              templist.append(-1)
      yeniperms.append(templist)
  minsum=sys.maxsize
  minindex=-1
  #herbir permutasyon için
  for i in range(len(yeniperms)):
    tempsum=0
    #herbir asistan için
    for j in range(len(arr)):
        if yeniperms[i][j]!=-1:
             tempsum=tempsum + arr[j][yeniperms[i][j]]
        else:
            tempsum=tempsum+6
    if minsum>tempsum:
        minsum=tempsum
        minindex=i

  return yeniperms[minindex],minsum

array= [[1,8,2], # R.A. 0
[22,3,99], # R.A. 1
[1,33,55],[1,1,11]]
minsum,minlist=permcontex(array)
print("minsum=" +str(minsum))
print("minlist=" + str(minlist))
