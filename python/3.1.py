hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)


if h <=40:
   pay = h * r
elif h > 40:
   pay = 40* r + (h-40)*1.5*r
   
print (pay)