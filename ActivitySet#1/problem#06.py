def computepay(h, r):
    if h<=40:
        p=h*r
    else:
        p=(40*r)+(h-40)*r*1.5
    return p

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter Rate :")
r=float(rate)
p=computepay(h,r)
print("Pay", p)