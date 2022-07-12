def input_two_numbers():
    a=int(input('Enter 1st number: '))
    b=int(input('Enter 2nd number: '))
    return a,b

def add(a, b):
    sum=a+b
    return sum # ...


def output(a, b, sum):
    print('Sum of',a,'and',b,'is',sum)  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)
    output(a, b, sum)


if __name__ == '__main__':
    main()
