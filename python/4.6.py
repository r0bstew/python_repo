
try:
	hrs = input("Enter Hours:")
	h = float(hrs)
	rate = input("Enter Rate:")
	r = float(rate)
except:
	print ('Error: Please enter a number')


def computepay(h,r):
	if h <=40:
		pay = h * r
	elif h > 40:
		pay = 40* r + (h-40)*1.5*r
	return pay

print (computepay(h,r))