if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        s = input()
        if ('insert' in s):
            s = s.split()
            arr.insert(int(s[1]),int(s[2]))
        elif ('print' in s):
            print(arr)
        elif ('remove' in s):
            s = s.split()
            arr.remove(int(s[1]))
        elif ('append' in s):
            s = s.split()
            arr.append(int(s[1]))
        elif ('sort' in s):
            arr.sort()
        elif ('pop' in s):
            arr.pop()
        elif ('reverse' in s):
            arr.reverse()

