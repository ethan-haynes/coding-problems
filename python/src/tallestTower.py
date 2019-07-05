def tallestTower(ppl):
    
    def __tallestTower(ppl, last_ht, last_wt, memo=None):
        if len(ppl) == 0:
            return 0
        if memo is None:
            memo = {}
            
        towers = []

        for i,p in enumerate(ppl):
            ht, wt = p
            key = f'{ht},{wt},{last_ht},{last_wt}'
            if key not in memo:
                memo[key] = 0
                if ht < last_ht and wt < last_wt:
                    memo[key] = 1 + __tallestTower(ppl[i+1:], ht, wt, memo)
                else:
                    memo[key] = __tallestTower(ppl[i+1:] + [ppl[i]], last_ht, last_wt, memo)
                towers.append(memo[key])
        if len(towers):
            return max(towers)
        else:
            return 0

    return __tallestTower(ppl, float("inf"), float("inf"))
    
print(tallestTower([(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]))

