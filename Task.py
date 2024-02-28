# #1.sorting letters in a string
# str1='nfkhsevnhjbgfcyvsgja'
# sorted1=sorted(str1)
# print(sorted1)
# str2=''.join(sorted1)
# print(str2)
# #2.printing items
# item=input('Enter an item')
# cost=input('Enter cost')
# total_length=len(item)+len(cost)
# dots='.'*(25-total_length)
# print('Product Name','.'*25,'Price')
# print(item,dots,cost)
# #3.conform password
# p1=input('enter password')
# p2=input('Enter  Confirm password')
# if p1==p2:
#     print('Valid Password')
# else:
#     if(p1.casefold()==p2.casefold()):
#         print('Please check the cases')
#     else:
#         print('Invalid Password')
# #4.card number display
# cn=input('Card Number')
# star='*'*4+' '
# last=cn[15::]
# print(star*3+last)
# #Domain name from email
# d1=input('enter email')
# atrate=d1.find('@')
# user=d1[:atrate]
# domain=d1[atrate+1:]
# print(user)
# print(domain)

#5.palindrome checking and converting into palindrome
# p1=input('Enter text')
# rev=p1[::-1]
# if(rev==p1):
#     print('palindrome')
# else:
#     print('not a palindrome')
#     print(p1+rev)
#6.extracting date month year from DOB
# dob=input('enter DOB')
# l=dob.split('/')
# for i in l:
#     print(i)
# print('Day',l[0])
# print('Month',l[1])
# print('year',l[2])

#7.Anagrams checking
# an1=input('enter text')
# an2=input('enter text')
# if(len(an1)!=len(an2)):
#     print('not a anagram')
# else:
#     for i in an1:
#         if i in an2:
#             print('anagrams')
#             break
#         else:
#             print('not anagrams')

#we have another approach
# an1=input('enter text')
# an2=input('enter text')
# if(len(an1)==len(an2)):
#     if(sorted(an1)==sorted(an2)):
#         print('anagrams')
#     else:
#         print('not anagrams')
# else:
#     print('not a anagram')

#8.rearraging the string
e1=input('enter text')
lower=''
upper=''
for i in e1:
    if i.islower():
        lower+=i
    else:
        upper+=i
print(lower+upper)