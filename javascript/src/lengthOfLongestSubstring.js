/*
  first approach used a temp array insead of templength & offset
  there were two drawbacks with that approach:
    1) it used O(n) space complexity in adition to the
       histogram space complexity (i.e., sub = {})
    2) it was expensive to resize when we backtracked to on the substring
       when we encountered duplicated
  second approach used the same thought behind the array, but managed an
  offset value and length meta values instead of holding the values in memory.
  this allows us to keep our place in the logical construction of the substring
  without having to manage the bookkeeping of trimming the array.
*/
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
