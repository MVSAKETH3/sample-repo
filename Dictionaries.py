#creating dictionaries:key-value pairs
#it doesnt allow duplicates 
#it two keys are same then only one key and its value is stored:the key which is last entered
car1={'name':'audi','model':'q7'}
print(car1)
car2={'name':'audi','model':'q7','model':'q8'}
print(car2)
#they are Mutable
car1['model']='t5'
print(car1)

#len(car) gives the count of key value pairs
print(len(car1))

#creating dictionary using dict()function
car3=dict(name='saketh',age=19)
print(car3)



#accessing keys and values in dictionary
#1.using key names value is accessed

print(car3['name'])
print(car2['model'])

#2.using get() method value is accessed

print(car3.get('name'))
print(car2.get('model'))

#3.uing keys() method keys is accessed

#returns a view object containing keys as a list
#view object reflects any changes done to the dictionary

car_keys=car1.keys()
print(car_keys)
car1['diesel']='petrol'
print(car_keys)

#accessing values using values()method 
#returns a view object containing values as a list
#view object reflects any changes done to the dictionary

car_vals=car1.values()
print(car_vals)
car1['color']='black'
print(car_vals)

#accessing items() using items() an items is a key-value pair

#returns a view object containing items as a list
#view object reflects any changes done to the dictionary
car_items=car1.items()
print('Items:',car_items)
car1['type']='automatic'
print(car_items)


# print(dir(car1))


#changing values in dictionary
#1.using key names

car1['color']='red'
print(car1)

#2.update()
#dict_name.update(dictioonary)
car1.update({'model':'Benz'})
print(car1)

#3.adding new items using key names
#dict_name[new_key]=new_value

car1['year']=2020
print(car1)


#Removing items
#1.pop() removes the items using the key of the item and return the deleted value

print(car1.pop('year'))
print(car1)

#2.popitem() removes the last inserted item  and return the deleted item as tuple

print(car1.popitem())
print(car1)

#3.del() it is just a keyword not a function  it also removes the entire dictionary

del car1['color']
print(car1)

#del car1  to delete entire car1

#clear()
print(car2)
car2.clear()
print(car2)

print('*'*30)
###The assignment opeartor is used to copy only the Immutable objects .it shouldnot be used for Mutable objects
s1='saketh'
s2=s1
print(s1)
print(s2)
s2='sai'
print(s1) 
print(s2) #as string is immutable one change doesnt effected the other 
print('*'*30)
#now observe
d1={'name':'saketh','age':19,'color':'fair'}
d2=d1
print(d1)
print(d2)

d2['age']=20
print(d1)
print(d2)
print('*'*30)
#so here both d1 and d2 are changes so assignment operator is not used for mutable objetcs

#copy()
d3=d1.copy()
print(d1)
print(d3)
d3['age']=21
print(d1)
print(d3)
print('*'*30)
#copy a dictionary using dict() method
d4=dict(d1)
print(d1)
print(d4)
d4['height']=6
print(d1)
print(d4)
print('*'*30)

#fromkeys()
l1=[1,2,3,4,5]
value=0
dict1=dict.fromkeys(l1,value)
print(dict1)

values=['a', 'b', 'c', 'd', 'e']
dict2=dict.fromkeys(l1)
print(dict2)

for i,j in enumerate(l1):      #here in i the index of the list is stored and in j the values of the list is stored
    dict2[j]=values[i]
print(dict2)

#enumerate() is a built-in Python function that adds a counter to an iterable object, such as a list, tuple, or string.
# It returns an enumerate object, which yields pairs of the form (index, value) for each element in the iterable
fruits=['apple','banana','mango','watermelon']
for index,value in enumerate(fruits):
    print(index,value)
print('*'*30)
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
