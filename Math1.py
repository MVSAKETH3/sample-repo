import fractions
f1=fractions.Fraction(1,2)
print('f1',f1)
f2=fractions.Fraction(0.6)
print('f2',f2)
f3=f2.limit_denominator(5)
print('f3',f3)

print('------------------------------------')
print(f'{f1+f2}')
print(f'{f1-f2}')
print('{}'.format(f1*f2))
print('{}'.format(f1/f2))
print('f1 denominator',f1.denominator)
print('f1 numerator',f1.numerator)
print('------------------------------------')
l=[(1,2),(3,4),(5,6),(7,8)]
for i,j in l:
    print('{}'.format(fractions.Fraction(i,j)))
