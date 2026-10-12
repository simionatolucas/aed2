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


#Ejercicio 8
def find_first(s: str, substr: str) -> int | None:
    n = len(s)
    m = len(substr)

    if m > n:
        return None

    if m == 0:
        return 0

    base = 31
    mod = 101 # utilizamos modulo para evitar overflow en cadenas muy grandes

    slide = pow(base, m - 1, mod) # desplazamiento del primer caracter

    hash_substr = 0
    hash_window = 0

    for i in range(m):
        hash_substr = (hash_substr * base + ord(substr[i])) % mod
        hash_window = (hash_window * base + ord(s[i])) % mod

    for i in range(n - m + 1):
        if hash_window == hash_substr: 
            if s[i:i + m] == substr:    # verificar colisiones
                return i

        if i < n - m:
            hash_window = ((hash_window - ord(s[i]) * slide) * base + ord(s[i + m])) % mod

    return None


#Ejercicio 9
def check_subset(S: list[int], T: list[int]) -> bool:
    if len(S) > len(T):
        return False

    D = Dictionary(len(T))

    for i in T:
        insert(D, i, i)

    for i in S:
        if search(D, i) is None:
            return False

    return True


if __name__ == "__main__":
    print("Ejercicio 4:")
    print(check_permutation("qweqwe", "ewqewq"))

    print("\nEjercicio 5:")
    print(check_unique([1,2,3,4,5]))

    print("\nEjercicio 6:")
    postal_dict = Dictionary(1009) # Número primo
    codigo1 = "C1024CWN"
    codigo2 = "H0544MDZ"

    print(postal_dict.hash_function(postal_hash(codigo1)))
    print(postal_dict.hash_function(postal_hash(codigo2)))

    print("\nEjercicio 7:")
    print(compression("aaaabbccd"))

    print("\nEjercicio 8:")
    print(find_first("aabbccddabcde", "abc"))

    print("\nEjercicio 9:")
    print(check_subset([2,3,4], [1,2,3,4,5]))