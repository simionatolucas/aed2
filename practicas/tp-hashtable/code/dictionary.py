from linkedlist import LinkedList, add as lkAdd, delete as lkDelete

#Ejercicio 2
class Dictionary:
    def __init__(self, m: int):
        self.m = m
        self.dictionary = [LinkedList() for i in range(m)]

    def hash_function(self, key: int) -> int:
        return key % self.m

def insert(D: Dictionary, key: int, value) -> Dictionary:
    if key < 0:
        # raise ValueError("La key debe ser un entero positivo.")
        return D

    position = D.hash_function(key)
    lkAdd(D.dictionary[position], [key, value])

    return D

def search(D: Dictionary, key: int):
    if key < 0:
        # raise ValueError("La key debe ser un entero positivo.")
        return None

    position = D.hash_function(key)

    currentNode = D.dictionary[position].head
    while currentNode:
        if currentNode.value[0] == key:
            return currentNode.value[1]

        currentNode = currentNode.nextNode

    return None

def delete(D: Dictionary, key: int):
    if key < 0:
        # raise ValueError("La key debe ser un entero positivo.")
        return D
    
    position = D.hash_function(key)

    currentNode = D.dictionary[position].head
    while currentNode:
        if currentNode.value[0] == key:
            lkDelete(D.dictionary[position], currentNode.value)
            return D

        currentNode = currentNode.nextNode

    return D

def print_dict(D: Dictionary):
    for i in range(0, D.m):
        currentNode = d.dictionary[i].head

        if currentNode:
            print(f"Entradas en la posición {i}:")

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.nextNode


if __name__ == "__main__":
    d = Dictionary(9)
    insert(d, 3, "asd")
    insert(d, 12, "qweqwe")
    insert(d, 21, "zxczxc")
    insert(d, 30, "cvbbn")

    print_dict(d)

    delete(d, 21)

    print_dict(d)
