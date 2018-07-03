const hasPair = require('../src/hasPair')

const arr = [-1,1,2,5,3,4,5]

console.log(
  (ans => `${ans} should equal false: ${false === ans}`)(hasPair(arr, -1))
)
console.log(
  (ans => `${ans} should equal true: ${true === ans}`)(hasPair(arr, 0))
)
console.log(
  (ans => `${ans} should equal true: ${true === ans}`)(hasPair(arr, 8))
)
console.log(
  (ans => `${ans} should equal true: ${true === ans}`)(hasPair(arr, 10))
)
console.log(
  (ans => `${ans} should equal false: ${false === ans}`)(hasPair(arr, 11))
)
