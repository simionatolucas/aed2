from linkedlist import LinkedList, add as LLadd, getNodeValue as LLgetNode, delete as LLdelete

class Trie:
    root = None

class TrieNode:
    parent = None
    children = LinkedList()
    key = None
    isEndOfWord = False


#Ejercicio 1
def insert(T: Trie, element):
    currentNode = T.root

    for i in element:
        node = LLgetNode(currentNode.children, i)

        if node:
            currentNode = node
        else:
            newNode = TrieNode()
            newNode.parent = currentNode
            newNode.key = i

            LLadd(currentNode.children, newNode)

            currentNode = newNode

    currentNode.isEndOfWord = True
    return


def search(T: Trie, element) -> bool:
    currentNode = T.root

    for i in element:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            return False

        currentNode = node

    return currentNode.isEndOfWord


#Ejercicio 3
def delete(T: Trie, element) -> bool:
    currentNode = T.root

    for i in element:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            return False

        currentNode = node

    if not currentNode.isEndOfWord:
        return False

    currentNode.isEndOfWord = False

    if currentNode.children.head is not None: # Si el nodo tiene hijos no podemos eliminarlo.
        return True
    
    while currentNode != T.root:
        parent = currentNode.parent

        LLdelete(parent.children, currentNode)

        currentNode = parent

        # Verificamos si recorriendo hacia arriba los nodos tienen hijos o son otras palabras.
        if currentNode.children.head is not None:
            break

        if currentNode.isEndOfWord:
            break

    return True
            
trie = Trie()
trie.root = TrieNode()
insert(trie, "casa")

print(search(trie, "casa"))

insert(trie, "casamiento")

print(delete(trie, "casamiento"))

print(search(trie, "casa"))
print(search(trie, "casamiento"))