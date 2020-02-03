# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Fonksiyon 2 liste ve kth index ve recursive'in kth. indexe gelip gelmediğini kontrol etmek için nth adlı 
integer index tutmaktadır. Basecase'de 3 durum vardır. Bunlar; 
-ilk listenin boş 2.listenin dolu,2.listenin boş ilk listenin dolu ve iki listenin de dolu olma durumudur. 
-Her üç durumdada eğer nth index kth index'e eşitse dolu olan listenin ilk elemanı return edilir. 
-İlk iki case için eğer dolu listenin size'ının iki eksiği eğer kth. indexden büyükse kth eleman listenin ortalarında
demektir bu yüzden listenin başından ve sonundan bir eleman eksiltilerek tekrar yeni listeyi recursive çağrı yapılır.
Eğer değilse zaten birer birer ilerlemek zorundadır. 
-3.case içinde ilk önce liste1 ve liste2nin ilk elemanı kontrol edilir bu sayede hangi listenin daha önce olduğu tespit edilir
ardından nth ile kth kontorlu yapılır yukarıda belirtildiği gibi eğer bu koşul sağlanmazsa , kth elemanın iki listenin sizeı top-
lamının 5 eksiğinden küçük mü diye kontrol edilir( 5 eksik olma sebebi toplam 4 eleman  eksiltmemiz ve bir eleman arama yapmamızdır).
Eğer küçükse ,iki listeyide baştan ve sondan eksilterek recursive çağrı yapılır.Ve daha sonra her çağrı için 
divide and conq. tekrar uygulanır.
- Ve Sonuç olarak algoritma O(Log(k)) karmaşıklığa sahiptir.

Mehmet Önder.

'''
def findin2list(liste1,liste2,kth,nth):
	if len(liste2)>0 and len(liste1)==0:
		if nth==kth:
			return liste2[0]
		if len(liste2)-2>kth:
			return findin2list(liste1,liste2[1:-1],kth,nth+1)
		return findin2list(liste1,liste2[1:],kth,nth+1)
	if len(liste2)==0 and len(liste1)>0:
		if nth==kth:
			return liste1[0]	
		if len(liste1)-2>kth:
			return findin2list(liste1[1:-1],liste2,kth,nth+1)
		return findin2list(liste1[1:],liste2,kth,nth+1)
	if liste1[0]>liste2[0]:
		if kth==nth:
			return liste2[0]
		if kth<len(liste1)+len(liste2)-5:
			return findin2list(liste1[1:-1],liste2[1:-1],kth,nth+1)
		else:
			return findin2list(liste1,liste2[1:],kth,nth+1)
	else:
		if kth==nth:
			return liste1[0]
		if kth<len(liste1)+len(liste2)-5:
			return findin2list(liste1[1:-1],liste2[1:-1],kth,nth+1)
		else:
			return findin2list(liste1[1:],liste2,kth,nth+1)

def find_kth_book_2(m,n,kth):
	if len(m)+len(n)<=kth:
		print("Wrong kth number")
		return ""
	return findin2list(m,n,kth,0)
m = ["algotihm", "programminglanguages", "systemsprogramming"] 
n = ["computergraphics", "cprogramming","oop"]
print(find_kth_book_2(m,n,3	))