const isUnique = (obj) =>
  (function uniqueCheck(set, obj) {
    for (let [key,value] of Object.entries(obj)) {
      if (set.has(key)) return false

      set.add(key)

      if (Array.isArray(value)) {
        if (value.reduce((x, y) => x || set.has(y), false)
            || value.length !== new Set(value).size) return false
        set.add(...value)
      } else if (typeof value === 'object') {
        if (uniqueCheck(set, value) !== undefined) return false
      } else {
        if (set.has(value)) return false

        set.add(value)
      }
    }
  })(new Set(), obj) === undefined
