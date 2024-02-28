#tuples too have duplicates
#to make a tuple with one item
t1=('audi',)
print(t1)
#comma is mandatory
t2=('benz')
print(t2)

#length of tuple
t3=('audi','cars','benz','volvo')
print(len(t3))
print(t3)
#alternative way to create a tuple using tuple()
t4=tuple(('audi','cars','benz','volvo'))
t5=(('audi','cars','benz','volvo'))
print(t4)
print(type(t4))
print(t5)
print(type(t5))


#accessing tupleitems 
#tryning to access item out of the index range will result an IndexError
#providing float or any other data type as index will result in TypeError
print(t5[:])

#adding items to a tuple
#as there are immutable we cant directly add items to a tuple
l1=list(t5)
l1.append('toyota')
t6=tuple(l1)
print(t6)

#so we done it indirectl through converting into a list


#updating items to a tuple
#as there are immutable we cant directly update items to a tuple
l2=list(t5)
l2[1]='kodi'
t7=tuple(l2)
print(t7)

#removing items from a tuple
l3=list(t5)
l3.remove('audi')
t8=tuple(l3)
print(t8)

#deleting a tuple
del t5
# print(t5)



#packing means assigning values to a tuple.

#unpacking means extracting values from a tuple.


names=('saketh','sai','surya','harikesh','venkat')
v1,v2,v3,v4,v5=names
print(v1,v2,v3,v4,v5)


#use of asterisk
#used when the no.of variables are less than the values of a tuple.
v1,v2,*v3=names
print(v1,v2,v3)
v1,*v2,v3=names
print(v1,v2,v3)