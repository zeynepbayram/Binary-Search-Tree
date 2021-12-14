from BinaryTree import BinaryTree
import numpy as np

def main():
    myTree = BinaryTree()
    a = np.random.randint(0, 100, 50)
    for i in a:
        myTree.insert(i)
    myTree.insert(121)
    myTree.search(myTree.root, 8)
main()