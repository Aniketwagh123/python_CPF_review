def pre_sum(arr):
    if not len(arr) > 0:
        return arr

    new_array = []
    new_array.append(arr[0])
    for i in range(1, len(arr)):
        new_array.append(arr[i] + arr[i-1])

    return new_array


def pre_sum2(arr):
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i]+arr[i-1]
    return arr


if __name__ == "__main__":
    array = [7, 12, 11, 29, 51, 6, 4, 3, 2]
    print(pre_sum2(array))
