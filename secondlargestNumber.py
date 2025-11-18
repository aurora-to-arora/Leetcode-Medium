 if len(arr) < 2:
        return -1

    largest = second = float('-inf')

    for x in arr:
        if x > largest:
            second = largest
            largest = x
        elif x > second and x != largest:
            second = x

    return second if second != float('-inf') else -1


##OR###
