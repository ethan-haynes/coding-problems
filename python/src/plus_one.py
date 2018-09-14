def plus_one(digits):
    n = int(('{}'*digits).format(*digits)) + 1
    return [int(i) for i in str(n)]
