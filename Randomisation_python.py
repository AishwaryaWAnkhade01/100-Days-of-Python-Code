# print("Hello World")
# print(type("Hello World"))
#
# print(type(12345))
#
# print(type(12.34678))
#
# print(type(12/4))
#
# print(type(1256))
# ***************************************************************************************************
##Generating random Numbers

import random
# number=random.random()*10
# print(number)

random_number=random.uniform(1 ,10)*10
print(random_number)

#heads and Tails
result=random.randint(0,1)
if result==0:
    print("heads")
else:
    print("tails")

# ***************************************************************************************************
#List in python
#Data Structures:
#creating a list

states_of_india=["Maharashtra", "Manipur", "Meghalaya","Mizoram","Maharashtra","Nagaland","Odisha", "Punjab"]
print(states_of_india[0] + " " "is the state of India")

#Append
#Adds the element in the end of the list
states_of_india.append("Gujrat")
print("added")
print(states_of_india)

#Insert
states_of_india.insert(3,"Himachal")
print(states_of_india)

#count:
result=states_of_india.count("Maharashtra")
print(result)

#negative index
res=states_of_india[-4]
print(res)

#Using List As a Stack
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.insert(3,10)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
#************************************************************************************
#  Using Lists as Queues
from  collections import deque
queue=deque(["Berlin","Tokyo","Rio","Denver","Nairobi"])
queue.append("Palermo")
print(queue)
queue.append("Moscow")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
