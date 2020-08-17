def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {} # cache will be taking the form of a dict
    if length < 2:
        return None
    for index, w in enumerate(weights):
        if w not in cache:
            cache[w] = index

    for item in range(length):
        # store each weight as key
        item_weight = weights[item]
        new_weight = limit - item_weight

        if new_weight in cache and cache[new_weight] != item:
            return(max(item, cache[new_weight]), min(item, cache[new_weight]))

    return None
