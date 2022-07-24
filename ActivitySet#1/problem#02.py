# Write a program that uses a print statement to say 'hello world'

print('hellooo')

str1=str(input("Enter the string"))
def slicing():
	m=int(input("Enter the starting index value or index1"))
	n=int(input("Enter the ending index value or index2"))
	substr=str1[m:n]
	print("String extracted between index1 and index2 is",substr)
slicing()
