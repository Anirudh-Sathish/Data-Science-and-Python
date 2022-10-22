# @ Author : Anirudh Sathish 
# @ RollNo : CS20B1125

#Defining the libraries 
import pandas as pd 

class Manage(object):
    def __init__(self):
        # Creating the inital dataframe 
        #Holding the required values 
        name_list = ["Ram","Sam","Prabhu","Ruth","Jam"]
        AccountNo_list = ["9893893891","9893893898","9893893871","9893893872","9893893873"]
        AccountType_list = ["SB","CA","SB","SB","CA"]
        AadhaarNo_List = ["989389389173","989389389179","989389389159","989389389160","989389389162"]
        Balance = [8989839,7690990,989330,50000,1000]

        # Creating a dictionary to hold values 
        dict_1 ={'Name': name_list, 'AccountNo':AccountNo_list,
         'AccountType': AccountType_list ,'Adhaar_No': AadhaarNo_List ,
          'Balance': Balance}
        
        # Creating the dataframe 
        df1 = pd.DataFrame(dict_1)
        self.data_frame = df1
        print(df1)
        #Coverting to excel
        df1.to_csv("SBIAccountHolder.csv")
    
    def createAndAppendRecord(self):
        name = input("Enter the name of the user ")
        accountNo = input("Enter the account of the user ")
        accountType = input("Enter the Bank Type of the user ")
        adharNo = input("Enter the Aadhar Number ")
        balance = int(input("Enter the Bank Balance "))

        name_list = [name]
        AccountNo_list = [accountNo]
        AccountType_list = [accountType]
        AadhaarNo_List = [adharNo]
        Balance = [balance]

        dict_2 ={'Name': name_list, 'AccountNo':AccountNo_list, 'AccountType': AccountType_list ,
      'Adhaar_No': AadhaarNo_List , 'Balance': Balance}
        df2 = pd.DataFrame(dict_2) 
        self.data_frame = self.data_frame.append(df2,ignore_index=True)

        print(self.data_frame)
        self.data_frame.to_csv("SBIAccountHolder.csv")
    
    def DeleteAccount(self):
        index = 0
        requiredAccount = input("Enter the required account no")
        for acc_no in self.data_frame["AccountNo"]:
            if(acc_no == requiredAccount):
                self.data_frame = self.data_frame.drop(index)
                self.data_frame = self.data_frame.reset_index()
                self.data_frame = self.data_frame.drop(['index'], axis=1)
                print(self.data_frame)
                self.data_frame.to_csv("SBIAccountHolder.csv")
            index+=1 

    def Credit(self):
        requiredAccount = input("Enter the required account no")
        index = 0
        for acc_no in self.data_frame["AccountNo"]:
            if(acc_no == requiredAccount):
                print("Balance : ")
                moneyToBeCredited = int(input("Enter the amount to be credited"))
                val = self.data_frame['Balance'][index] + moneyToBeCredited 
                self.data_frame['Balance'][index] = val 
                print(self.data_frame['Balance'][index])
                print(self.data_frame)
                self.data_frame.to_csv("SBIAccountHolder.csv")
                return 0
            index+=1
        #If it is here , then i didnt find the code
        print("Could not find the account")
    def debit(self):
        requiredAccount = input("Enter the required account no")
        index = 0
        for acc_no in self.data_frame["AccountNo"]:
            if(acc_no == requiredAccount):
                print("Balance : ")
                moneyToBeDebited= int(input("Enter the amount to be credited"))
                if(self.data_frame["AccountType"] == "SB" and self.data_frame['Balance'][index] > moneyToBeDebited):
                    print("There is .an error!!!!")            
                else:
                    val = self.data_frame['Balance'][index] - moneyToBeDebited
                    self.data_frame['Balance'][index] = val    
                    print(self.data_frame['Balance'][index])
                    print(self.data_frame)
                    self.data_frame.to_csv("SBIAccountHolder.csv")
                    break
            index+=1
        print("Didnt find the account number")
    def createAndMergeSecond(self):
        # Creating the inital dataframe 
        #Holding the required values 
        name_list = ["Ram","Sam","Prabhu","Ruth","Jam"]
        AadhaarNo_List = ["989389389173","989389389179","989389389159","989389389160","989389389162"]
        Contact_No_List = ["9893800891","90093893898","989389387100","989380293872","9890023893873"]
        DOB_List = ["12-2-1990","12-2-2000","12-10-2010","12-10-2011","12-10-2013"]
        Address = ["Kandigai","Melakpttaiyur","Tambaram","Chepauk","Tnagar"]

        # Creating a dictionary to hold values 
        dict_3 ={'Name': name_list, 'Adhaar_No':AadhaarNo_List,
         'ContactNo': Contact_No_List ,'DOB': DOB_List ,
          'Address': Address}
        
        # Creating the dataframe 
        df3 = pd.DataFrame(dict_3)
        df3.to_csv("Aadhar_DB.csv")

        self.data_frame = pd.merge(self.data_frame,df3,how='left')
        print("\n The Merged  is : \n")
        print(self.data_frame)

        self.data_frame.to_csv("SBIAccountHolder.csv")
        


Instance = Manage()
exploration_done = False

while exploration_done is False:
    # Writing the menu part 
    print("Welcome  \n ")
    print("What Operation do u want to perform \n")
    print("Press Key according to need ")
    print("Press 1 To Insert  ")
    print("Press 2 To Delete Record")
    print("Press 3 To Credit ")
    print("Press 4 For Debit ")
    print("Press 5 for Merge with the other required information ")
    print("Press 6 To Exit")
    option_chosen = int(input("Enter the option you want to chose"))
    if option_chosen == 1:
        #Inserting value into dict
        print("1. Inserting record ")
        Instance.createAndAppendRecord()
    elif option_chosen == 2:
        print("2. Deleting record")
        Instance.DeleteAccount()
    elif option_chosen == 3:
        print("3. Crediting to Account")
        Instance.Credit()
    elif option_chosen == 4:
        print("Debiting from the account ")
        Instance.debit()
    elif option_chosen == 5:
        print("Merging Two tables ")
        Instance.createAndMergeSecond()
    elif option_chosen == 6:
        print("Thanks for visiting ")
        print("You are exiting now")
        exploration_done = True
    else:
        print("Maybe you made an input error. We take input values from range 1 to 6")