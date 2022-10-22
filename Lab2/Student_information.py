"""
    Lab code 2 : Question 1 : Student Information
    @Author : Anirudh Sathish
"""
""" 
Write a python script to implement student details using a dictionary.
The roll number of the student will be the key, the value will be a list 
containing the name, CGPA, and mobile number of the respective student.
The program should be implemented as a menu-driven program with the following menus,
1.Insert
2.Delete
3.Search
4.Exit
"""

#Creating an empty dict 
    #It should contain a roll_no key and a student_info_list
    #roll_no shall be a string 
student_storage ={}

exploration_done = False

while exploration_done is False:
    # Writing the menu part 
    print("Welcome to the Student Info Corner")
    print("What are you here for ?")
    print("Press Key according to need ")
    print("Press 1 For Inserting your data ")
    print("Press 2 For Deleting your data ")
    print("Press 3 For Searching your data ")
    print("Press 4 For Exiting ")
    option_chosen = int(input("Enter the option you want to chose "))
    if option_chosen == 1:
        #Inserting value into dict
        #So take input 
        #Ask for roll_number
        roll_number = (input("Enter your roll_number "))
        #Creating an empty list
            #The list shall contain name , CGPA and mobile number     
        student_info_list = []
        #Ask for Name , CGPA and mobile_number 
        student_Name = (input("Enter your name "))
        student_info_list.append(student_Name)
        student_CGPA = (input("Enter CGPA "))
        student_info_list.append(student_CGPA)
        student_Mobile = int(input("Enter mobile no "))
        student_info_list.append(student_Mobile)

        #Inserting into the dict with student as key
        student_storage[roll_number] = student_info_list
    elif option_chosen == 2:
        #Deleting the key
        #Take roll Number as input for that
        #Ask for roll_number
        roll_number = (input("Enter your roll_number "))
        if roll_number not in student_storage:
            print("Sorry , this is an invalid roll number ")
            print("Bye Bye!!!! ")
        else: 
            print("We will begin deletion")
            student_storage.pop(roll_number)
            print("Congrats ! You have been succesfully deleted ")
    elif option_chosen == 3:
        print("Let us search for you ")
        roll_number = (input("Enter your roll_number "))
        if roll_number not in student_storage:
            print("Sorry , this roll number does not exist")
            print("Bye Bye!!!! ")
        else:
            student_Name =student_storage[roll_number][0]
            student_CGPA =student_storage[roll_number][1]
            student_Mobile = student_storage[roll_number][2]
            print("The details are ")
            print("Student Name:",student_Name)
            print("Student CGPA:",student_CGPA)
            print("Student Mobile:",student_Mobile)
    elif option_chosen == 4:
        print("Thanks for visiting ")
        print("You are exiting now")
        exploration_done = True
    else:
        print("Maybe you made an input error. We take input values from range 1 to 4")
