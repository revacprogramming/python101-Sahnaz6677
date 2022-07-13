

def get_cs():
    s=input('Enter the string:')
    return s

def cs_to_lot(cs):
    a=cs.split(';')
    d=list()
    for b in a:
        c=b.split('=')
        d.append(c)
    return d

def lot_to_cs(lot):
    
    y=list()
    for i in lot:
        x=' '
        x.join(i) 
        y.append(x)
    print(y)

    


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
