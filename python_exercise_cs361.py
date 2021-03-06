# -*- coding: utf-8 -*-
"""Python Exercise CS361.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JHW2uG6jKwhvZLIM5RQ3Tb_YwpsA1c93
"""

#Python Exercise -  Jeremy Rivera
#This is the .py file that includes anything I tested or wrote during the completion of this homework


#Exercise 4
for i in range(5):
  print(range(i))
  
type(range(5))

#Exercise 5
numberfound = 0
x = 11
while numberfound < 20:
	if x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
    print(x)
	numberfound += 1
	x += 1

#Exercise 6a
def is_prime(n):
  if n > 1:
    for i in range(2, int(n / 2)):
      if n % i == 0:
        return False
      else: 
        return True
  else:
    return "Valid Parameters are n > 1"
  
is_prime(23);

#Exercise 6c
def getPrimesTo(n):
	l = []
	for i in range(n):
		if is_primeFast(n):
			l.append(i)
	return l

getPrimesTo(100)

#Exercise 6b
def is_primeFast(n):
  if n > 1:
    if n == 2 or n == 3:
        return True
    elif (n - 1) % 6 == 0 or (n + 1) % 6 == 0:
        if(is_prime(n)):
            return True
        else:
            return False
    else:
        return False
  else:
      return "Valid Parameters are n > 1"

is_primeFast(23)

#Exercise 6d
def firstPrimes(n):
result = []
counter = 0
test = 2
while counter < n:
if is_primeFast(test):
result.append(test)
      			counter += 1
	test += 1
return result

print (firstPrimes(5))

#Exercise 7a
l = [1,2,3,4,599,999]
def printList(n):
	print(n[0:len(n)])
printList(l)

#Exercise 7b
l = [1,2,3,4,599,999]
def printReverseList(n):
	print(n[::-1])
printReverseList(l)

#Exercise 7c
l = [1,2,3,4,599,999]
def lengthList(n):
  count = 0
  if isinstance(n, list):
    for i, value in enumerate(n):
      count += 1
  return count

print(lengthList(l))

#Exercise 8a
a = [1,2,3,4,599,999]

#Exercise 8b
b = a

#Exercise 8c
b[1] = 5

#Exercise 8e
c = a[:]

#Exercise 8f
c[2] = 6

#Exercise 8-Extra
a = [1,2,3,4,599,999] 
def set_first_elem_to_zero(l):
  if len(l) == 0:
    print('list empty')
  else:
    l[0] = 0
  return l

print(set_first_elem_to_zero(a))

#Exercise 9
l = [[1,3] , [3,6]]
def printInnerLists(n):
	for i in range(len(n)):
		if isinstance(n[i], list):
			printInnerLists(n[i])
		else:
			print(n[i])
printInnerLists(l)

#Exercise 10
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
a = np.arange(0.0, 2.0, 0.01)
b = (np.sin(a - 2) **2) * np.exp(-a **2)

fig, ax = plt.subplots()
ax.plot(a, b)

ax.set(xlabel='x', ylabel='y', title='f(x)')
fig.savefig("test.png")
plt.show()

#Excercise 11a
l = [1, 2, 10, 5]
def prodList(n):
  for i in range(1, len(n)):
    n[0] *= n[i]
  return n[0]

print(prodList(l))

#Excercise 11b
l = [1, 2, 10, 5]
def prodList(n):
	if len(n) == 1:
		return n[0]
	else:
		return prodList([n[0]])  * prodList(n[1:])

#Exercise 12
def fibonacci(n): 
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n < 16:
		return fibonacci(n-1) + fibonacci(n-2)
	else:
		return 0
fibonacci(5)

#Exercise 13
import re

file = open('emails.txt','r')
file = file.read()

Emails = re.findall(r'[\w\"\.-@]*[\w\"\w.-]+@[\w\.-]+\.[\w]+', file)
print(Emails)