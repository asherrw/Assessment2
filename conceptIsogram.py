def is_isogram(word):
    string = str(word)
    sentence = string.replace(" ", "")
    return len(sentence) == len(set(sentence.lower()))

print(is_isogram("CodeFirstGirls"))
print(is_isogram(12))
