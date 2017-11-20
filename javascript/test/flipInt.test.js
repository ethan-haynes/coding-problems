const flipInt = require('../src/flipInt')

console.log(
  (ans => `${ans} should equal 321: ${321 === ans}`)(flipInt(123))
)

console.log(
  (ans => `${ans} should equal 123: ${123 === ans}`)(flipInt(321))
)

console.log(
  (ans => `${ans} should equal 8765: ${8765 === ans}`)(flipInt(5678))
)

console.log(
  (ans => `${ans} should equal 123456789: ${123456789 === ans}`)
  (flipInt(987654321))
)
