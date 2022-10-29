# Library Processing using python 
#Anirudh Sathish 


#Defining header file 
import pickle

# Defining The library object
class Library(object):
    def __init__(self):
        self.bookCount = 0
        self.fileSelected =""
    def Write(self,fileName,recordCount):
        self.fileSelected = fileName
        #Opening the required file
        if(self.bookCount == 0):
            file_procured = open(self.fileSelected,"wb")
        else:
            file_procured = open(self.fileSelected,"ab")
        
        #Information to be stored for each book is 
        for i in range(recordCount):
            bookInfoList = []
            #book ISSN, book title, price, edition, year, and author name
            ISSN = int(input("Enter the ISSN number of the book \n"))
            bookInfoList.append(ISSN)
            bookTitle = input("Enter the book title \n")
            bookInfoList.append(bookTitle)
            bookPrice = float(input("Enter the cost of the book in rupees \n"))
            bookInfoList.append(bookPrice)
            bookEdition = int(input("Enter the book edition \n"))
            bookInfoList.append(bookEdition)
            bookYear = int(input("Enter the year of the book \n"))
            bookInfoList.append(bookYear)
            bookAuthorName = input("Enter the author name \n")
            bookInfoList.append(bookAuthorName)

            print(bookInfoList)
            self.bookCount +=1
            #dumping the information in the required dat file
            pickle.dump(bookInfoList,file_procured)
        
        #Closing the file
        file_procured.close()

    def Read(self,fileName):
        self.fileSelected = fileName
        #Opening the required file
        file_procured = open(self.fileSelected,"rb")

        recordCount = self.bookCount
        if(self.bookCount == 0):
            print("Sorry , No records to view ") 
        for i in range(recordCount):
            bookInfoList = []
            try:
                bookInfoList = pickle.load(file_procured)
                print("ISSN : ",bookInfoList[0]," Book Title : ",bookInfoList[1] ," Price : ",bookInfoList[2]," Edition : ",bookInfoList[3] ," Year : " , bookInfoList[4] , " Author : ", bookInfoList[5])
                #print(bookInfoList)
            except EOFError:
                if(self.bookcount == 0):
                    print("There are no records here")
                else:
                    print("The file has reached its end ")
        
        # Closing the file 
        file_procured.close()
    def Search(self , fileName , bookTitle ):
        self.fileSelected = fileName
        #Opening the required file
        file_procured = open(self.fileSelected,"rb")

        recordCount = self.bookCount
        if(self.bookCount == 0):
            print("Sorry , No records to search")
        #Information to be stored for each book is 
        for i in range(recordCount):
            bookInfoList = []
            try:
                bookInfoList = pickle.load(file_procured)
                if (bookInfoList[1] == bookTitle):
                    print("The required item has been found")
                    print("ISSN : ",bookInfoList[0]," Book Title : ",bookInfoList[1] ," Price : ",bookInfoList[2]," Edition : ",bookInfoList[3] ," Year : " , bookInfoList[4] , " Author : ", bookInfoList[5])
                    file_procured.close()
                    return 0
                    break
                        
            except:
                print("The file has reached its end , without obtaining the books ")
                return 0
        # Closing the file
        print("The required item has been not been found")
        file_procured.close()

#Working with the Library 
Library_IIITDM = Library()
exploration_done = False

while exploration_done is False:
    # Writing the menu part 
    print("Welcome to The Library Management System \n ")
    print("What Operation do u want to perform \n")
    print("Press Key according to need ")
    print("Press 1 To Write book records to the Library  ")
    print("Press 2 To Read book contents available in the Library")
    print("Press 3 To search a book by its title ")
    print("Press 4 For Exiting ")
    option_chosen = int(input("Enter the option you want to chose"))
    if option_chosen == 1:
        #Inserting value into dict
        Value_token = int(input("Enter the number of books to be inserted on record \n"))
        file = "books.dat"
        Library_IIITDM.Write(file,Value_token)
    elif option_chosen == 2:
        file = "books.dat"
        Library_IIITDM.Read(file)
    elif option_chosen == 3:
        bookTitle = input("Enter the title you want to search for \n")
        file = "books.dat"
        Library_IIITDM.Search(file,bookTitle)
    elif option_chosen == 4:
        print("Thanks for visiting ")
        print("You are exiting now")
        exploration_done = True
    else:
        print("Maybe you made an input error. We take input values from range 1 to 4")
