def findWords(board, words):
    """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
    """
    out = []
    def has_word(word, ittr, root=None):
        x,y = ittr
        r_char = board[y][x] #root char

        if r_char in word[0]: 
            i = word[0].index(r_char)
            word[0] = word[0][:i] + word[0][i+1:]
            if root == None: root = [x,y]
                                
        if y < len(board) - 1: has_word(word, [x, y+1], root)
        if x < len(board[y]) - 1: has_word(word, [x+1, y], root)
            
        if len(word[0]) == 0: return True
        if ittr == root: word[0] = word[1]
            
    for word in words:
        if 0 < len(word) and has_word([word, word], [0, 0]): 
            if word not in out:
                out.append(word)
    return out
