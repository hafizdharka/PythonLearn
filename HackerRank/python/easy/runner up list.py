if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    maxv = max(arr)
    newlist = []
    
    for i in range(len(arr)):
        if arr[i]!=maxv:
            newlist.append(arr[i])
    
    print(max(newlist))
