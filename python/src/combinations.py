def combs(n,k,start=1):
    combs_list = []
    if k == 0:
        return combs_list

    for num in range(start, n+1):
        if k == 1:
            combs_list.append([num])
        for sub_combs in combs(n,k-1,num+1):
            combs_list.append([num] + sub_combs)

    return combs_list

print(combs(4,2))
