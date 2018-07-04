const maxSpan = (arr) => {
  let dict = {}
  let last = arr.length-1
  let max = 1
  for (let i = 0; i < arr.length; i++) {
    if (dict[arr[i]] === undefined) {
        dict[arr[i]] = i
    }
    if (dict[arr[last-i]] === undefined) {
        dict[arr[last-i]] = last-i
    }
    if (dict[arr[i]] != i) {
      max = dict[arr[i]] - i + 1
      break;
    }
    if (dict[arr[last-i]] != last-i) {
      max = (last-i) - (dict[arr[last-i]]) + 1
      break;
    }
  }
  return max
}
console.log(maxSpan([1, 2, 1, 1, 3]))
console.log(maxSpan([1, 4, 2, 1, 4, 1, 4]))
console.log(maxSpan([1, 4, 2, 1, 4, 4, 4]))
