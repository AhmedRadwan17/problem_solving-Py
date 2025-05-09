friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def trim_if_upper(string):
    if string[0].isupper() or string[-1].isupper():
        return string[1:-1]
    return string

MyResults = map(trim_if_upper, friends_map)

print(list(MyResults))

print("-----------------------------------------------------------------------------------")

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

MyResults = map(lambda s: s[1:-1] if s[0].isupper() or s[-1].isupper() else s, friends_map)

print(list(MyResults))
