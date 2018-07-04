/*
  QUESTION:
  Consider the leftmost and righmost appearances of some
  value in an array. We'll say that the "span" is the number
  of elements between the two inclusive. A single value has
  a span of 1. Returns the largest span found in the given
  array.
  NOTE:
    Expected time complexity O(n)
*/
const maxSpan = (arr) => {
  let dict = {}
  let last = arr.length-1
  let max = 1
  for (let i = 0; i < arr.length; i++) {
    if (arr.length/2 < i) break;

    if (dict[arr[i]] === undefined) {
        dict[arr[i]] = i
    }
    if (dict[arr[last-i]] === undefined) {
        dict[arr[last-i]] = last-i
    }
    if (dict[arr[last-i]] != last-i) {
      tempMax = Math.abs((last-i) - (dict[arr[last-i]])) + 1
      if (max < tempMax) {
        max = tempMax
      }
    }

    if (dict[arr[i]] != i) {
      tempMax = Math.abs(dict[arr[i]] - i) + 1
      if (max < tempMax) {
        max = tempMax
      }
    }
  }
  return max
}
console.log(maxSpan([1, 2, 1, 1, 3])) // 4
console.log(maxSpan([1, 4, 2, 1, 4, 1, 4])) // 6
console.log(maxSpan([1, 4, 2, 1, 4, 4, 4])) // 6
console.log(maxSpan([1,2,1,4,5,6,7,8,9,10,11])) // 3
