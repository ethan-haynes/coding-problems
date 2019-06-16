def firstUniqChar(s: str) -> int:
    if len(s) == 0: 
        return -1
    
    hist = {}
    for i, ch in enumerate(s):
        if ch in hist:
            hist[ch][0] += 1
        else:
            hist[ch] = [1, i]
            
    repeats = sorted(hist, key=hist.get)
    count, index = hist[repeats[0]]
    
    if count > 1:
        return -1
    else: return index
