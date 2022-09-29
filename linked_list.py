# charan's module
# developed linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert(self, data):
        if self.head is None:
            self.head = data
        else:
            lastNode = self.head
            while True:
                if lastNode.Next is None:
                    break
                lastNode = lastNode.Next
            lastNode.Next = data

    def append(self, data):
        if self.lastNode is None:
            self.head = Node(data)
            self.lastNode = self.head
        else:
            self.lastNode.Next = Node(data)
            self.lastNode = self.lastNode.Next

    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                print("finished")
                break
            elif currentNode is not None:
                print(currentNode.data)
                currentNode = currentNode.Next
            else:
                print("ntg")



