from dictionary import Dictionary, insert, delete, print_dict, next_prime

#Ejercicio 4
def check_permutation(S: str, P: str) -> bool:
    if len(S) != len(P):
        return False

    D = Dictionary(27)

    for char in S:
        insert(D, ord(char), char)

    for char in P:
        delete(D, ord(char))

    for i in D.dictionary:
        if i.head is not None:
            return False

    return True

print(check_permutation("qweqwe", "ewqewq"))

#Ejercicio 5
def check_unique(L: list[int]) -> bool:
    if len(L) == 0:
        return False
    
    D = Dictionary(next_prime(len(L)))

    for num in L:
        insert(D, num, num)

    for i in D.dictionary:
        if i.head and i.head.nextNode:
            return False

    return True

print(check_unique([1,2,3,4,5]))