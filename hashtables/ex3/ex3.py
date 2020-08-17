def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    intersections = []

    for array in arrays:
        for value in array:
            # if value in cache and not in results add tvalue
            if value in cache and value not in intersections:
                intersections.append(value)
            else:
                cache[value] = True
    print(intersections)
    
    return intersections


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
