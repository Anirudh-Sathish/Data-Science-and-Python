"""      Lab 2 : Data Science : Q2
         @Author : Anirudh Sathish
"""
""" 
Write a python program to implement set operations using menu-driven programming. The menus to be implemented are as follows,
1.Create Empty Set
2.Insert
3.Delete
4.Search
5.Print
6.Union
7.Intersection
8.Set Difference
9.Symmetric Difference
"""

# Creating a dictionary to hold the sets
SetDict = {"set":"NULL"}

exploration_done = False

while exploration_done is False:
    # Writing the menu part
    print("----------------------------------------------------------------------")
    print("                                                                      ")
    print("Welcome to the Set Ops ")
    print("What are you here for ? ")
    print("Press Key according to need ")
    print("Press 1 For Creating Empty Set ")
    print("Press 2 For Insert ")
    print("Press 3 For Delete ")
    print("Press 4 For Search ")
    print("Press 5 For Print ")
    print("Press 6 For Union ")
    print("Press 7 For Intersection ")
    print("Press 8 For Set Difference ")
    print("Press 9 For Symmetric Difference ")
    print("Press 10 For Exiting ")


    option_chosen = int(input("Enter the option you want to chose "))
    if option_chosen == 1:
        setName = (input("Enter the setName "))
        var = setName
        if setName not in SetDict:
            setName =set()
            print("The set has been created with name ",var)
            SetDict[var]= setName
        else:
            print("There is already a set with the given name")


    elif option_chosen == 2:
        #Inserting into set
        print("To which set do u want to insert to ")
        setName = (input("Enter the setName "))
        var = setName
        if setName in SetDict:
            num_val = int(input("Enter the no of elements in the set "))
            for i in range(0,num_val):
                value = (input("Enter the value u want to insert "))
                SetDict[var].add(value)
                print(value," has been added to ",var)
                

        else:
            print("There is no set like this ")
    elif option_chosen == 3:
        #Deleting from the set
        print("To which set do u want to delete from ")
        setName = (input("Enter the setName "))
        var = setName
        if setName in SetDict:
            value = (input("Enter the value u want to delete "))
            if value in SetDict[var]:
                SetDict[var].remove(value)
                print("Removed")
            else:
                print(value," is not there in the set ",setName)
        else:
            print("There is no set like this ")
    elif option_chosen == 4:
        print("Let us search for you ")
        setName = (input("Enter the setName "))
        var = setName
        if var in SetDict:
            value = (input("Enter the value u want to search for "))
            if value in SetDict[var]:
                print(value," is there in the set ",setName)
            else:
                print(value," is not there in the set ",setName)
        else:
            print("There is no set like this ")

    #Display
    elif option_chosen == 5:
        print("Let us display for you ")
        setName = (input("Enter the setName "))
        var = setName
        if var in SetDict:
            print("The set is :",SetDict[var])
        else:
            print("There is no set like this ")

    #Union        
    elif option_chosen == 6:
        print("Union Operation ")
        setName1 = (input("Enter the setName "))
        var1 = setName1
        if setName1 in SetDict:
            print("Enter the name of the set u want to make this set perform union with ")
            setName2 = (input("Enter the second setname "))
            var2 = setName2
            if setName2 in SetDict:
                SetDict[var1] =SetDict[var1].union(SetDict[var2])
                print("The set after union is ",SetDict[var1])
            else:
                print("There is no such set ")       
        else:
            print("There is no set like this ")
    #Intersection        
    elif option_chosen == 7:
        print("Intersection operation")
        setName1 = (input("Enter the setName "))
        if setName1 in SetDict:
            print("Enter the name of the set u want to make this set perform intersection with ")
            setName2 = (input("Enter the second setname "))
            if setName2 in SetDict:
                SetDict[setName1] = SetDict[setName1].intersection(SetDict[setName2])
                print("The set after intersection is ",SetDict[setName1])
            else:
                print("There is no such set ")       
        else:
            print("There is no set like this ")
    #Set Difference    
    elif option_chosen == 8:
        print("Set Difference operation")
        setName1 = (input("Enter the setName "))
        if setName1 in SetDict:
            print("Enter the name of the set u want to make this set perform set difference with ")
            setName2 = (input("Enter the second setname "))
            if setName2 in SetDict:
                SetDict[setName1] = SetDict[setName1].difference(setName2)
                print("The set after set difference is ",SetDict[setName1])
            else:
                print("There is no such set ")       
        else:
            print("There is no set like this ")
    #Symmetric Difference        
    elif option_chosen == 9:
        print("Symmetric Difference operation")
        setName1 = (input("Enter the setName "))
        if setName1 in SetDict:
            print("Enter the name of the set u want to make this set perform symmetric set difference with ")
            setName2 = (input("Enter the second setname "))
            if setName2 in SetDict:
                SetDict[setName1] = SetDict[setName1].symmetric_difference(SetDict[setName2])
                print("The set after symmetric set difference is ",SetDict[setName1])
            else:
                print("There is no such set ")       
        else:
            print("There is no set like this ")
    elif option_chosen == 10:
        print("Thanks for visiting ")
        print("You are exiting now")
        exploration_done = True
    else:
        print("Maybe you made an input error. We take input values from range 1 to 9")
