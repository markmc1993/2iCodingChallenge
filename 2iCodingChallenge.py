def get_sum_pairs_number(x, arr):
    count = 0
    count2 = 0
    while len(arr):
        for i in reversed(arr):
            if i > x:
                arr.remove(i)
        for i in reversed(arr):
            if len(arr) > 1:
                for j in arr[:-1]:
                    if i + j == x:
                        arr.remove(i)
                        arr.remove(j)
                        count += 1
                        count2 += 1
                        break
            if len(arr) and not count2:
                arr.remove(arr[-1])
            count2 = 0
    return(count)