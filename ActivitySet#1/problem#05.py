
score = input("Enter Score: ")
s=float(score)
if(s<=1 and s>=0):
    if(s>=0.9):
        print('A')
    elif(s>=0.8):
        print('B')
    elif(s>=0.7):
        print('C')
    elif(s>=0.6):
        print('D')
    elif(s<0.6):
        print('F')
else:
    print('Ooopsss! please enter a value between 0.0 to 1.0')