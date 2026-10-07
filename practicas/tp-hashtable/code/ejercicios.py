from dictionary import Dictionary, insert, search, delete, print_dict, next_prime

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


#Ejercicio 6
def postal_hash(code: str):
    value = 0
    i = len(code) - 1

    for char in code:
        try:
            value += int(char) * (26 ** i)
        except ValueError:
            value += (ord(char) - ord('A')) * (26 ** i)
        i -= 1

    return value

postal_dict = Dictionary(1009) # Número primo
codigo1 = "C1024CWN"
codigo2 = "H0544MDZ"

print(postal_dict.hash_function(postal_hash(codigo1)))
print(postal_dict.hash_function(postal_hash(codigo2)))

#Ejercicio 7
def compression(s: str) -> str:
    D = Dictionary(26)
    res = ""

    for char in s:
        if search(D, ord(char)):
            key = D.hash_function(ord(char))
            D.dictionary[key].head.value[1] += 1
        else:
            insert(D, ord(char), 1)

    for i in D.dictionary:
        if i.head:
            count = i.head.value[1]
            res += f"{chr(i.head.value[0])}{count}"

    if len(res) < len(s):
        return res
    else:
        return s

print(compression("aaaabbccd"))