class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        next = self.trie
        for char in word:
            if char not in next:
                next[char] = {}
            next = next[char]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def deep_search(head, chars):
            next = head
            for i, char in enumerate(chars):
                if char  == '.':
                    if i == len(chars) - 1: return True
                    for key in next.keys():
                        if deep_search(next[key], chars[i+1:]): return True

                    return False
                else:
                    if char in next:
                        if i == len(chars) - 1: return True
                        next = next[char]
                    else: return False
        return deep_search(self.trie, word)

        
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('word')
print(obj.search('word'))
obj.addWord('cats')
obj.addWord('cord')
print(obj.search('cats'))
print(obj.search('wor.'))
print(obj.search('w.rd'))
print(obj.search('cord'))
print(obj.search('..rd'))
obj.addWord('ball')
obj.addWord('belt')
print(obj.search('b.l.'))
