list1=[4,9,5,3,7,2,6,1]
print("original list is",list1)
count=0

# Finding the sum
for i in list1:
    count=count+1
print("the sum is ",count)
# finding the average
average=count/len(list1)
print("the average is ",average)


# Sorting the elements of the list
list1.sort()
print("The smallest element is ",list1[0])
print("the largest element is ",list1[-1])