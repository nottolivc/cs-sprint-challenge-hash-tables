# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    result = []

    for file in files:
        suffix = file.rsplit("/", 1)[-1]
    
        if suffix not in dictionary:
            dictionary[suffix] = [file]
        else:
            dictionary[suffix].append(file)

    for query in queries:
        try:
            for path in dictionary[query]:
                result.append(path)
        except:
            pass

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
