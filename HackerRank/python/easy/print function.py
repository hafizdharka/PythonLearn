if __name__ == '__main__':
    n = int(input())
    a = list(i+1 for i in range(n))
    z = ""
    for i in a:
        z = z + str(i)
    print(z)
        
        
