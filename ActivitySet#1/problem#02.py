


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)


L1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(L1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)



L1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(L1[-4:-1])


for x in range(2, 30, 3):
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)


print("Hello World")

x = "Hello"
y = 15
print(bool(x))
print(bool(y))


a=5
b=3
c=10<<1
d=20>>1
print("bitwise and of a and b is", a&b)
print("bitwise or of a and b is", a|b)
print("bitwise xor of a and b is", a^b)
print("bitwise not of a and b is", ~a)
print("Zero fill left shift is", c)
print("Signed right shift is", d)


a=int(input("Enter first value"))
b=int(input("Enter second value"))
print("Before swapping, value of a=", a)
print("Before swapping, value of b=", b)
a,b=b,a
print("After swapping, value of a=", a)
print("After swapping, value of b=", b)


x="REVA UNIVERSITY"
print('R' in x)
print('U' in x)
print("reva" not in x)