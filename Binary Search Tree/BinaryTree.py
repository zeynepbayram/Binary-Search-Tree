from Node import Node

class BinaryTree:

    def __init__(self, data = None):
        if data != None:
            self.root = Node(data)
        else:
            self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        root = self.root
        while True:
            if data > root.data:
                if root.rightChild == None:
                    root.rightChild = Node(data)
                    return
                else:
                    root = root.rightChild
            else:
                if root.leftChild == None:
                    root.leftChild = Node(data)
                    return
                else:
                    root = root.leftChild
    
    def printTreeInOrder(self, root):
        if root == None:
            return
        self.printTreeInOrder(root.leftChild)
        print(root.data, end = ' ')
        self.printTreeInOrder(root.rightChild)
    
    def printTreePreOrder(self, root):
        if root == None:
            return
        self.printTreePreOrder(root.leftChild)
        self.printTreePreOrder(root.rightChild)
        print(root.data, end = ' ')
    
    def search(self, root, key):
        if root == None:
            print("bulunamadi ", key)
        elif root.data == key:
            print("bulundu ", key)
            return
        elif root.data < key:
            self.search(root.rightChild, key)
        else:
            self.search(root.leftChild, key)
        


           
        