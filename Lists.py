# #MultiDimensinonal Lists

#Lists are Mutable
# l1=[[1,2,3],'saketh',[10,11,12]]
# print(l1[0])
# print(l1[0][0])
# l2=[[1,2,3],[['a','b','c'],5,6]]
# #to access b
# print(l2[1][0][1])

# #Methods
# #adding elements to a list
# #1.append(value)  used to add item at the end of the list
# #1.1)we can add value
# #1.2)duplicate appned() to add multiple elements
# #1.3)a list as an item can be added
# l3=[1,2,3,4,5,6,7,8,9,10]
# #1.1)
# l3.append('saketh')
# print(l3)
# #1.2)
# l3.append('sai')
# l3.append('surya')
# l3.append('venkat')
# l3.append('harikesh')
# print(l3)
# #1.3)
# l3.append([678909876,5678909876])
# print(l3)

# #2.insert() used to add an item at a specific position
# #insert(position,value)
# l3.insert(0,'python')
# print(l3)


# #3.extend() used to add all items of one list in another list
# #list1.extend(list2)
# l4=['saketh','sai','charan']
# l5=['surya','venkat','harikesh']
# l5.extend(l4)
# print(l5)
# l4.extend(l5)
# print(l5)

# n=int(input('enter no.of items:'))
# list1=[]
# for i in range(n):
#     item=input('Enter item')
#     list1.append(item)
# print(list1)
# print(dir(list))


#input a list using split method
# numbers1=input('Enter numbers').split()
# print(numbers1)
#but these are in string type to convert them to integer follow this:

# n1=int(input('Enter no.of elements:'))
# numbers2=input('Enter items').split()
# print(numbers2)
# for i in range(n1):
#     numbers2[i]=int(numbers2[i])
# print(numbers2)



#Remove an item form the list
#1.remove()  it removes the specified item
v1=['surya', 'venkat', 'harikesh', 'saketh', 'sai', 'charan']
v1.remove('sai')
print(v1)
#2.pop() it removes the item at the specified index and it also displays the deleted item
print(v1.pop(2))
#if now value is given in pop() then last item is popped
#3.del() it removes theitem at the speciied index and it is also capable of deleting the entire list
del v1[1]
print(v1)
del v1
# print(v1)  now it shows error

#4.clear() it removes all the items from the list and empty the list
v2=[1,2,3,4,5]
v2.clear()
print(v2)

#copy
v3=[7647839,2345,567,1,4,2]
v4=v3.copy()
print(v4)

#count
v5=[1,2,3,4,5,1,2,1,1,1,2,3,4,4,5]
print(v5.count(1))

#reverse

v3.reverse()
print(v3)

#sort

v3.sort()
print(v3)

v3.sort(reverse=True)
print(v3)



#List comprehensions
#It provides a shorter syntax while creating a new list from the existing list
#the consition should be true
f1=['saketh','surya','venkat','sai']
f2=[name for name in f1 if 's' in name]
print(f2)
f3=[name for name in f1]
print(f3)
f4=[name for name in f1 if 'd' in name]
print(f4)