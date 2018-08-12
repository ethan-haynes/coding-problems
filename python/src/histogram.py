def histogram(text):
    hist = {}
    words = text.split()
    for word in words:
        if word in hist:
            hist[word] += 1
        else: hist[word] = 1
    return hist

print(histogram('word word word cat cat dog dog dog dog bird'))
