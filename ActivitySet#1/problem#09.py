# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
y=0
cnt=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    f=line.find("0.")
    n=float(line[f:])
    y=y+n
    cnt=cnt+1
avg=y/cnt    
print('Average spam confidence:',avg)