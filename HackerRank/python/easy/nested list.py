if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
    s = sorted(arr, key=lambda x: (x[1],x[0]))
    for i in range(len(s)-1):
        if (s[i+1][1])!=(s[i][1]):
            samei = [s[i+1][0]]
            for j in range(i+1,len(s)-1):
                if s[j][1]==s[j+1][1]:
                    samei.append(s[j+1][0])
                else: break
            print("\n".join(samei))
            break
                    
