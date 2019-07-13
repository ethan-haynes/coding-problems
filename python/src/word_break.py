def word_graph(_str, _dict):
    wg = dict()
    for word in _dict:
        indx = _str.rfind(word)
        if indx == -1:
            continue
        if indx in wg:
            wg[indx].append(word)
        else:
            wg[indx] = [word]
    return wg

def get_sentences(words, start, end):
    sentences = []
    
    for word in words.get(start, []):
        if start + len(word) == end:
            return [word]
        for sentence in get_sentences(words, start + len(word), end):
            if len(sentence):
                sentences.append(word + " " + sentence)
    
    return sentences

def word_break(_str, _dict):
    words = word_graph(_str, _dict) # dict(starting_index=[str: word])
    return get_sentences(words, 0, len(_str))

print(word_break("catsanddog",["cats","cats","and","sand","dog"]))
print(word_break("pineapplepenapple",["apple","pen","applepen","pine","pineapple"]))
