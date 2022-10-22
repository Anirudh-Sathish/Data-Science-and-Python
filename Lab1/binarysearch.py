"""
                 Lab 1 Code : To perform binary search
                 Author : @Anirudh Sathish
"""

""" 
    Insertion sort is simmilaer to dealing a hand of cards. Maintaing an 
    array of sorted cards on one side 
    The constant part in the algorithm is that the left side sorted array
    is always sorted
"""

"""
  Time Complexity analysis of the algo"""

#Code to sort the array using insertion sort 
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

#Code to binary search any given element in a sorted array 
def binarySearch(low , high ,arr , key):
    # Check if high is greater than low 
    if(high >=low):
        # The // is to make sure we get an integer output to the mid value 
        mid = (low+high)//2
        if(key == arr[mid]):
            return mid
        if(key >arr[mid]):
            return binarySearch(mid+1, high,arr,key)
        elif(key <arr[mid]):
            return binarySearch(mid-1,high,arr,key)
    else:
        # The element is not found in the list 
        return -1

#Function to do the search
def searchElement(low , high ,arr , key):
    if(len(arr) >4):
        binarySearch(low,high,arr,key)
    else:
        for i in range(0,arr(len)):
            if(key == arr[i]):
                return arr[i]
        return -1
        
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

#Asking the user to input a search parameter
search_parameter = int(input("What is the number you are searching for "))

#performing the binary search
search = binarySearch(0,val-1,arr,search_parameter)

print("The sorted array is ")
print(arr)
#Printing out the index at which it exists 
if(search == -1):
    print("The given element does not exist in the array")
else:
    print("The given element exists in the array at index "+str(search))