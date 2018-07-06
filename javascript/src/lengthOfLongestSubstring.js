const lengthOfLongestSubstring = function(s) {
  let sub = {},
      length = 0,
      templength = 0,
      offset = 0,
      index = 0
  for (const letter of s) {
    if (sub[letter] != undefined && sub[letter] >= offset) {
      templength -= (sub[letter] - offset)
      offset = sub[letter]+1
    } else {
      templength++
    }
    if (length < templength) {
      length = templength
    }
    sub[letter] = index
    index++
  }
  return length
}

console.log(lengthOfLongestSubstring("abc")) // 3
console.log(lengthOfLongestSubstring("abcabcbb")) // 3
console.log(lengthOfLongestSubstring("pwwkew")) // 3
console.log(lengthOfLongestSubstring("dfdv")) // 3
console.log(lengthOfLongestSubstring("abba")) // 2
console.log(lengthOfLongestSubstring("bbtablud")) // 6
