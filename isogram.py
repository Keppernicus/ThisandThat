def is_isogram(string):
    string_list = sorted([i for i in string.lower() if i not in ",- "])
    print(string_list)
    string_set = sorted({i for i in string.lower() if i not in ",- "})
    print(string_set)
    return string_list == string_set
