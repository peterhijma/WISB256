sum1=[]
sum2=[]

for i in range(1,101):
    x=i*i
    sum1.append(x)

for j in range(1,101):
    sum2.append(j)

sum_of_numbers_squared=sum(sum2)*sum(sum2)
    
print(sum(sum1))
print(sum_of_numbers_squared)

print('The difference between the two is: ', sum_of_numbers_squared-sum(sum1))