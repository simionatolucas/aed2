def contiene_suma(A: list, n: int):
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] + A[j] == n:
                print(f"El elemento en la posición {i} ({A[i]}) sumado al elemento en la posición {j} ({A[j]}) da por resultado {n}.")
                return True
    return False

A = [3, 5, 1, 7, 2, 6, 10]
contiene_suma(A, 8)