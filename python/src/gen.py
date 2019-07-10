from random import random

def gen(word):
    n = len(word)
    def _gen():
        i = int(random() * n)
        j = int(random() * (n-i)+1) + i
        if j == n:
            return (word[i],None)
        return (word[i],word[j])

    return _gen

func = gen("cats")

def guess(func, num):
    
    def search(graph, v, num):
        words = []
        for e in graph[v]:
             words.append(v + search(graph, e, num - 1))
        
        try:
            word = next(filter(lambda w: len(w) == num, words))
            return word
        except StopIteration as e:
            return v
    
    graph = {}
    word = ""

    while len(word) != num:
        ch1, ch2 = func()
        if ch1 not in graph:
            graph[ch1] = set()
        
        if ch2 != None:
            if ch2 not in graph[ch1]:
                graph[ch1].add(ch2)
            if ch2 not in graph:
                graph[ch2] = set()
        
        for v in graph:
            word = search(graph, v, num)
            if len(word) == num: 
                break
    
    return word

print(guess(func, 4))
print(guess(gen('what?'), 5))
