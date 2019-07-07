def distribute(ratings):
    n = len(ratings)
    dist = [1]

    for i in range(1,n):
        dist.append(1)
        if ratings[i] > ratings[i-1]:
            while dist[i] <= dist[i-1]:
                dist[i] += 1

    for i in range(n-1,-1,-1):
        if ratings[i] < ratings[i-1]:
            while dist[i-1] <= dist[i]:
                dist[i-1] += 1
    
    return sum(dist)

print(distribute([1,2]))
print(distribute([8,2,2,3]))
print(distribute([1,2,3,4,5,4,3,2,1]))
