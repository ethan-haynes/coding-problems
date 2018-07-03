/* 
  QUESTION: 
    Given an array of integers, and a number ‘sum’, 
    return a Boolean denoting whether there is a pair
    of integers in the array whose sum is equal to ‘sum’.
  NOTE: 
    Expected time complexity O(n)
*/
module.exports = (arr, sum) => {
  const comps = new Set() // set of complimenting pairs
  return arr.some(item => comps.has(item) || (comps.add(sum-item), false))
}
