# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
'''
	Subarray_finder fonksiyonu;
	Divide için;  liste ile birlikte bir index numarası alır.
	bunun sebebi listeyi bir sağa kaydırarak iterative olarak o başlangıç 
	noktasından listenin sonuna kadar olan sub arraylarını bulmaktır. 
	Sağa kaydırılır ve bir döngü içerisinde listenin uzunluğuna kadar 
	indexden başlayıp birer kaydırarak recursive yeni oluşturduğu sublist için
	recur çağrı yapar.Ve bunları kendi içinde bir arrayde tutar. 
	Conqure için ilk önce divide kısımda recursive ile gönderilen subarrayın sonucunu minsum 
	ve minliste atama yapar ardından divide kısımda tuttuğu array içindeki tüm elemanları gezer
	ve dahada küçük bir toplam varsa bu değişkenleri tekrar set eder ve son olarak bu değişkenleri
	return eder.


	worst case ;
	f(n)=f(n-1) + n
	bunun sonucuda master teoreme göre O(N^2) bulunur.

'''


def subarray_finder(liste,index):
	if len(liste)==0:
		return []
	alllist=[]
	minlist=[]
	minsum=sys.maxint
	#divide kısmı
	for x in range(index,len(liste)+1):
		alllist.append(liste[index:x])
		if x==len(liste)-1:
			minlist,minsum=subarray_finder(liste,index+1)
	#conqure kısmı
	for x in alllist:
		if x !=[] and sum(x)<minsum:
			minsum=sum(x)
			minlist=x
	return minlist,minsum
def min_subarray_finder(liste):
	return subarray_finder(liste,0)

print(min_subarray_finder([1, -4, -7, 5, -13, 9, 23, -1]))