// subsequence
const D = ["able", "ale", "apple", "bale", "kangaroo"]
const S = 'abppplee'

const subsequence = (str, dict) => {
  const histogram = {}
  let sub = ''

  for (let letter of str) {
    histogram[letter] = ++histogram[letter] || 1
  }

  for (let word of dict) {
    if (
      [...word].every(letter => histogram[letter])
      && word.length > sub.length
    ) sub = word
  }

  return sub
}
console.log(subsequence(S, D))
