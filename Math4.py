import statistics as s
data1=[1,2,3,4,5,6]
print(s.mean(data1))
print(s.median(data1))
print(s.mode(data1))
print(s.harmonic_mean(data1))
print(s.median_high(data1))
print(s.median_low(data1))
print('-'*40)
#here p means taking complete data
print('1)',s.pvariance(data1))
print('2)',s.pstdev(data1))

#we also have variance() and stdev()
print('1)',s.variance(data1))
print('2)',s.stdev(data1))