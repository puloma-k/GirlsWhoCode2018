#create list
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

#find sum of all elements in list
sum = 0
for age in ages:
    sum += age

#divide the sum by the length of the list
average = sum / len(ages)

#print out average
print(average)
