"""
                 Lab 1 Code : To perform insertion sort 
                 Author : @Anirudh Sathish
"""

""" 
    Insertion sort is simmilar to dealing a hand of cards. Maintaing an 
    array of sorted cards on one side 
    The loop invariant in the algorithm is that the left side array
    is always sorted
"""
"""
Time complexity :
Best time -> O(n)
Worst time -> omega(n^2)
"""

#Take inputs from the user 
val = int(input("Enter the total numbers "))

#Creating an empty list to hold the values 
list1 =[]

#Taking in the values that have to go into the list
for i in range(val):
    i = int(input("Enter Value  "))
    list1.append(i)

#Appling the sort function on the list
for i in range(1,len(list1)):
    #Keeping track of the curr element we have 
    curr =list1[i]

    #Sorting out the elements less than the key 
    k = i-1
    while (curr <list1[k]) and k>=0:
        list1[k+1] = list1[k]
        k = k-1
    list1[k+1] = curr

print("The sorted list is ")
print(list1)
