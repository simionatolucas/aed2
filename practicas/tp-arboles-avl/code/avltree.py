from linkedlist import LinkedList, add

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

    return newRoot

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

    return newRoot


#Ejercicio 2
def calculateBalance(tree: AVLTree):
    _balanceImpl(tree.root)

    return tree

def _balanceImpl(currentNode: AVLNode) -> int:
    if currentNode is None:
        return -1

    leftH = _balanceImpl(currentNode.leftnode)
    rightH = _balanceImpl(currentNode.rightnode)

    currentNode.bf = leftH - rightH

    return 1 + max(leftH, rightH) #max porque buscamos el camino más largo hacia abajo


#Ejercicio 3
def reBalance(tree: AVLTree):
    calculateBalance(tree)
    
    if tree.root is not None:
        reBalanceSubTree(tree, tree.root)
        
    return tree

def reBalanceSubTree(tree: AVLTree, node: AVLNode):
    if node is None:
        return
        
    reBalanceSubTree(tree, node.leftnode)
    reBalanceSubTree(tree, node.rightnode)
    
    if node.bf > 1: 
        # rotación doble izquierda derecha
        if node.leftnode and node.leftnode.bf < 0:
            rotateLeft(tree, node.leftnode)
        
        new_root = rotateRight(tree, node)
        _balanceImpl(new_root)
        
    elif node.bf < -1: 
        # rotación doble derecha izquierda
        if node.rightnode and node.rightnode.bf > 0:
            rotateRight(tree, node.rightnode)

        new_root = rotateLeft(tree, node)
        _balanceImpl(new_root)


#Ejercicio 4
def insert(tree: AVLTree, element, key: int) -> int | None:
    newNode = AVLNode()
    newNode.value = element
    newNode.key = key

    if tree.root is None:
        tree.root = newNode
        return newNode.key
    else:
        new_key = _insertImpl(newNode, tree.root)
        reBalance(tree)

        return new_key

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


#Ejercicio 5
def delete(tree: AVLTree, key: int) -> int | None:
    if tree.root is None:
        return None

    deleted_key = _deleteImpl(tree, tree.root, key)

    if deleted_key is not None:
        reBalance(tree)
    
    return deleted_key

def _deleteImpl(tree: AVLTree, currentNode: AVLNode, key: int) -> int | None:
    if currentNode is None:
        return None

    if currentNode.key == key:
        # si el nodo es una hoja o tiene un solo hijo
        if currentNode.leftnode is None or currentNode.rightnode is None:
            if currentNode.leftnode is not None:
                child = currentNode.leftnode
            else: 
                child = currentNode.rightnode

            if currentNode.parent is None: # si el nodo es la raíz
                tree.root = child
                if child is not None: 
                    child.parent = None
            else: 
                if currentNode.parent.leftnode == currentNode:
                    currentNode.parent.leftnode = child
                else: 
                    currentNode.parent.rightnode = child
                    
                if child is not None:
                    child.parent = currentNode.parent

        # nodo con dos hijos
        else:
            child = min_node(currentNode.rightnode)
            
            currentNode.key = child.key
            currentNode.value = child.value
            
            _deleteImpl(tree, currentNode.rightnode, child.key)
        
        return key
        
    elif key > currentNode.key:
        _deleteImpl(tree, currentNode.rightnode, key)
    else:
        _deleteImpl(tree, currentNode.leftnode, key)

def min_node(node: AVLNode) -> AVLNode:
    while node.leftnode is not None:
        node = node.leftnode
    return node


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


if __name__ == "__main__":
    tree = AVLTree()

    insert(tree, "e", 30)
    insert(tree, "c", 25)
    insert(tree, "d", 28)
    insert(tree, "b", 15)
    insert(tree, "a", 10)
    insert(tree, "f", 40)

    calculateBalance(tree)
    print_inPostOrder(tree)

    insert(tree, "j", 12)
    insert(tree, "k", 13)
    print_inPostOrder(tree)

    delete(tree, 30)
    print_inPostOrder(tree)