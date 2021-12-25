''' 
Program 1 -  find the average of 2 numbers

a = input("Enter first number: ")   # string type
b = input("Enter second number: ")  # string type

a = int(a)  # int type
b = int(b)  # int type

avg = (a + b) / 2

# print("The average of a and b is", avg)
print(f"The average of a and b is {avg}")   # Another way to print using format string

'''

'''
Program 2 - Functionality of List Features

# this does not cover all methods so check out python docs for the rest of the list methods

l1 = [2, 4, 1, 5, 9, 6, 8, 3]
# print(l1)
# newL1 = l1.sort()   # this line of code does not modify the newL1 variable
# print(newL1)        # which is why none is printed

# l1.sort()  # sorts the string
# l1.reverse()  # reverses the string
# l1.append(8)  # adds value at the end of the list   [Most used method]
# l1.insert(3,8) # insert 8 at index 3 [this shifts the elements after index 3 towards right by one position]
# l1.pop(3) # removes element from index 3
# l1.remove(8) # removes element 8 from the list 
# print(l1)   

'''


'''
Program 3 - Functionality of Dictionary


myDict = { "Harry": "a coder", "animal": "lion"}
myDict2 = { 'pet': 'dog', 'car': 'mercedes', "list": [1,2,1,3,5,55,6,8], "anotherDict": { "fruits": 'apple', "vegetables": "potato"}
}

print(myDict["Harry"])
print(myDict2['pet])
print(myDict2['list'])
print(myDict2['anotherDict'])
print(myDict2['anotherDict']['fruits'])
myDict2['list'] = [3, 4, 4, 6, 7, 7, 3]    # list in dictionary 2 got updated
print(myDict2['list'])

# Using key we can access the value in dictionary in O(log n) time

# Methods of dictionary [Some of them] :
#   myDict.keys() -> list all keys in dictionary
#   myDict.value() -> list all values in dictionary
#   myDict.items() -> displays a list of a given dictionary's (key, value) tuple pair
#   myDict.update()

# Similarity between .get and [] syntax in Dict

print(myDict.get('Harry'))  // returns value
print(myDict['Harry'])   // returns value

# One key difference between .get and just using square bracket to access value from a key

print(myDict.get('Harry2'))   # returns none if key not present in dictionary
print(myDict['Harry2'])   # throwas an error if key not present in dicionary

'''

# a = [24,34,44]
# print(44 in a)

# subject1 = int(input("Enter marks fo first subject: "))
# print(subject1)

'''
Program 4 - Check if a number is prime or not

num = (int(input("Enter the number: ")))
flag = True

for i in range(2, num):
    if (num % i == 0):
        flag = False

if flag is True:
    print("Number is Prime")
else:
    print("Number is not Prime")

'''

'''
PROGRAM 5 - Find the factorial of a number

num = int(input("Enter the number: "))
fact = 1


for i in range(1, num + 1):
    print("enter")
    fact = fact * i

print(fact)
'''

'''
Program 6 - Print the following pattern:

*
**
***

num = int(input("Enter the number: "))
i = 0
j = i + 1
mylist = []    # empty list

for i in range(1, num + 1):
    mylist.append("*" * i)
print("\n".join(mylist))

'''



'''
Program 7 - Print the following pattern:

     *
   * * *
 * * * * *

num = int(input("Enter the number: "))
 # 1st loop is printing the spaces
 # 2nd  loop is printing the star pattern

space = ""
# k = num

for i in range(num):

    print(" " * (num - i - 1), end = "")
    print("*" * (2 * i + 1), end = "")
    print(" " * (num - i - 1))
    # print("\n".join(mylist))
    # k = k - 1

'''

'''

Program 8 - Hollow Square pattern

* * *
*   *
* * *

for n = 3

num = int(input("Enter the number: "))

for i in range(num):
    for j in range(num):
        if (i == 0 or i == num - 1 or j == 0 or j == num - 1):
            print("*", end = "")
        else:
            print(" ", end = "")

    print("\r")  #  end line afrer each row

'''

'''

Program 9 - Sum of first n natural numbers using recursive function

num = int(input("Enter the value of n: "))

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))

'''































