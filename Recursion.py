def Recursion(Word):
    if len(Word)==1:
        return Word
    if Word[0] == Word[1] :
        return Recursion(Word[1:])
    return Word[0]+Recursion(Word[1:])
print(Recursion("WWWoorlddddd"))
