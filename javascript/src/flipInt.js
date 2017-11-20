/*
  Write a function that takes a positive integer and reverses it. Do so
  without string manipulation, arrays, or bitwise operators.

  Example:
    An input of 123 would return 321
*/
const flipInt = (n) => {
  let temp = n,
        num = 0

  for (let i = Math.floor(Math.log10(n)); i >= 0; i--) {
    num += 10**i * (temp % 10)
    temp = Math.floor(temp/10)
  }
  return num
}

module.exports = flipInt
