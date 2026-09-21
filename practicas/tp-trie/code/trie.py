from linkedlist import LinkedList, add as LLadd, getNodeValue as LLgetNode, delete as LLdelete

class Trie:
    def __init__(self):
        self.root = TrieNode()

class TrieNode:
    def __init__(self):
        self.parent = None
        self.children = LinkedList()
        self.key = None
        self.isEndOfWord = False


#Ejercicio 1
def insert(T: Trie, element: str):
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


def search(T: Trie, element: str) -> bool:
    currentNode = T.root

    for i in element:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            return False

        currentNode = node

    return currentNode.isEndOfWord


#Ejercicio 3
def delete(T: Trie, element: str) -> bool:
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


#Ejercicio 4
def findPrefix(T: Trie, p: str, n: int):
    currentNode = T.root
    if len(p) > n:
        print("El prefijo debe ser más corto que la longitud de la palabra.")
        return False

    for i in p:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            print("No existen palabras con ese prefijo.")
            return False

        currentNode = node

    _findPrefixImpl(currentNode, p, n-len(p))


def _findPrefixImpl(currentNode: TrieNode, word: str, n: int):
    if n == 0:
        if currentNode.isEndOfWord:
            print(word)
        return

    current = currentNode.children.head

    while current is not None:
        j = current.value
        _findPrefixImpl(j, word + j.key, n-1)
        current  = current.nextNode


if __name__ == "__main__":
    T = Trie()

    insert(T, "casa")
    insert(T, "caso")
    insert(T, "cama")
    insert(T, "camino")
    insert(T, "casamiento")
    insert(T, "perro")
    insert(T, "perla")

    print("Palabras con prefijo 'ca' y longitud 4:")
    findPrefix(T, "ca", 4)

    print("\nPalabras con prefijo 'ca' y longitud 5:")
    findPrefix(T, "ca", 5)

    print("\nPalabras con prefijo 'cas' y longitud 4:")
    findPrefix(T, "cas", 4)

    print("\nPalabras con prefijo 'per' y longitud 5:")
    findPrefix(T, "per", 5)
