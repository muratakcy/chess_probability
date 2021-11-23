Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> j=0
>>> for i in range(10000000,11111112,1):
	dizilim=str(i)
	tut=True
	for n in dizilim:
		if(n!="1")and(n!="0"):
			tut=False
			break
	if tut==True:
	    for n in range(0,len(dizilim),1):
		    if (len(dizilim)-1)!=n:
			    if (dizilim[n]=="0")and(dizilim[n+1]=="0"):
				    tut=False
				    break
	if tut==True:
		j=j+1
		print(dizilim,end=",")

		
10101010,10101011,10101101,10101110,10101111,10110101,10110110,10110111,10111010,10111011,10111101,10111110,10111111,11010101,11010110,11010111,11011010,11011011,11011101,11011110,11011111,11101010,11101011,11101101,11101110,11101111,11110101,11110110,11110111,11111010,11111011,11111101,11111110,11111111,
>>> print("8*8 satranç tahtası için toplam ",j*8," farklı dizilim bulunmaktadır")
8*8 satranç tahtası için toplam  272  farklı dizilim bulunmaktadır
>>> 