const hasPair = require('../src/hasPair')

const arr = [-1,1,2,5,3,4,5]
const reset = '\x1b[0m'
const green = '\x1b[32m'
const red = '\x1b[31m'
const answer = bool => bool ? `${green} correct${reset}` : `${red} incorrect${reset}`

console.log(
  (ans => `${reset}${ans} should equal false: ${answer(false === ans)}`)(hasPair(arr, -1))
)
console.log(
  (ans => `${reset}${ans} should equal true: ${answer(true === ans)}`)(hasPair(arr, 0))
)
console.log(
  (ans => `${reset}${ans} should equal true: ${answer(true === ans)}`)(hasPair(arr, 8))
)
console.log(
  (ans => `${reset}${ans} should equal true: ${answer(true === ans)}`)(hasPair(arr, 10))
)
console.log(
  (ans => `${reset}${ans} should equal false: ${answer(false === ans)}`)(hasPair(arr, 11))
)
