from linkedlist import *

class AVLTree: 
    root = None 

class AVLNode: 
    parent = None
    leftnode = None 
    rightnode = None 
    key = None 
    value = None 
    bf = None 

#Ejercicio 1
def rotateLeft(tree, rotRoot):
    newRoot = rotRoot.rightnode
    rotRoot.rightnode = newRoot.leftnode

    if newRoot.leftnode != None:
        newRoot.leftnode.parent = rotRoot
    newRoot.parent = rotRoot.parent

    if rotRoot.parent == None:
        tree.root = newRoot
    else:
        if rotRoot.parent.leftnode == rotRoot:
            rotRoot.parent.leftnode = newRoot
        else:
            rotRoot.parent.rightnode = newRoot

    newRoot.leftnode = rotRoot
    rotRoot.parent = newRoot

def rotateRight(tree, rotRoot):
    newRoot = rotRoot.leftnode
    rotRoot.leftnode = newRoot.rightnode

    if newRoot.rightnode != None:
        newRoot.rightnode.parent = rotRoot
    newRoot.parent = rotRoot.parent

    if rotRoot.parent == None:
        tree.root = newRoot
    else:
        if rotRoot.parent.rightnode == rotRoot:
            rotRoot.parent.rightnode = newRoot
        else:
            rotRoot.parent.leftnode = newRoot

    newRoot.rightnode = rotRoot
    rotRoot.parent = newRoot


#Ejercicio 2
def calculateBalance(tree: AVLTree):
    _balanceImpl(tree.root)

def _balanceImpl(currentNode: AVLNode) -> int:
    if currentNode == None:
        return -1

    leftH = _balanceImpl(currentNode.leftnode)
    rightH = _balanceImpl(currentNode.rightnode)

    currentNode.bf = leftH - rightH

    return 1 + max(leftH, rightH) #max porque buscamos el camino más largo hacia abajo


def access(tree: AVLTree, key: int):
    if tree.root.key == key:
        return tree.root
    
    node = getNode(tree.root, key)
    if node:
        return node
    else:
        return

def getNode(currentNode: AVLNode, key: int) -> AVLNode:
    if currentNode is None:
        return None

    if currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return getNode(currentNode.leftnode, key)
    else:
        return getNode(currentNode.rightnode, key)


def search(AVL: AVLTree, element) -> int | None:
    if AVL.root is None:
        return None
    
    return _searchImpl(AVL.root, element)

def _searchImpl(currentNode: AVLNode, element):
    if currentNode is None:
        return None
    
    if currentNode.value == element:
        return currentNode.key
    
    looked_left = _searchImpl(currentNode.leftnode, element)

    if looked_left is not None:
        return looked_left
    
    looked_right = _searchImpl(currentNode.rightnode, element)
    return looked_right


def insert(AVL: AVLTree, element, key: int) -> int | None:
    newNode = AVLNode()
    newNode.value = element
    newNode.key = key

    if AVL.root is None:
        AVL.root = newNode
        return newNode.key
    else:
        return _insertImpl(newNode, AVL.root)

def _insertImpl(newNode: AVLNode, currentNode: AVLNode) -> int:
    if newNode.key > currentNode.key:
        if currentNode.rightnode is None:
            currentNode.rightnode = newNode
            newNode.parent = currentNode
        else:
            return _insertImpl(newNode, currentNode.rightnode)
    else:
        if currentNode.leftnode is None:
            currentNode.leftnode = newNode
            newNode.parent = currentNode
        else:
            return _insertImpl(newNode, currentNode.leftnode)

    return newNode.key


def traverseInOrder(AVL: AVLTree) -> LinkedList | None:
    if AVL.root is None:
        return None
    
    L = LinkedList()
    _inOrderImpl(AVL.root, L)
    return L

def _inOrderImpl(currentNode: AVLNode, L: LinkedList):
    if currentNode:
        _inOrderImpl(currentNode.rightnode, L)

        add(L, currentNode.value)

        _inOrderImpl(currentNode.leftnode, L)

def print_inOrder(tree):
    linkedTree = traverseInOrder(tree)
    currentNode = linkedTree.head

    while currentNode:
        print(currentNode.value, end=" ")
        currentNode = currentNode.nextNode
    print("")


def traverseInPostOrder(AVL: AVLTree) -> LinkedList | None:
    if AVL.root is None:
        return None
    
    L = LinkedList()
    _inPostOrderImpl(AVL.root, L)
    return L

def _inPostOrderImpl(currentNode: AVLNode, L: LinkedList):
    if currentNode:
        data = [currentNode.value, currentNode.bf]

        add(L, data)
        _inPostOrderImpl(currentNode.rightnode, L)
        _inPostOrderImpl(currentNode.leftnode, L)

def print_inPostOrder(tree):
    linkedTree = traverseInPostOrder(tree)
    currentNode = linkedTree.head

    while currentNode:
        print(currentNode.value, end=" ")
        currentNode = currentNode.nextNode
    print("")


tree = AVLTree()
# insert(tree, "a", 4)
# insert(tree, "b", 2)
# insert(tree, "c", 6)
# insert(tree, "d", 1)
# insert(tree, "e", 3)
# insert(tree, "f", 5)
# insert(tree, "g", 7)

insert(tree, "e", 30)
insert(tree, "c", 25)
insert(tree, "d", 28)
insert(tree, "b", 15)
insert(tree, "a", 10)
insert(tree, "f", 40)


calculateBalance(tree)

print(tree.root.bf)

print_inPostOrder(tree)

# print(access(tree, 30))
rotateRight(tree, access(tree, 30))

calculateBalance(tree)
print(tree.root.bf)
print_inPostOrder(tree)