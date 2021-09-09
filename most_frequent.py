def most_frequent(string):
    string = string.lower()
    dictionary = {}
    for i in string:
        dictionary[i] = string.count(i)
    keys = list(dictionary.keys())
    value = list(dictionary.values())
    while (len(value) != 0):
        i = value.index(max(value))
        print(keys[i], "=", value[i])
        value.pop(i)
        keys.pop(i)
    

string = str(input("Enter a string: "))
most_frequent(string)
