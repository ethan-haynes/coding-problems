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
console.log(maxSpan([1, 2, 1, 1, 3]))
console.log(maxSpan([1, 4, 2, 1, 4, 1, 4]))
console.log(maxSpan([1, 4, 2, 1, 4, 4, 4]))
console.log(maxSpan([1,2,1,4,5,6,7,8,9,10,11]))
