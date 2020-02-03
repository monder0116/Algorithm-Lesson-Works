# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
'''
  -ilk önce verilen listedeki kelime uzunluğu en küçük olan kelime bulunur.
	*Divide kısmı;
	-Bulunan en küçük kelime DivideAndConlist fonksiyonuna gönderilir ve bu kelimenin 
	harflerinden oluşabilecek tüm subwordler index parametresine bağlı olarak aynı fonksiyona tekrar
	gönderilir öylece ortak olabilecek tüm subwordler fonksiyona tekrar gelerek recursive şekilde parçalanmış olunur.
	*Conqure kısmı;
	-Divide kısmında bölünen tüm subwordler bir listeye eklenmişti bu liste içerisindeki tüm elemanları 
	parametre olarak gelen kelimeler içerisinde arama işlemi yapılır. Hepsinde geçip ve en uzun subwordu bularak 
	return eder. Aynı şekilde recursive çağrısından gelen sonuca kontrol ederek en uzun subword u bulmuş olunur.

	Worst case
	F(n)=f(n-1) + n^2
	master teorem uygulanırsa F(n)=O(n^3) bulunur.
	

'''

def DivideAndConlist(liste,minword,index):
	if len(liste)==0:
		return []
	substrlist=[]
	recurResult=""
	result=""


	for x in range(index,len(minword)+1):
		tempstr=minword[index:x]
		if len(tempstr)!=0:
			substrlist.append(tempstr)
		if x==len(minword):
			recurResult=DivideAndConlist(liste,minword[index:x],index+1)
	for hece in substrlist:
		tempresult=1
		temphece=""
		for kelime in liste:
			if hece not in kelime:
				tempresult=0
				next
			else:
				temphece=hece

		if len(result)<len(temphece) and tempresult==1:
			result=temphece
	if len(result)>len(recurResult):
		return result
	return recurResult
		
				
		
def longest_common_postfix(liste):
	mini=minindex(liste)
	return DivideAndConlist(liste,liste[mini],0)
def minindex(liste):
	minlen=sys.maxint
	minindex=-1
	for x in range(len(liste)):
		if minlen>len(liste[x]):
			minlen=len(liste[x])
			minindex=x
	return minindex


longest_common_postfix(["ali", "hali", "kslili","yali"])