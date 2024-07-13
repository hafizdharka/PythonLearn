if __name__ == '__main__':
    n = int(input().strip())
    thelist = map(int, input().strip().split())
    t = tuple(thelist)
    print(hash(t))
