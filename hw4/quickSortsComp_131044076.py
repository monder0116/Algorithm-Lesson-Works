# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
-İki algoritmanin karmaşıklığıda O(n) dir.
-Lomuto Partition listeyi 4 kısma böler. Bunlar pivot,pivottan küçük ve pivottan büyük  ve belirsiz kısım
şeklindedir
-Hoare Partion da ise liste pivottan küçük ve büyük olmak üzere 2 kısıma ayrılır.
- Swaping işlemleri Hoare Part.'a göre Lomuto part. 3 kat daha yüksektir.
- Compariton işlemleri iki yöntemde de n-1 karşılaştırma yapmaktadır.
- Sıralı bir liste verildiğinde Lomuto partition O(n^2) kadar çıkarken,
Hoare partition O(nlogn) dir.
-Lomuto part. Hoare Part. e göre daha kolay implement edilebilmektedir.


Not:Algoritmaların implemantationları yapılırken ders defteri ve geeksforgeeks.org sitelerinden
yararlanıldı.
'''


def LomutoPartition(arr,low,high):
	pivot = arr[high]
	i = low - 1
	for j in range(low,high-1):
     
		if arr[j] <= pivot:
     
			i=i+1  
			arr[i],arr[j]=arr[j],arr[i]
        
 
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return i+1


def HoarePartiton(arr,low,high):
	right = low-1
	left = high+1	
	pivot=arr[low]
	while right<left:
		while 1:
			right=right+1
			if arr[right]>= pivot:
				break
		while 1:
			left=left-1
			if arr[left]<=pivot:
				break	
		if right<=left:
			arr[left],arr[right]=arr[right],arr[left]
	position=left
	arr[low]=arr[position]
	arr[position]=pivot
	return position
def quickSort(arr, low,  high):
	if low < high:
   		pos= HoarePartiton(arr,low,high)
   		print(pos)
		quickSort(arr, low, pos);
		quickSort(arr, pos+1 , high);
	return arr
  
liste=[4,52,46,72,1]
print(quickSort(liste,0,len(liste)-1))