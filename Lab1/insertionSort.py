"""
                 Lab 1 Code : To perform insertion sort 
                 Author : @Anirudh Sathish
"""
#Code to sort the array usign insertion sort 
def insertionSort(arr):
    result =[]
    for i in range(1,len(arr)):
        #Keeping track of the curr element we have 
        curr =arr[i]

        #Sorting out the elements less than the key 
        k = i-1
        while (curr <arr[k]) and k>=0:
            arr[k+1] = arr[k]
            k = k-1
        arr[k+1] = curr

#Take inputs from the user 
val = int(input("Enter the total numbers "))

#Creating an empty list to hold the values 
arr =[]

#Taking in the values that have to go into the array s
for i in range(val):
    i = int(input("Enter Value  "))
    arr.append(i)

#Appling the sort function on the array 
insertionSort(arr)

print("The sorted array is ")
print(arr)