def count_characters(file_path):
    """Count number of characters.
    The file is read segment by segment, so there is no limit on file size.
    If the file does not exist, return an empty dictionary {}.
    
    :param file_path: the path of the file which characters is to be counted.
    :return dictionary: {"count": number of characters, ...count of each character category}.
        Return empty {} if file was not found.
        e.g.{'count': 33, ' ': 3, '吗': 1, '你': 1, 'r': 2, 'H': 2, 'e': 2, '!': 1, 'u': 1, 
        '？': 1, 'a': 1, '?': 1, 'w': 2, 'o': 4, '\n': 5, 'y': 1, '好': 1, 'l': 3, 'd': 1}
    """

    dict1 = {}
    count = 0
    f = None
    try:
        f = open(file_path, "r")
        while True:
            str1 = f.read(10240)
            if str1 == "":
                break
            for c in str1:
                dict1[c] = dict1.get(c, 0) + 1
                count += 1
        f.close()
        dict1["count"] = count
        return dict1
    except FileNotFoundError:
        print("File was not found: ", file_path)
        return {}
    finally:
        if f is not None:
            f.close()
