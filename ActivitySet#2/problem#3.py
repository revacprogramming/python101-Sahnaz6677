

def get_cs():
    s=input('Enter the string :')
    return s


def cs_to_lot(cs):
    a=cs.split(';')
    d=list()
    for b in a:
        c=b.split("=")
        d.append(c)
    return d

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
