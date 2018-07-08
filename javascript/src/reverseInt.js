/**
 * @param {number} x
 * @return {number}
   O(n) runtime
   Runtime beats 99.63 % of javascript submissions on leetcode
 */
var reverse = function(x) {
  let low = -2147483648,
      high = 2147483647,
      temp = Math.abs(x),
      sign = Math.sign(x)
  if (temp/10 < 1) { return x }

  let length = Math.ceil(Math.log10(temp+1)),
      num = 0,
      previousPlace = 10**(length-1||1),
      nextPlace = 1

  for (var i = 0; i < length+1; i++) {
    num += (Math.floor(temp/previousPlace)%10) * nextPlace
    previousPlace /= 10
    nextPlace *= 10
  }
  let out = num * sign
  return (out <= low || high < out) ? 0 : out
}
console.log(reverse(123))
console.log(reverse(-123))
console.log(reverse(10))
console.log(reverse(120))
console.log(reverse(123456)) // 654321
console.log(reverse(100)) // 1
console.log(reverse(1534236469)) // 0
console.log(reverse(-1563847412)) // 0
