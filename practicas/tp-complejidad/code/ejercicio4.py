import random

def partition(array, start, end):
    pivot = random.randint(start, end)
    pivot_value = array[pivot]

    array[pivot], array[end] = array[end], array[pivot]

    left = start
    for i in range(start, end):
        if array[i] < pivot_value:
            array[i], array[left] = array[left], array[i]
            left += 1

    array[left], array[end] = array[end], array[left]
    return left

def quickselect(array, target):
    left = 0
    right = len(array) - 1

    while True:
        if left == right:
            return array[left]

        pivot = partition(array, left, right)

        if pivot == target:
            return array[target]
        
        if pivot < target:
            left = pivot + 1
        elif pivot > target:
            right = pivot - 1

def order(array):
    mid = quickselect(array, round(len(array)/2 - 1))
    center_index = round(len(array)/2 - 1)
    print(f"El elemento central es {mid}, que una vez ordenado, está en la posición {center_index}.")
    print(f"Lista luego de realizar Quickselect: {array}")

    count_smaller = 0 # cuántos elementos más pequeños tengo a la izquierda
    for i in range(center_index):
        if array[i] < array[center_index]:
            count_smaller += 1

    desired_left = round(count_smaller / 2) # cuántos elementos más pequeños quiero tener a la izquierda

    print(f"Tenemos {count_smaller} elementos menores que {mid} en la parte izquierda, y queremos dejar solo {desired_left}.")

    left = 0
    right = center_index + 1

    while count_smaller > desired_left:
        while array[left] >= mid:  # buscar un elemento menor que el centro que esté a la izquierda
            left += 1

        while array[right] <= mid: # buscar un elemento mayor que el centro que esté a la derecha
            right += 1

        array[left], array[right] = array[right], array[left]

        count_smaller -= 1

        left += 1
        right += 1

    return(array)

if __name__ == "__main__":
    #arr = [11,6,3,4,8,2,9,7,1,5,10,45,23]
    arr = [89,48,2,25,52,69,66,86,77,95,30,34,73,13,11,88,27,97,33,71]
    print(f"Lista original: {arr}")
    print(f"Lista ordenada: {sorted(arr)}")
    print(f"Lista final: {order(arr)}")