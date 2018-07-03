const stringSplosion = (str) => {
  let arr = []

  return [...str].map((letter,i) =>
    arr[arr.push((arr[i-1] || '') + letter)-1]
  ).join('')
}
console.log(stringSplosion('ab'))
console.log(stringSplosion('Code'))
