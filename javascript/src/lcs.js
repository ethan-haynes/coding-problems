const lcs = (s1, s2) => {
  let res = ['', '']
  let i = -1, j = -1
  let set = new Set([...s2]) 

  while(++i < s1.length) {
    if (j+1 >= s2.length) {
      j = -1
      res = [res[0].length > res[1].length ? res[0] : res[1], '']
    }

    if (set.has(s1[i])) {
      while(++j < s2.length) {
        if (s1[i] === s2[j]) {
          res[1] += s1[i]
          break;
        }
      }
    }
  }

  return res.pop()
}
console.log(lcs('AGGTAB', 'GXTXAYB'))
console.log(lcs('ABCDE', 'BCDEA'))
console.log(lcs('ABCDE', 'FGHIJ'))
