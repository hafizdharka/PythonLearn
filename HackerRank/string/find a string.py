def count_substring(string, sub_string):
    s = 0
    c = 0
    for i in range(len(string)-len(sub_string)+1):
        c += string[s:s+len(sub_string)].count(sub_string)
        s +=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
