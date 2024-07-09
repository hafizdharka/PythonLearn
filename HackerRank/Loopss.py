if __name__ == '__main__':
    n = int(input())
    if n>0 and n<=20:
        a = list(i for i in range (n))
        for i in a:
            print(i**2)
