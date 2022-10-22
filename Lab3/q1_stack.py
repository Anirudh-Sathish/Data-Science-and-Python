#Code for linkedlist 

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
            print("Nothing here")
        elif Temp.NextNode == None:
            print(Temp.data)
        else:
            while(Temp.NextNode != None):
                print(Temp.data)
                Temp = Temp.NextNode
            print(Temp.data)

            
class Stack(object):
    def __init__(self):
        self.top = -1
        self.elementList = LinkedList()
    def push(self,item):
        self.top += 1
        self.elementList.prepend(item)
    def pop(self):
        if self.top == -1:
            print("No elements in the stack ")
            return 0 
        item = self.elementList.pop()
        print(item," Popped ")
        return item
    def peek(self):
        if self.top == -1:
            print("No elements in the stack ")
            return 0 
        item = self.elementList.seeFirstElement()
        print(item , " Is at the top of the stack ")
        return item
    def print(self):
        self.elementList.printList()

s = Stack()
exploration_done = False

while exploration_done is False:
    # Writing the menu part 
    print("Welcome to Stack operations ")
    print("What are you here for ?")
    print("Press Key according to need ")
    print("Press 1 For Inserting your data to stack ")
    print("Press 2 For Popping your data from the stack ")
    print("Press 3 For Peeking your data ")
    print("Press 4 For Printing your data ")
    print("Press 5 For Exiting ")
    option_chosen = int(input("Enter the option you want to chose"))
    if option_chosen == 1:
        #Inserting value into dict
        Value_token = int(input("Enter data inserted "))
        s.push(Value_token)
    elif option_chosen == 2:
        item_popped = s.pop()
    elif option_chosen == 3:
        value =  s.peek()
    elif option_chosen == 4:
        s.print()
    elif option_chosen == 5:
        print("Thanks for visiting ")
        print("You are exiting now")
        exploration_done = True
    else:
        print("Maybe you made an input error. We take input values from range 1 to 5")
