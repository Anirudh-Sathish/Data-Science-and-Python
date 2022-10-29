"""
                 Lab 1 Code : To perform binary search
                 Author : @Anirudh Sathish
"""


"""
  Time Complexity analysis of the algorithm:
  The binary search has a time complexity of theta(logn)
"""




#Take inputs from the user 
val = int(input("Enter the total numbers "))

#Creating an empty list to hold the values 
list1 =[]

#Taking in the values that have to go into the list
for i in range(val):
    i = int(input("Enter Value  "))
    list1.append(i)

#Appling the sort function
list1.sort()

#Asking the user to input a search parameter
search_parameter = int(input("What is the number you are searching for "))

#performing the binary search
lower_index = 0
higher_index = val -1

# looping around while the condition is true
while(higher_index >= lower_index):
    middle_index = (lower_index+higher_index)//2

    #found the element ,exit the loop 
    if(list1[middle_index] == search_parameter):
        result = middle_index
        break
    #keep searching 
    elif(list1[middle_index] < search_parameter):
        lower_index = middle_index+1
    else:
        higher_index = middle_index-1
    
if(list1[middle_index] == search_parameter):
    search = result
else: # element not there in the list
    search = -1    


print("The sorted list is ")
print(list1)
#Printing out the index at which it exists 
if(search == -1):
    print("The given element does not exist in the list")
else:
    print("The given element exists in the list at index "+str(search))
