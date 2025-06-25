sentences = [
    "Python is awesome",
    "I love coding",
    "Short",
    "This is a slightly longer sentence"
]

sortedSentence = sorted(sentences,key= lambda x: -len(x))
print(sortedSentence)