import random
print(random.random())
print(random.random())
print(random.uniform(1,10))
print(random.uniform(30,50))
print(random.randint(1,40))
print(random.randrange(1,20,3))
print('*'*30)
random.seed(10)
print('1.',random.random())
print('2.',random.random())
print('3.',random.random())
random.seed(10)
print('1.',random.random())
print('2.',random.random())
print('3.',random.random())
print('*'*30)
l1=[4,5,7,8,9,1,3]
l2=['saketh','surya','venkat','hariikesh']
random.shuffle(l1)
print(l1)
print(random.choice(l1))
print(random.choice(l2))
# print(random.sample(l2))
print(random.choices(l1,k=2))
print(random.choices(l2,k=2))
# print(random.sample(l2,k=3))
print('*'*30)
st=random.getstate()
print('1.',random.random())
print('2.',random.random())
print('3.',random.random())
random.setstate(st)
print('1.',random.random())
print('2.',random.random())
print('3.',random.random())

print('*'*40)
print(random.getrandbits(2))
print(random.getrandbits(2))
print(random.getrandbits(3))
print(random.getrandbits(3))