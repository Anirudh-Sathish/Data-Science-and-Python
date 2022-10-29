"""
    @Author : Anirudh Sathish 
    Lab 3 
    Question 2 
"""
"""
    Write a python program using classes to implement a queue with the following menu options,
    1.Enqueue
    2.dequeue
    3.Peek (Note: Displays the front value but does not remove it)
    4.Print (Note: Displays all the elements of a queue but does not remove the elements)
    5.Exit
"""



class Node():
    def __init__(self , data):
        self.data = data
        self.NextNode = None

class LinkedList():
    def __init__(self):
        self.HeaderNode = None
        self.Size = 0
    def append(self,data):
        #Adding element to the end of the linkedlist
        NewNode = Node(data)
        if self.Size == 0:
            Temp = NewNode
            self.HeaderNode = Temp
        else:
            # Temp points to the headerNode 
            Temp = self.HeaderNode
            while (Temp.NextNode != None):
                Temp = Temp.NextNode
            Temp.NextNode = NewNode
        self.Size += 1

    def prepend(self,data):
        #Adding elements to the begining of the linkedlist
        NewNode = Node(data)
        
        if self.Size == 0:
            Temp = NewNode
            self.HeaderNode = Temp
            self.Size =self.Size+1
        else:
            NewNode.NextNode = self.HeaderNode
            self.HeaderNode = NewNode
            self.Size =self.Size+1
    def pop(self):
        Temp = self.HeaderNode
        if self.Size == 0 :
            print("Nothing to delete")
        else:
            value = Temp.data
            self.HeaderNode = Temp.NextNode
            del Temp 
            self.Size -= 1
            return value
    def getSize(self):
        return self.Size
    def seeFirstElement(self):
        Temp = self.HeaderNode
        if self.Size == 0:
            print("Empty Stack")  
        else:
            return Temp.data  
    def printList(self):
        Temp = self.HeaderNode
        if Temp == None :
            print("Nothing there")
        elif Temp.NextNode == None:
            print(Temp.data)
        else:
            while(Temp.NextNode != None):
                print(Temp.data)
                Temp = Temp.NextNode
            print(Temp.data)

# To implement a queue 

#Queue should consist of front and rear 
#Operations to be defined on a queue 
#1.Enqueue 
#2.Dequeue
#3.Peek
#4.Print
class Queue(object):
    def __init__(self):
        self.front = -1 
        self.rear = -1
        self.queueList = LinkedList() 
    def Enqueue(self,item):
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queueList.append(item)
    def Dequeue(self):
        if self.front == -1:
            print("There exists no elements in the queue")
            return "Nothing"
        item = self.queueList.pop()
        self.front += 1
        if self.front > self.rear: 
            self.front = self.rear = -1 
        return item
    def peek(self):
        if self.front == -1:
            print("There exists no elements in the queue")
            return "Nothing"
        item = self.queueList.seeFirstElement()
        return item
    def print(self):
        self.queueList.printList()

q = Queue()
exploration_done = False

while exploration_done is False:
    # Writing the menu part 
    print("Welcome to Queue operations ")
    print("What are you here for ?")
    print("Press Key according to need ")
    print("Press 1 For Enqueue ")
    print("Press 2 For Dequeue ")
    print("Press 3 For Peeking your data ")
    print("Press 4 For Printing your data ")
    print("Press 5 For Exiting ")
    option_chosen = int(input("Enter the option you want to chose"))
    if option_chosen == 1:
        #Inserting value into dict
        Value_token = int(input("Enter data inserted "))
        q.Enqueue(Value_token)
    elif option_chosen == 2:
        item_popped = q.Dequeue()
        print(item_popped," Dequed ")
    elif option_chosen == 3:
        item = q.peek()
        print(item , " Is at the front of the queue ")
    elif option_chosen == 4:
        q.print()
    elif option_chosen == 5:
        print("Thanks for visiting ")
        print("You are exiting now")
        exploration_done = True
    else:
        print("Maybe you made an input error. We take input values from range 1 to 5")
