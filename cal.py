#to calculate the proprotion of items to buy to minimise steam wallet unused
import parse_price as *
import math
x=input("balance?")
if type(x) != int:
	x=parse_price(x)
a=input("item 1 price?")
b=input("item 2 price?")
def cal(a,b,x):
	best_remainder= min(a,b)
	maxa=math.floor(x/a)
	maxb=math.floor(x/b)
	for i in range(0,maxa):
		suma=x-(i*a)
		for j in range(0,maxb):
			if suma-j*b<0:
				break
			if best_remainder >=suma-j*b:
				best_remainder=suma-j*b
				print("buy {} of a(${}) and {} of b(${}) for {} steam wallet left".format(i,a,j,b,best_remainder))
cal(a,b,x)
